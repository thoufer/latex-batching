import re

LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),    # replace single backslash
    (re.compile(r'([{}_#%&$])'), r'\\\1'),      # add \ for symbols to render actual symbol
    (re.compile(r'"'), r"''"),                  # replace double quotes with double single quote
)

def escape_tex(value):
    """
        given a string apply each LaTeX substitution ensuring
        that the string renders correctly in the final document.
    """
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval

