#!/usr/bin/env bash
# curls a page (in this case a webfiction). If a certain text is found on page, says a message aloud
curl https://archiveofourown.org/works/11478249/chapters/50446721 | grep "Next Chapter" && say "New chapter, yeah"
