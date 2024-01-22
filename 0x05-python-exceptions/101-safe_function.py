#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as exp:
        sys.stderr.write(f"Exception: {exp}\n")
        return None
