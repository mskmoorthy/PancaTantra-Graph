# Scratchpad for trying out short code snippets
__author__ = "tv.raman.tv@gmail.com"

import entities


# Missing characters in cast:
def cast_missing():
    s = entities.stories
    c = [s[id].told_to for id in s] + [s[id].told_by for id in s]
    return {w for w in c if w not in entities.cast}


def stories_missing():
    [i for i in entities.stories['34'].stories if i not in entities.stories]


print("Missing Cast Members", cast_missing())
print("Missing stories", stories_missing())
