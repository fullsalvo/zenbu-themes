def nohash(s):
    """
    Remove the leading hash from hexadecimal colors.
    """
    return s.strip("#")

def colorn(s):
    """
    Determine color number from its string-form name.
    """
    colorns = {"black": 1,
               "red": 2,
               "green": 3,
               "yellow": 4,
               "blue": 5,
               "magenta": 6,
               "cyan": 7,
               "white": 8}
    return colorns.get(s)
