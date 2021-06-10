def arg_to_list(s: str) -> list[str]:
    """ Gets a line and returns a list containing such items, formatted.
    
    ## Tests ##
    >>> arg_to_list("mathjax, jquery, bootstrap")
    ('mathjax', 'jquery', 'bootstrap')

    >>> arg_to_list("script1, script2, script3, script4,")
    ['script1', 'script2', 'script3', 'script4']
    
    """
    l = []
    for item in s.split(","):
        if(item.strip() != ""): l.append(item.strip())

    return l

def arg_to_dict(s: str) -> dict:
    """ Gets a string and makes a dictionary from it, where every (key, value) is a
    corresponding pair in a string: 'a b' -> (a, b)
    
    ## Tests ##
    >>> arg_to_dict("[title My Document][arg1][arg2 5]")
    {'title': 'My Document', 
     'arg1': None, 'arg2': '5'}
    
    >>> arg_to_dict("[opt1 value1][opt2 value2][opt3][opt4][opt5][opt6 value6]")
    {'opt1': 'value1', 'opt2': 'value2', 
    'opt3': None, 'opt4': None, 'opt5': None, 'opt6': 'value6'}
    """
    
    d = dict()
    l = s.split("[")
    l1 = []

    for item in l:
        if(item != ""): l1.append(item.split("]")[0])

    del l # remove l, we don't need it anymore.

    for item in l1:
        t = get_first_item(item)
        if(item[len(t)+1:] == ""):
            d[t] = None
        else:
            d[t] = item[len(t)+1:]
    
    return d

def get_first_item(s: str) -> str:
    """ Gets first word in s """
    s1 = ""
    for c in s:
        if(c == " "): return s1
        s1 += c
    return s # if we didn't return s1, then s is a single word.
