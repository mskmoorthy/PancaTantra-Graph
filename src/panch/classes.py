"""
Classes For Panchatantra  Graphs
"""


class Story:
    """ A Story consists of Characters, etc."""
    title = ""
    stories = []
    narrator = ""
    moral = ""


class Character:
    """A character in a Story"""
    name = ""
    said = []
    narrated = []
    appears_in = []
