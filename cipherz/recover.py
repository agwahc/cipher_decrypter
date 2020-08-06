def recover(source):  # To try to recover elements in list structure from *source*.txt
    try:
        g = open(source, 'r')
        for i in g:
            n = str.casefold(i)
            x = n.split()
        return x
    except:
        print("No current {} file present!".format(source))
