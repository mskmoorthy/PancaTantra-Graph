# Utils: Scratchpad for trying out short code snippets
__author__ = "tv.raman.tv@gmail.com"

import entities
import graph


# Missing characters in cast:
def cast_extra():
    "identify redundant cast members"
    s = entities.book_1
    c = [s[id].told_to for id in s] + [s[id].told_by for id in s]
    all = [s[i].told_by for i in s] + [s[i].told_to for i in s]
    return {i for i in all if i not in c}


def cast_missing():
    s = entities.book_1
    c = [s[id].told_to for id in s] + [s[id].told_by for id in s]
    return {w for w in c if w not in entities.cast_1}


def stories_missing():
    [i for i in entities.book_1['34'].stories if i not in entities.book_1]


def report(g):
    "Show interesting facts from our graph."
    b = entities.book_1
    c = entities.cast_1
    l = g.degree_iter([n for n in c])
    [print(i) for i in l]


if __name__ == '__main__':
    print("Missing Cast Members", cast_missing())
    print("Missing stories", stories_missing())
    print("Extra Cast Members", cast_extra())
