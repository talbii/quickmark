# NOTE: This was written quickly as a Proof-Of-Concept
#     : This is not the final project!
#     : As I develop this project, soon this file will be removed.
#     : to run: place script in the same directory as your Quickmark file, and run using python3 qm-test.py
fname = input("[Quickmark:Prompt] Enter input file name: ")
oname = input("[Quickmark:Prompt] Output file name same as input (y/n): ")

if(fname[-3:] != ".qm"): fname += ".qm"

if(oname.upper() == "Y"):
    out = fname[:-3]
elif(oname.upper() == "N"):
    out = input("[Quickmark:Prompt] Enter output file name: ")
else:
    print("[Quickmark: Error] Invalid input.")
    raise SystemExit

f = open(fname, "r")

d = {
    "font": {
        "text": ".text{{font-family: {};}}",
        "heading": ".head{{font-family: {};}}",
        "code": ".code{{font-family: {};}}",
    },
    "text": {
        "size": ".text{{font-size: {}px;}}",
        "color": ".text{{color: {};}}",
        "colour": ".text{{color: {};}}",
        "align": ".text{{text-align: {};}}",
        "inline": ".text{{display: inline-block}}",
    },
    "code": {
        "size": ".code{{font-size: {}px;}}",
        "color": ".code{{color: {};}}",
        "colour": ".code{{color: {};}}",
        "align": ".code{{text-align: {};}}",
        "inline": ".code{{display: inline-block}}",
    },
    "heading": {
        "size": ".heading{{font-size: {}px;}}",
        "color": ".heading{{color: {};}}",
        "colour": ".heading{{color: {};}}",
        "align": ".heading{{text-align: {};}}"
    },
    "title": {"<title> {} </title"},
}

def setargs(line: str) -> str:
    """ Gets a line from a non-compiled file and returns code to insert into an HTML document. """
    if(line[2:7] == "title"):
        return f"<title> {line[9:]} </title>"

    i = 2
    m, s = "", ""

    while(i < line.__len__() and line[i:i+2] != "->"):
        m += line[i]
        i += 1
    i += 2

    while(i < line.__len__() and line[i] != "("):
        s += line[i]
        i += 1
    
    if(s[-1] == "\n"):
        s = s[:-1]
 
    return d[m][s].format(line[i+1:-2])

t = {
    "h": "<h1 class='heading'>{}</h1>"
}

def formatcode(text: str):
    """ Formats code (`foo()`) """
    i = 1
    s = ""
    for ch in text:
        if(ch == "`"):
            if(i == 1):
                s += "<span class='code'>"
                i = 2
            else:
                s += "</span>"
                i = 1
        elif(ch != "\n"):
            s += ch
    return s
            

def settext(line: str):
    """ Formats regular text (paragraphs) """
    return t[line[2]].format(line[3:-1])

headstyle = setargs("@!code->inline")
headmisc = ""
body = ""
lastarg = True
for line in f:
    if(line[0:2] == "@!"):
        headstyle += setargs(line)
    elif(line[0:2] == "@#"):
        headmisc += setargs(line)
    elif(line[0:2] == "@$"):
        body += settext(line)
    else:
        if(line == "\n"):
            if(lastarg):
                lastarg = False
            else:
                body += "<br>"
        else:
            body += f"<span class='text'>{formatcode(line)}</span>"


x = f'''
<!DOCTYPE html>
<html lang="en">
<head>
{headmisc}
<style>
{headstyle}
</style>
</head>
<body>
{body}
</body>
</html>
'''

k = open(f"{out}.html", "w")
k.write(x)
k.close()

print(f"[Quickmark] Successful - output: {out}.html")
