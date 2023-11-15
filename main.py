from ctypes import cdll, c_char_p, c_void_p

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

lib = cdll.LoadLibrary("./dtext.so")
lib.DText_destroy.argtype = (c_void_p,)
lib.DText_parse.argtype = (c_char_p,)
lib.DText_parse.restype = c_void_p


def parse_dtext(dtext: str):
    buffer = dtext.encode()
    pointer = c_char_p(lib.DText_parse(buffer))
    html = pointer.value.decode()
    lib.DText_destroy(pointer)
    return html


app = FastAPI(title="dtext-docker")
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/", include_in_schema=False)
async def route_index():
    return RedirectResponse("/docs")


@app.post("/dtext-parse", summary="Parse Danbooru DText strings into HTML.")
async def route_manga_ocr(strings: list[str]) -> list[str]:
    return [parse_dtext(string) for string in strings]
