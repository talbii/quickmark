from __future__ import annotations  # Used for type-hinting.

class Paragraph:
    ''' This class/object represents a singular paragraph in an HTML file,
    e.g. text between <p> </p> tags. This class is to be used instead of a string,
    as it features more functions and readability.
    '''

    def __init__(self):
        """ Constructs an empty paragraph """
        self.texts = ""
        
    def release(self) -> str:
        """ Empties the current paragraph and returns it as a HTML paragraph - string """
        temp = self.texts
        self.texts = ""
        return f'<p class="text">{temp}</p>\n'
    
    def add(self, text):
        """ Adds `text` to current paragraph. `text` is formatted!! """
        self.texts += (text+"\n")
    
class Content:
    ''' Holds all of the body content. '''
    def __init__(self):
        self.body_content = ""
    
    def add(self, pr: Paragraph):
        """ Gets a paragraph and adds it (empties it) to current content. """
        self.body_content += pr.release()
    
    def release(self) -> str:
        """ Empties all of the content, with `<body>` tags. Use this once!! """
        temp = self.body_content
        self.body_content = ""
        return f'<body>{temp}</body>\n'

class Style:
    ''' Holds a style for a singular tag (p, div, span, etc.).
    
    Also saves a list of all the existing styles. '''

    instances = []

    def __init__(self, tag, class_name):
        ''' Initializes a new Style. 
        
        Required: tag (e.g. p, div, span), and class name (e.g. <p class="...">) '''
        if(Style.exists(tag, class_name)):
            raise DuplicateStyle(f"{tag}, class={class_name}  Already exists.")
        self.tag = tag
        self.class_name = class_name
        self.css = ""
        Style.instances.append(self)

    def add_property(self, name, value) -> None:
        """ Adds the property `name` with `value` to current object's CSS style """
        self.css += f"{name}: {value},\n"

    def __eq__(self, other: Style) -> bool:
        """ Equals method. Used only for `exists` to make things a little shorter. """
        return self.tag == other.tag and \
        self.class_name == other.class_name

    def exists(self, tag, class_name) -> bool:
        """ Returns `True` if this style (tag, class_name) already exists. """
        s: Style # type-hinting
        for s in self.instances:
            if(self == s):
                return True
        return False

class DuplicateStyle(Exception):
    """ This is used mainly for debugging. 
    
    Raised if trying to create multiple `Style`s with the same identifiers. """
