# Utils: Scratchpad for trying out short code snippets
__author__ = "tv.raman.tv@gmail.com"

import entities
import graph


def cast_extra():
    "identify redundant cast members"
   # s1 = entities.book_1
    s2 = entities.book_2
    c2 = [s2[id].told_to for id in s2] + [s2[id].told_by for id in s2]
    all = [s2[i].told_by for i in s2] + [s2[i].told_to for i in s2]
    return {i for i in all if i not in c2}


def cast_missing():
    #s1 = entities.book_1
    s2 = entities.book_2
    
    c2 = [s2[id].told_to for id in s2] + [s2[id].told_by for id in s2]
    return {w for w in c2 if w not in entities.cast_2}


def stories_missing():
    [i for i in entities.book_2['0'].stories if i not in entities.book_2]


def report(g):
    "Show interesting facts from our graph."
    b2 = entities.book_2
    c2 = entities.cast_2
    print("Cast: Degrees")
    c_iter = g.degree_iter([n for n in c2])
    [print(i) for i in c_iter]
    b_iter = g.degree_iter([b2[n].title for n in b2])
    print("Book: Degrees")
    [print(i) for i in b_iter]


def moral_len():
    "Show length of morals."
    print("Moral Lengths")
    m = [entities.book_2[i].moral for i in entities.book_2]
    [print(len(i), ": ", i) for i in sorted(m, key=len)]


def title_len():
    "Show length of titles."
    print("Title Lengths")
    m = [entities.book_2[i].title for i in entities.book_2]
    [print(len(i), ": ", i) for i in sorted(m, key=len)]


if __name__ == '__main__':
    print("Missing Cast Members", cast_missing())
    print("Missing stories", stories_missing())
    print("Extra Cast Members", cast_extra())
    moral_len()
    title_len()
