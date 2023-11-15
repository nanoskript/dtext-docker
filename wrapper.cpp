#include "dtext_rb/ext/dtext/dtext.h"

#include <iostream>
#include <set>

extern "C" {
    char* DText_parse(const char* text) {
        DTextOptions options;
        options.base_url = "https://danbooru.donmai.us";
        options.domain = "https://danbooru.donmai.us";
        options.internal_domains = {"https://danbooru.donmai.us"};

        auto [html, _wiki_pages] = StateMachine::parse_dtext(text, options);
        char* string = new char[html.length() + 1];
        std::strcpy(string, html.c_str());
        return string;
    }

    void DText_destroy(char* string) {
        delete string;
    }
}
