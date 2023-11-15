g++ -shared \
  -std=c++20 -O2 -pipe -flto -fno-strict-aliasing -D_GNU_SOURCE -DNDEBUG \
  ./dtext_rb/ext/dtext/dtext.cpp \
  ./wrapper.cpp \
  -o dtext.so
