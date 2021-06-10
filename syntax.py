""" 
Regex matching for Markdown Expressions
"""

# Text Styling

code = r"^`.+`$"                    # Matches `ANY TEXT`
bold = r"^[(*){2}\S].+[.(*){2}]$"   # Matches **ANY TEXT**
italic = r"^[*(?!*)].+[.*]$"        # Matches *ANY TEXT*
                                    # (this is not working!)