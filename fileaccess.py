from objects.generic import NULL

def get_path(s=NULL, ext:str="qm", ignore_ext:int=0) -> str:
    """ Gets a file name/path as an input, an extension and `ignore_ext` and returns the path if its valid (=exists on disk). NULL otherwise.

    ignore_ext represents a flag, that is 1 (True) if the user doesn't care about file extensions (e.g. compile a file.txt and not `ext`)
    
    If the file on disk doesn't end with `ext` then the function will NOT raise an error/quit, but output a warning to sys.stderr.
    """
    from os.path import exists
    from sys import stderr
    wflag = 0 # will be 1 if the file input extension isn't `ext`
    if(s is NULL):
        s = input("Enter a file name:").lower()
    else:
        s = s.lower() 
    if(s[-len(ext):] != f".{ext}"):
        wflag = 1              

    if(exists(s)):
        print(("", f"[Quickmark: Warning] File extension doesn't match regular .{ext} extension. Silence this using -S\n")[(not ignore_ext) and wflag], file=stderr, end="")
        return s
    else: 
        return NULL

def write(path: str, data: str) -> None | NULL:
    """ Writes string to path. Assumes path is valid (and includes file type) """
    try:
        with open(path, "w") as f:
            f.write(data) # this "closes" the function, and therefore a "None will be returned"
    except Exception: # If there's any error
        return NULL       # (this shouldn't really happen)
                          # and will be treated later.