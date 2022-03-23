"""
Draw Graphs  For Book-1
"""
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities
# aliases
b = entities.book_1
c = entities.cast_1

graph = pgv.AGraph(directed=True,
                   name="book-1",
                   size="8,8",
                   label="graphatantra")
[
    graph.add_node(c[i].name, color=c[i].color, style="filled", fontsize="8pt")
    for i in c
]  #Cast
for i in b:  #stories
    graph.add_node(b[i].title, color="SkyBlue", shape="box", fontsize="10pt")
    graph.add_node(b[i].moral,
                   color="DeepSkyBlue",
                   shape="box",
                   fontsize="7pt")
    graph.add_edge(b[i].told_by, b[i].title)
    graph.add_edge(b[i].title, b[i].told_to)
    graph.add_edge(b[i].title, b[i].moral)
    if b[i].stories is not None:
        [graph.add_edge(b[i].title, b[j].title) for j in b[i].stories]
#graph.tred()
graph.unflatten("-f -l1").layout()
graph.write("book-1.dot")
graph.draw("book-1.pdf")
