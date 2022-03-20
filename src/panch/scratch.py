# Scratchpad for trying out short code snippets
import entities


# Missing characters in cast:
def cast_missing():
    s = entities.stories
    c = [s[id].told_to for id in s] + [s[id].told_by for id in s]
    unseen = [w for w in c if w not in entities.cast]
    return [i for i in {k: 1 for k in unseen}]


print(cast_missing())
