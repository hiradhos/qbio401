def compbase(base):
    '''Returns complement of one element'''
    if base == "A":
        compbase = "T"
    elif base == "C":
        compbase = "G"
    elif base == "G":
        compbase = "C"
    elif base == "T":
        compbase = "A"
    else:
        compbase = base 
        # if there's an N in the sequence for example, leave it alone
    return compbase

def compseq(seq):
    '''Returns complement of entire string'''
    complst = list(seq)
    for i in range(len(complst)):
        temp = compbase(complst[i])
        complst[i] = temp
    return "".join(complst)

def rev(seq):
    '''Returns the reverse of a string'''
    return seq[::-1]

def revcomp(seq):
    '''Returns the reverse complement of seq'''
    rv = rev(seq)
    rvcp = compseq(rv)
    return rvcp
