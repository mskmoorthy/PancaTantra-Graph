"""
Draw Graphs  For Book-1
"""
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities

b = entities.book_1
c = entities.cast_1

graph = pgv.AGraph(directed=True, name="book-1", label="graphatantra")
c_props = {"style": "filled", "fontsize": "8pt"}
[graph.add_node(c[i].name, color=c[i].color, **c_props) for i in c]
for i in b:
    ec = c[b[i].told_by].color
    m_props = {"shape": "rectangle", "fontsize": "7pt", "style": "dotted"}
    e_props = {"carrowhead": "halfopen"}
    graph.add_node(b[i].title, shape="box", fontsize="10pt")
    graph.add_node(b[i].moral, color=ec, **m_props)
    graph.add_edge(b[i].told_by, b[i].title, color=ec)
    graph.add_edge(b[i].title, b[i].told_to, color=ec)
    graph.add_edge(b[i].title, b[i].moral, color=ec, **e_props)
    if b[i].stories is not None:
        [graph.add_edge(b[i].title, b[j].title) for j in b[i].stories]

animals = ['rusty', 'lively', 'crafty', 'cautious']
top = [b['34'].title, b['34'].told_by, b['34'].told_to]
graph.add_subgraph(top, rank="same", name="outer")
graph.add_subgraph(animals, rank="same", name="main")
graph.unflatten("-f -l3").layout()
graph.write("book-1.dot")
graph.draw("book-1.pdf")
