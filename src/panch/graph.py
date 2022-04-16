""" Panchatantra Graph """
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities

b = entities.book_1
c = entities.cast_1

c_props = {"style": "filled, bold", "fontsize": "6pt"}  #cast
t_props = {"shape": "box", "fontsize": "6pt", "style": "filled"}  #book
i_props = {  #inner subgraph
    "style": "dashed,radial",
    "rank": "same",
    "bgcolor": "CornflowerBlue:PaleGoldenrod"
}
m_props = {  #moral
    "fontsize": "6pt",
    "style": "striped",
    "shape": "rectangle",
    "fontname": "helvetica italic"
}
tm_props = {"carrowhead": "filled"}  #title->moral
g_props = {"label": "Graphatantra", "fontname": "helvetica"}  #graph


def graph_a():
    "Version A. Morals are nodes."
    graph = pgv.AGraph(directed=True, name="book-1a", **g_props)
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
                graph.add_edge(b[i].title, b[j].title, style="dotted")
                for j in b[i].stories
            ]

    inner = [
        b[i].stories for i in b
        if i != '0' and b[i].stories is not None and len(b[i].stories) > 1
    ]

    animals = ['rusty', 'lively', 'crafty', 'cautious']
    top = [b['0'].title, b['0'].told_by, b['0'].told_to, b['0'].moral]
    crafty = [b[i].title for i in b if b[i].told_by == 'crafty']
    cautious = [b[i].title for i in b if b[i].told_by == 'cautious']
    lively = [b[i].title for i in b if b[i].told_by == 'lively']

    # Rank explained:
    # https://www.worthe-it.co.za/blog/2017-09-19-quick-introduction-to-graphviz.html#:~:text=Ranks%20and%20Subgraphs,placed%20further%20to%20the%20right.
    graph.add_subgraph(top,
                       rank="same",
                       name="cluster_outer",
                       bgcolor="LightGray:PaleTurquoise")
    graph.add_subgraph(animals,
                       label="Cast",
                       rank="source",
                       name="cluster_cast",
                       bgcolor="LightBlue:LightGray")
    for i in range(len(inner)):
        subtitles = [b[j].title for j in inner[i]]
        graph.add_subgraph(subtitles, name="cluster_{}".format(i), **i_props)
    #graph.add_subgraph(crafty, name="cluster_crafty")
    #graph.add_subgraph(cautious, name="cluster_cautious")
    #graph.add_subgraph(lively, name="cluster_lively")

    graph.unflatten("-f -l3").layout()
    graph.write("book-1a.dot")


def graph_b():
    "Version B. Morals are edges."
    graph = pgv.AGraph(directed=True, name="book-1b", **g_props)

    [graph.add_node(c[i].name, color=c[i].color, **c_props) for i in c]
    for i in sorted(b, key=int):
        ec = c[b[i].told_by].color
        s_label = "{}: {}".format(i, b[i].title)
        graph.add_node(b[i].title, label=s_label, color=ec, **t_props)
        graph.add_edge(b[i].told_by, b[i].title, color=ec, label=b[i].moral)
        graph.add_edge(b[i].title, b[i].told_to, color=ec)
        if b[i].stories is not None:
            [
                graph.add_edge(b[i].title, b[j].title, style="dotted")
                for j in b[i].stories
            ]

    inner = [b[i].stories for i in b if i != '0' and b[i].stories is not None]
    animals = ['rusty', 'lively', 'crafty', 'cautious']
    top = [b['0'].title, b['0'].told_by, b['0'].told_to]
    # Rank explained:
    # https://www.worthe-it.co.za/blog/2017-09-19-quick-introduction-to-graphviz.html#:~:text=Ranks%20and%20Subgraphs,placed%20further%20to%20the%20right.
    graph.add_subgraph(top,
                       rank="same",
                       name="cluster_outer",
                       bgcolor="LightGray:PaleTurquoise")
    graph.add_subgraph(animals, rank="source", name="cluster_cast")
    for i in range(len(inner)):
        subtitles = [b[j].title for j in inner[i]]
        graph.add_subgraph(subtitles, name="cluster_{}".format(i), **i_props)
    graph.unflatten("-f -l3").layout()
    graph.write("book-1b.dot")


def main():
    "DDraw the graphs"
    graph_a()
    #graph_b()


if __name__ == '__main__':
    main()
