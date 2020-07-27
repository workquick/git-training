def main_program(arg):
    if arg == 'division':
        # In Py2, 3/2 returns 1
        return 3 / 2  # change to //
    elif arg == 'range_type':
        # In Py2, range() returns list
        return range(5)  # change to list(range(5))
    elif arg == 'raise_error':
        # In py3, raise IOError('file error')
        raise IOError, 'file error'
