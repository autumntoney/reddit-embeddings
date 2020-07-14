#!/usr/bin/env python3

import re

def remove_urls(s):
    s = remove_urls.REGEX.sub("", s)
    return s
remove_urls.REGEX = re.compile("https?://.+\s?")

def testf():
    print(remove_urls("hello https://google.com http://www.google.com world"))

if __name__ == "__main__":
    testf()
