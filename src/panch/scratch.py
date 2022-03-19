# Scratchpad for trying out short code snippets
import importlib
import entities


# Missing characters in cast:
def cast_missing():
    c = [entities.stories[id].told_to for id in entities.stories
         ] + [entities.stories[id].told_by for id in entities.stories]
    new = [w for w in c if w not in entities.cast]
    return [i for i in {k: 1 for k in new}]


print(cast_missing())
