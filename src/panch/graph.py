""" Panchatantra Graph """
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities

b = entities.book_1
c = entities.cast_1

graph = pgv.AGraph(directed=True,
                   name="book-1",
                   label="graphatantra",
                   fontname="helvetica")
c_props = {"style": "filled, bold", "fontsize": "6pt"}
t_props = {"shape": "box", "fontsize": "6pt", "style": "filled"}
m_props = {
    "fontsize": "6pt",
    "style": "dotted",
    "shape": "rectangle",
    "fontname": "helvetica italic"
}
tm_props = {"carrowhead": "filled"}
[graph.add_node(c[i].name, color=c[i].color, **c_props) for i in c]
for i in sorted(b, key=int):
    ec = c[b[i].told_by].color
    s_label = "{}: {}".format(i, b[i].title)
    graph.add_node(b[i].title, label=s_label, color=ec, **t_props)
    graph.add_node(b[i].moral, color=ec, **m_props)
    graph.add_edge(b[i].told_by, b[i].title, color=ec)
    graph.add_edge(b[i].title, b[i].told_to, color=ec)
    graph.add_edge(b[i].title, b[i].moral, color=ec, **tm_props)
    if b[i].stories is not None:
        [
            graph.add_edge(b[i].title,
                           b[j].title,
                           color="black",
                           style="dotted") for j in b[i].stories
        ]

animals = ['rusty', 'lively', 'crafty', 'cautious']
top = [b['0'].title, b['0'].told_by, b['0'].told_to, b['0'].moral]
# Rank explained:
# https://www.worthe-it.co.za/blog/2017-09-19-quick-introduction-to-graphviz.html#:~:text=Ranks%20and%20Subgraphs,placed%20further%20to%20the%20right.
graph.add_subgraph(top, rank="same", name="outer")
graph.add_subgraph(animals, rank="source", name="main")


def main():
    "DDraw the graph"
    graph.unflatten("-f -l3").layout()
    graph.write("book-1.dot")


if __name__ == '__main__':
    main()
