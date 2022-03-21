"""
Draw Graphs  For Stories
"""
__author__ = "tv.raman.tv@gmail.com"

import pygraphviz as pgv
import entities

A = pgv.AGraph()

A.add_edge(1, 2)
A.add_edge(2, 3)
A.add_edge(1, 3)

print(A.string())  # print to screen
A.write("simple.dot")  # write to simple.dot

B = pgv.AGraph("simple.dot")  # create a new graph from file
B.layout()  # layout with default (neato)
B.draw("simple.png")  # draw png
