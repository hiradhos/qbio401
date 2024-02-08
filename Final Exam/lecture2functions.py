

# IMPORTANT FUNCTION FOR YOUR FIRST HW ASSIGNMENT
# NOTE: THE FIRST TWO FUNCTIONS ASSUME ONLY ONE SEQUENCE IN THE FILE
# SOMETIMES FASTA FILES HAVE MULTIPLE SEQUENCES SEPARATED BY >
# THE THIRD FUNCTION HANDLES THAT CASE

def loadFASTA(filename):
    '''Outputs a sequence string from the FASTA file named filename'''
    infile = open(filename) # opens the file
    seqlist = [] # empty list
    temp = infile.readline() # reads a single line
                             # we don't want the first line 
                             # of the FASTA file ">..."
    for line in infile: # reads one line at a time
                        # when it gets to the end of the file it stops
        temp = line.replace("\n","") # removes \n
        temp = temp.replace("\r","") # removes \r too
        seqlist.append(temp)
    infile.close() # closes the file
    seq = "".join(seqlist) # combines the list into a string
    return seq

# Note: we appended to a list, and then made a sequence at the end.
# If we would have appended to a string, for each line
# we would have inefficiently created a different string each time.

# There are many different ways to do the same thing in Python.
# The advantage of using "with" below is that you don't have to remember
# to close the file when you are done with it.

def loadFASTA2(filename):
    '''Outputs a sequence string from the FASTA file named filename'''
    seqlist = []
    with open(filename,"r") as infile:
      temp = infile.readline() # reads a single line
                               # we don't want the first line 
                               # of the FASTA file ">..."
      for line in infile: # reads one line at a time
                          # when it gets to the end of the file it stops
        temp = line.replace("\n","") # removes \n
        temp = temp.replace("\r","") # removes \r too
        seqlist.append(temp)
    seq = "".join(seqlist) # combines the list into a string
    return seq

# THE THIRD FUNCTION BELOW HANDLES FILES IN THE MULTIFASTA FORMAT
# FOR EXAMPLE, FOR THE EXAMPLE BELOW (ALL IN ONE FILE) IT WOULD RETURN
# A LIST OF 3 STRINGS (THE FUNCTION HAS TO DETERMINE HOW MANY STRINGS
# THERE ARE)

# > gene 1
#ACCGTAAAAC
#GGCAATGCGA
#> gene 2
#ACCGTTAAAT
#CCGGATATAT
#> gene 3
#AAATTTGCGC
#CGATTAGCAA

def loadMULTIFASTA(filename):
    '''Outputs a list of strings from the MULTIFASTA file named filename'''
    bigseqlist = [] # empty list
    seqlist = [] # empty list
    with open(filename,"r") as infile:
        for line in infile:
            if line[0] == ">": # new sequence
                if len(seqlist) > 0: # something to add, not first >
                    seq = "".join(seqlist) # make into string
                    bigseqlist.append(seq) # add string to list of strings
                    seqlist = [] # re-start with empty list for next sequence
            else:
                temp = line.replace("\n","")
                temp = temp.replace("\r","")
                seqlist.append(temp)
        # have to include the last sequence
        seq = "".join(seqlist) # make into string
        bigseqlist.append(seq) # add string to list of strings
    return bigseqlist
      
      

