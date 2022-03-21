"""
Draw Graphs  For Stories
"""
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities

b = entities.book_1
c = entities.cast_1

g = pgv.AGraph()
g.add_nodes_from([name for name in c])
g.add_nodes_from([b[i].title for i in b])
g.add_nodes_from([b[i].moral for i in b])

for i in b:
    g.add_edge(b[i].told_by, b[i].title)
    g.add_edge(b[i].title, b[i].told_to)
    g.add_edge(b[i].moral, b[i].title)
g.layout(prog="circo")  # layout with default (neato)
g.write("book-1.dot")

#g.draw("book-1.png")
