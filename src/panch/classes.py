"""Classes For Panchatantra  Graphs"""


class Story:
    """ A Story consists of Characters, etc."""
    id  # unique id (computed)
    title = ""
    stories = []
    narrator = ""
    moral = ""

    def __init__(self,
                 title="",
                 stories=[],
                 narrator="",
                 moral=""):
        "Initialize a Story"
        self.title = title
        self.stories = stories
        self.narrator = narrator
        self.moral = moral


class Character:
    """A character in a Story"""
    id  # Unique id (computed)
    name = ""
    said = []
    narrated = []
    appears_in = []

    def __init__(self,
                 name="",
                 said=[],
                 narrated=[],
                 appears_in=[]):
        "Initialize a Character"
        self.name = name
        self.narrated = narrated
        self.said = said
        self.appears_in = appears_in
