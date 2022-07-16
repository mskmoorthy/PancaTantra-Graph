# Utils: Scratchpad for trying out short code snippets
__author__ = "tv.raman.tv@gmail.com"

import entities


def cast_extra(b, c):
    "identify redundant cast members"
    all = [b[i].told_by for i in b] + [b[i].told_to for i in b]
    return {i for i in all if i not in c}


def cast_missing(b, c):
    who = [b[id].told_to for id in b] + [b[id].told_by for id in b]
    return {w for w in who if w not in c}


def stories_missing(b):
    [i for i in b['0'].stories if i not in b]


def moral_len(name, b):
    "Show length of morals."
    print("Moral Lengths In {}".format(name))
    m = [b[i].moral for i in b]
    [print(len(i), ": ", i) for i in sorted(m, key=len)]


def title_len(name, b):
    "Show length of titles."
    print("Title Lengths In {}".format(name))
    m = [b[i].title for i in b]
    [print(len(i), ": ", i) for i in sorted(m, key=len)]


def show_primary(c):
    "Show primary characters."
    return [i for i in c if c[i].primary is not None]


if __name__ == '__main__':
    print("Cast 1:", show_primary(entities.cast_1))
    print("Cast 2:", show_primary(entities.cast_2))
    print("Cast 3:", show_primary(entities.cast_3))
    print("Cast 4:", show_primary(entities.cast_4))
    print("book-1 Missing Cast Members",
          cast_missing(entities.book_1, entities.cast_1))
    print("book-2 Missing Cast Members",
          cast_missing(entities.book_2, entities.cast_2))
    print("book-3 Missing Cast Members",
          cast_missing(entities.book_3, entities.cast_3))
    print("book-4 Missing Cast Members",
          cast_missing(entities.book_4, entities.cast_4))

    print("book-1: Missing stories", stories_missing(entities.book_1))
    print("book-2: Missing stories", stories_missing(entities.book_2))
    print("book-3: Missing stories", stories_missing(entities.book_3))
    print("book-4: Missing stories", stories_missing(entities.book_4))
    print("Book-1: Extra Cast Members",
          cast_extra(entities.book_1, entities.cast_1))
    print("Book-2: Extra Cast Members",
          cast_extra(entities.book_2, entities.cast_2))
    print("Book-3: Extra Cast Members",
          cast_extra(entities.book_3, entities.cast_3))
    print("Book-4: Extra Cast Members",
          cast_extra(entities.book_3, entities.cast_4))
    moral_len("book-1", entities.book_1)
    title_len('book-1', entities.book_1)
    moral_len("book-2", entities.book_2)
    title_len('book-2', entities.book_2)
    moral_len("book-3", entities.book_3)
    title_len('book-3', entities.book_3)
    moral_len("book-4", entities.book_4)
    title_len('book-4', entities.book_4)
