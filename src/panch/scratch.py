# Scratchpad for trying out short code snippets

from entities import cast, stories


# Missing characters in cast:
def cast_missing():
    c = [stories[id].told_to
         for id in stories] + [stories[id].told_by for id in stories]
    new = [w for w in c if w not in cast]
    return [i for i in {k: 1 for k in new}]


print(cast_missing())
