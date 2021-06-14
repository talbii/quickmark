from typing import Union
import re 

from ..fileaccess import get_path
from parse.util import arg_to_dict, arg_to_list
from ..syntax import *

def parse_line(line: str) -> str: 
    """ Parses a line into its HTML form. """

    s = line

    if(s == ""): return ""
    
    if(s[0] == "#"):
        h_count = 0
        while(s[0] == "#"): 
            h_count += 1
            s = s[1:]
            if(s == ""): return "" # if we got here, then we got something like "##" (aka an empty heading), which would be ignored
        
        if(s.isspace()): return "" # s is "##      " (...), ignoring that.

        if(h_count > 6): # not actually a header, just a bunch of #'s
            return f'<p class="qm-text">{line[:-1]}</p>' # unmodified line, without the trailing newline

        return f'<h{h_count} class="qm-h{h_count}> {s} </h{h_count}>' 

    if(len(s) <= 2): # this is either text, or a list (with no content)
        pass # handle case

    if(s[0:2] == "```"): # code block
        pass # handle case

    # text_after = re.sub(regex_search_term, regex_replacement, text_before)
    


def parse_special(line: str) -> Union[str, tuple[str]]:
    """ Parses a line into its code (usually compilation arguments or scripts to include) """

    if(line[0:2] == "@:"): # config name
        if(line[-2] == "]"): # syntax option 1
            return line[3:-2] # return the text inside [...], without newline
        else:                 # syntax option 2: @: my_style
            return line[3:-1] 
    elif(line[0:2] == "@!"): # general arguments
        return arg_to_dict(line[2:-1])
    else: # include scripts
        return tuple(arg_to_list(line[2:-1])) # get the list of arguments without @ and \n.