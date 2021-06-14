""" 
Regex matching for Markdown Expressions
"""

# Text Styling

regexcode = r"^`.+`$"                    # Matches `ANY TEXT`
regexbold = r"^[(*){2}\S].+[.(*){2}]$"   # Matches **ANY TEXT**
regexitalic = r"^[*(?!*)].+[.*]$"        # Matches *ANY TEXT*
