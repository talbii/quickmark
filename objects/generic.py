class __NULL__:
    """ NULL class type. Used instead of None """
    pass

'''
Note: throughout this project I use NULL instead of None,
the reason for this is to prevent accidental returns of None mistakenly
returned by me. For example, if some function fails and doesn't return
anything (so, None), I might mistake it to a None that I've returned,
which signals something else. This is why I use NULL:
So, if I return NULL I know that I've returned it. 

This is an excuse.
'''
NULL = __NULL__() # This is a NULL. Use this instead of None/__NULL__()