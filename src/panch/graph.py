"""
Draw Graphs  For Stories
"""
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities
# aliases
b = entities.book_1
c = entities.cast_1

g = pgv.AGraph(directed=True, layout="circo", name="Panchatantra Book 1")
g.add_nodes_from([name for name in c])
for i in b:
    g.add_edge(b[i].told_by, b[i].title)
    g.add_edge(b[i].title, b[i].told_to)
    g.add_edge(b[i].moral, b[i].title)
    if b[i].stories is not None:
        [g.add_edge(b[i].title, b[j].title) for j in b[i].stories]

g.layout(prog="circo")  # layout with default (neato)
g.write("book-1.dot")

#g.draw("book-1.png")
