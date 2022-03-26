"""
Draw Graphs  For Book-1
"""
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities
# aliases
b = entities.book_1
c = entities.cast_1

graph = pgv.AGraph(directed=True, name="book-1", label="graphatantra")
[
    graph.add_node(c[i].name, color=c[i].color, style="filled", fontsize="8pt")
    for i in c
]  #cast_1
for i in b:
    graph.add_node(b[i].title, shape="box", fontsize="10pt")
    graph.add_node(b[i].moral, shape="rectangle", fontsize="7pt")
    ec = c[b[i].told_by].color
    graph.add_edge(b[i].told_by, b[i].title, color=ec)
    graph.add_edge(b[i].title, b[i].told_to, color=ec)
    graph.add_edge(b[i].title, b[i].moral, arrowhead="halfopen")
    if b[i].stories is not None:
        [
            graph.add_edge(b[i].title, b[j].title, arrowshape="diamond")
            for j in b[i].stories
        ]  # contained stories

animals = ['rusty', 'lively', 'crafty', 'cautious']
# Rank explained: https://www.worthe-it.co.za/blog/2017-09-19-quick-introduction-to-graphviz.html#:~:text=Ranks%20and%20Subgraphs,placed%20further%20to%20the%20right.
graph.add_subgraph(animals, rank="same", name="main")
top = [b['34'].title, b['34'].told_by, b['34'].told_to]
graph.add_subgraph(top, rank="same", name="outer")
graph.unflatten("-f -l3 -c 5").layout()
graph.write("book-1.dot")
graph.draw("book-1.pdf")
