"""
Draw Graphs  For Stories
"""
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities
# aliases
b = entities.book_1
c = entities.cast_1

graph = pgv.AGraph(directed=True, layout="circo", name="Panchatantra Book 1")
graph.add_nodes_from([name for name in c])
for i in b:
    graph.add_edge(b[i].told_by, b[i].title)
    graph.add_edge(b[i].title, b[i].told_to)
    graph.add_edge(b[i].moral, b[i].title)
    if b[i].stories is not None:
        [graph.add_edge(b[i].title, b[j].title) for j in b[i].stories]

graph.layout(prog="circo")  # layout with default (neato)
graph.write("book-1.dot")

#graph.draw("book-1.png")
