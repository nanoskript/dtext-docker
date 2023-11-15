FROM python:3.10-slim-bookworm

RUN apt-get update && apt-get install -y g++

RUN pip install --no-cache-dir pdm
ADD ./pyproject.toml ./pdm.lock ./
RUN pdm sync && pdm cache clear

ADD ./dtext_rb ./dtext_rb
ADD ./build.sh ./wrapper.cpp ./
RUN ./build.sh

ADD ./main.py ./

CMD ["pdm", "run", "uvicorn", \
	"--host", "0.0.0.0", "--port", "$PORT", \
	"main:app"]
