# Scratchpad for trying out short code snippets
__author__ = "tv.raman.tv@gmail.com"

import entities


# Missing characters in cast:
def cast_missing():
    s = entities.book_1
    c = [s[id].told_to for id in s] + [s[id].told_by for id in s]
    return {w for w in c if w not in entities.cast_1}


def stories_missing():
    [i for i in entities.book_1['34'].stories if i not in entities.book_1]


print("Missing Cast Members", cast_missing())
print("Missing stories", stories_missing())
