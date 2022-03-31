""" Panchatantra Graph """
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities

b = entities.book_1
c = entities.cast_1

graph = pgv.AGraph(directed=True, name="book-1", label="graphatantra")
c_props = {"style": "filled, bold, solid", "fontsize": "8pt"}
m_props = {
    "fontsize": "6pt",
    "style": "dotted, rounded",
    "shape": "rectangle",
    "fontname": "times bold italic"
}
tm_props = {"carrowhead": "filled"}
[graph.add_node(c[i].name, color=c[i].color, **c_props) for i in c]
for i in b:
    ec = c[b[i].told_by].color
    graph.add_node(b[i].title, shape="box", fontsize="10pt", style="filled")
    graph.add_node(b[i].moral, color=ec, **m_props)
    graph.add_edge(b[i].told_by, b[i].title, color=ec)
    graph.add_edge(b[i].title, b[i].told_to, color=ec)
    graph.add_edge(b[i].title, b[i].moral, color=ec, **tm_props)
    if b[i].stories is not None:
        [graph.add_edge(b[i].title, b[j].title) for j in b[i].stories]

animals = ['rusty', 'lively', 'crafty', 'cautious']
top = [b['34'].title, b['34'].told_by, b['34'].told_to]
inner = [
    b[i].stories for i in b
    if b[i].stories is not None and len(b[i].stories) > 1
]

graph.add_subgraph(top, rank="same", name="outer")
graph.add_subgraph(animals, rank="same", name="main")
for i in range(len(inner)):
    graph.add_subgraph(inner[i], name="inner_{}".format(i), rank="same")


def main():
    "DDraw the graph"
    graph.unflatten("-f -l3").layout()
    graph.write("book-1.dot")
    graph.draw("book-1.pdf")


if __name__ == '__main__':
    main()
