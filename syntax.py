""" 
Main syntax for Quickmark.
Find more explanation at `docs.md` 
"""

# SET headers (@!)


# Content headers (@$)


# General content

code = r"^`.+`$"                    # Matches `ANY TEXT`
bold = r"^[(*){2}\S].+[.(*){2}]$"   # Matches **ANY TEXT**
italic = r"^[*(?!*)].+[.*]$"        # Matches *ANY TEXT*
                                    # (this is not working!)