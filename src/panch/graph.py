""" Panchatantra Graph """
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities
#  Rank explained:
#  https://www.worthe-it.co.za/blog/2017-09-19-quick-introduction-to-graphviz.html=

b = entities.book_1
c = entities.cast_1

c_props = {"shape": "box", "style": "filled, bold", "fontsize": "6pt"}  # cast
t_props = {"shape": "box", "fontsize": "6pt", "style": "dotted"}  # book
i_props = {  # inner subgraph
    "style": "dashed,radial",
    "rank": "same",
    "bgcolor": "CornflowerBlue:PaleGoldenrod"
}
m_props = {  # moral
    "shape": "box",
    "fontsize": "6pt",
    "style": "striped",
    "fontname": "helvetica italic"
}
tm_props = {"carrowhead": "filled"}  # title->moral
g_props = {
    "fixedsize": "shape",
    "overlap": "prism",
    "label": "Graphatantra",
    "fontname": "helvetica",
    "packmode": "clust",
    "outputMode": "nodesfirst",
    "outputorder": "nodesfirst",
}  # graph


def graph_a():
    "Version A. Morals are nodes."
    gName = 'book-1a'
    graph = pgv.AGraph(directed=True, name=gName, **g_props)
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

    inner = [b[i].stories for i in b if i != '0' and b[i].stories is not None]
    animals = ['rusty', 'lively', 'crafty', 'cautious']
    top = [b['0'].title, b['0'].told_by, b['0'].told_to, b['0'].moral]

    graph.add_subgraph(top,
                       rank="same",
                       name="cluster_outer",
                       label=gName,
                       bgcolor="LightGray:PaleTurquoise")
    graph.add_subgraph(animals,
                       label="Cast",
                       rank="source",
                       name="cluster_cast",
                       bgcolor="LightBlue:LightGray")
    for i in range(len(inner)):
        subtitles = [b[j].title for j in inner[i]]
        inner_by_to = [b[j].told_by for j in inner[i]]
        inner_by_to += [b[j].told_to for j in inner[i]]
        graph.add_subgraph(subtitles + inner_by_to,
                           name="cluster_{}".format(i),
                           label="Frame {}".format(i),
                           **i_props)
    graph.unflatten("-f -l3").layout()
    graph.write("{}.dot".format(gName))


def graph_b():
    "Version B: told_to is an edge label."
    gName = 'book-1b'
    graph = pgv.AGraph(directed=True, name=gName, **g_props)
    for i in sorted(b, key=int):
        ec = c[b[i].told_by].color
        s_label = "{}: {}".format(i, b[i].title)
        graph.add_node(b[i].title, label=s_label, color=ec, **t_props)
        graph.add_node(b[i].moral, color=ec, **m_props)
        graph.add_edge(b[i].told_by, b[i].title, color=ec, label=b[i].told_to)
        graph.add_edge(b[i].title, b[i].moral, color=ec, **tm_props)
        if b[i].stories is not None:
            [
                graph.add_edge(b[i].title, b[j].title, style="dotted")
                for j in b[i].stories
            ]

    inner = [b[i].stories for i in b if i != '0' and b[i].stories is not None]
    animals = ['rusty', 'lively', 'crafty', 'cautious']
    top = [b['0'].title, b['0'].told_by, b['0'].moral]

    graph.add_subgraph(top,
                       rank="same",
                       name="cluster_outer",
                       label=gName,
                       bgcolor="LightGray:PaleTurquoise")
    graph.add_subgraph(animals,
                       label="Cast",
                       rank="source",
                       name="cluster_cast",
                       bgcolor="LightBlue:LightGray")
    for i in range(len(inner)):
        subtitles = [b[j].title for j in inner[i]]
        inner_by = [b[j].told_by for j in inner[i]]
        graph.add_subgraph(subtitles + inner_by,
                           name="cluster_{}".format(i),
                           label="Frame {}".format(i),
                           **i_props)
    graph.unflatten("-f -l3").layout()
    graph.write("{}.dot".format(gName))


def main():
    "Output Graphs"
    import os
    prog = ['dot', 'twopi']
    fmt = ['pdf', 'plain']
    opt = ['a', 'b']
    cmd = '{} book-1{}.dot | gvcolor | {} -T{} -o  {}-1{}.{}'
    graph_a()
    graph_b()
    [[[os.system(cmd.format(p, o, p, f, p, o, f)) for o in opt] for p in prog]
     for f in fmt]


if __name__ == '__main__':
    main()
