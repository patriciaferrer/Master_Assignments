#NAME: Patricia Ferrer Torres

#This is the code I used to get a dictionary from a blosum matrix in a text file (attatched to the email)
# inputblosum = open("blosumfile.txt", "rt")
# list=[]
# matrix = []
# n = 0
# blosum62 = {}
# for line in inputblosum:
#     temp = line.strip().split(" ")
#     for element in temp:
#         if element != "":
#             list.append(element)
#     matrix.append(list)
#     temp, list = [], []
#
# for x in range(len(matrix[0])-1):
#     for y in range(1,len(matrix)-1):
#         z = matrix[y][0], matrix[0][x]
#         if z not in blosum62:
#             blosum62[matrix[0][x], matrix[y][0]] = int(matrix[y][x+1])

#Dictionary for the blosum62 matrix
blosum62 = {('A', 'A'): 4, ('A', 'R'): -1, ('A', 'N'): -2, ('A', 'D'): -2, ('A', 'C'): 0, ('A', 'Q'): -1, ('A', 'E'): -1,
            ('A', 'G'): 0, ('A', 'H'): -2, ('A', 'I'): -1, ('A', 'L'): -1, ('A', 'K'): -1, ('A', 'M'): -1, ('A', 'F'): -2,
            ('A', 'P'): -1, ('A', 'S'): 1, ('A', 'T'): 0, ('A', 'W'): -3, ('A', 'Y'): -2, ('A', 'V'): 0, ('A', 'B'): -2,
            ('A', 'Z'): -1, ('A', 'X'): 0, ('R', 'R'): 5, ('R', 'N'): 0, ('R', 'D'): -2, ('R', 'C'): -3, ('R', 'Q'): 1,
            ('R', 'E'): 0, ('R', 'G'): -2, ('R', 'H'): 0, ('R', 'I'): -3, ('R', 'L'): -2, ('R', 'K'): 2, ('R', 'M'): -1,
            ('R', 'F'): -3, ('R', 'P'): -2, ('R', 'S'): -1, ('R', 'T'): -1, ('R', 'W'): -3, ('R', 'Y'): -2, ('R', 'V'): -3,
            ('R', 'B'): -1, ('R', 'Z'): 0, ('R', 'X'): -1, ('N', 'N'): 6, ('N', 'D'): 1, ('N', 'C'): -3, ('N', 'Q'): 0,
            ('N', 'E'): 0, ('N', 'G'): 0, ('N', 'H'): 1, ('N', 'I'): -3, ('N', 'L'): -3, ('N', 'K'): 0, ('N', 'M'): -2,
            ('N', 'F'): -3, ('N', 'P'): -2, ('N', 'S'): 1, ('N', 'T'): 0, ('N', 'W'): -4, ('N', 'Y'): -2, ('N', 'V'): -3,
            ('N', 'B'): 3, ('N', 'Z'): 0, ('N', 'X'): -1, ('D', 'D'): 6, ('D', 'C'): -3, ('D', 'Q'): 0, ('D', 'E'): 2,
            ('D', 'G'): -1, ('D', 'H'): -1, ('D', 'I'): -3, ('D', 'L'): -4, ('D', 'K'): -1, ('D', 'M'): -3, ('D', 'F'): -3,
            ('D', 'P'): -1, ('D', 'S'): 0, ('D', 'T'): -1, ('D', 'W'): -4, ('D', 'Y'): -3, ('D', 'V'): -3, ('D', 'B'): 4,
            ('D', 'Z'): 1, ('D', 'X'): -1, ('C', 'C'): 9, ('C', 'Q'): -3, ('C', 'E'): -4, ('C', 'G'): -3, ('C', 'H'): -3,
            ('C', 'I'): -1, ('C', 'L'): -1, ('C', 'K'): -3, ('C', 'M'): -1, ('C', 'F'): -2, ('C', 'P'): -3, ('C', 'S'): -1,
            ('C', 'T'): -1, ('C', 'W'): -2, ('C', 'Y'): -2, ('C', 'V'): -1, ('C', 'B'): -3, ('C', 'Z'): -3, ('C', 'X'): -2,
            ('Q', 'Q'): 5, ('Q', 'E'): 2, ('Q', 'G'): -2, ('Q', 'H'): 0, ('Q', 'I'): -3, ('Q', 'L'): -2, ('Q', 'K'): 1,
            ('Q', 'M'): 0, ('Q', 'F'): -3, ('Q', 'P'): -1, ('Q', 'S'): 0, ('Q', 'T'): -1, ('Q', 'W'): -2, ('Q', 'Y'): -1,
            ('Q', 'V'): -2, ('Q', 'B'): 0, ('Q', 'Z'): 3, ('Q', 'X'): -1, ('E', 'E'): 5, ('E', 'G'): -2, ('E', 'H'): 0,
            ('E', 'I'): -3, ('E', 'L'): -3, ('E', 'K'): 1, ('E', 'M'): -2, ('E', 'F'): -3, ('E', 'P'): -1, ('E', 'S'): 0,
            ('E', 'T'): -1, ('E', 'W'): -3, ('E', 'Y'): -2, ('E', 'V'): -2, ('E', 'B'): 1, ('E', 'Z'): 4, ('E', 'X'): -1,
            ('G', 'G'): 6, ('G', 'H'): -2, ('G', 'I'): -4, ('G', 'L'): -4, ('G', 'K'): -2, ('G', 'M'): -3, ('G', 'F'): -3,
            ('G', 'P'): -2, ('G', 'S'): 0, ('G', 'T'): -2, ('G', 'W'): -2, ('G', 'Y'): -3, ('G', 'V'): -3, ('G', 'B'): -1,
            ('G', 'Z'): -2, ('G', 'X'): -1, ('H', 'H'): 8, ('H', 'I'): -3, ('H', 'L'): -3, ('H', 'K'): -1, ('H', 'M'): -2,
            ('H', 'F'): -1, ('H', 'P'): -2, ('H', 'S'): -1, ('H', 'T'): -2, ('H', 'W'): -2, ('H', 'Y'): 2, ('H', 'V'): -3,
            ('H', 'B'): 0, ('H', 'Z'): 0, ('H', 'X'): -1, ('I', 'I'): 4, ('I', 'L'): 2, ('I', 'K'): -3, ('I', 'M'): 1,
            ('I', 'F'): 0, ('I', 'P'): -3, ('I', 'S'): -2, ('I', 'T'): -1, ('I', 'W'): -3, ('I', 'Y'): -1, ('I', 'V'): 3,
            ('I', 'B'): -3, ('I', 'Z'): -3, ('I', 'X'): -1, ('L', 'L'): 4, ('L', 'K'): -2, ('L', 'M'): 2, ('L', 'F'): 0,
            ('L', 'P'): -3, ('L', 'S'): -2, ('L', 'T'): -1, ('L', 'W'): -2, ('L', 'Y'): -1, ('L', 'V'): 1, ('L', 'B'): -4,
            ('L', 'Z'): -3, ('L', 'X'): -1, ('K', 'K'): 5, ('K', 'M'): -1, ('K', 'F'): -3, ('K', 'P'): -1, ('K', 'S'): 0,
            ('K', 'T'): -1, ('K', 'W'): -3, ('K', 'Y'): -2, ('K', 'V'): -2, ('K', 'B'): 0, ('K', 'Z'): 1, ('K', 'X'): -1,
            ('M', 'M'): 5, ('M', 'F'): 0, ('M', 'P'): -2, ('M', 'S'): -1, ('M', 'T'): -1, ('M', 'W'): -1, ('M', 'Y'): -1,
            ('M', 'V'): 1, ('M', 'B'): -3, ('M', 'Z'): -1, ('M', 'X'): -1, ('F', 'F'): 6, ('F', 'P'): -4, ('F', 'S'): -2,
            ('F', 'T'): -2, ('F', 'W'): 1, ('F', 'Y'): 3, ('F', 'V'): -1, ('F', 'B'): -3, ('F', 'Z'): -3, ('F', 'X'): -1,
            ('P', 'P'): 7, ('P', 'S'): -1, ('P', 'T'): -1, ('P', 'W'): -4, ('P', 'Y'): -3, ('P', 'V'): -2, ('P', 'B'): -2,
            ('P', 'Z'): -1, ('P', 'X'): -2, ('S', 'S'): 4, ('S', 'T'): 1, ('S', 'W'): -3, ('S', 'Y'): -2, ('S', 'V'): -2,
            ('S', 'B'): 0, ('S', 'Z'): 0, ('S', 'X'): 0, ('T', 'T'): 5, ('T', 'W'): -2, ('T', 'Y'): -2, ('T', 'V'): 0,
            ('T', 'B'): -1, ('T', 'Z'): -1, ('T', 'X'): 0, ('W', 'W'): 11, ('W', 'Y'): 2, ('W', 'V'): -3, ('W', 'B'): -4,
            ('W', 'Z'): -3, ('W', 'X'): -2, ('Y', 'Y'): 7, ('Y', 'V'): -1, ('Y', 'B'): -3, ('Y', 'Z'): -2, ('Y', 'X'): -1,
            ('V', 'V'): 4, ('V', 'B'): -3, ('V', 'Z'): -2, ('V', 'X'): -1, ('B', 'B'): 4, ('B', 'Z'): 1, ('B', 'X'): -1,
            ('Z', 'Z'): 4, ('Z', 'X'): -1, ('X', 'X'): -1}


pattern = "FATCAT"
text = "FASTCAR"
def edit_distance_dp(pattern,text):
    # Init
    dp_matrix = [[0 for _ in range(len(text)+1)] for _ in range(len(pattern)+1)]
    #Write the values of the first column and line
    for v in range(len(pattern)+1):
        dp_matrix[v][0] = v*(-2)
    for h in range(len(text)+1):
        dp_matrix[0][h] = h*(-4)
    # Compute DP Matrix
    for h in range(1,len(text)+1):
        for v in range(1,len(pattern)+1):
            #Save the pair of aa into a variable
            pair = text[h-1], pattern[v-1]
            #Look fot the pair the other way round if it is not in the dictionary
            if pair not in blosum62:
                pair = pattern[v-1], text[h-1]
                #If the pair is not in the dictionary, inform that there is an unvalid character
                if pair not in blosum62:
                    print("Unvalid character in input sequences")
                    exit()
            #Write in that position of the matrix the maximum puntuation
            dp_matrix[v][h] = max (
                #Punctuation for a match or missmatch (using the blosum dictionary)
                dp_matrix[v-1][h-1] + blosum62[pair],
                #Punctuation for insertions/deletions
                dp_matrix[v][h-1] - 4,
                dp_matrix[v-1][h] - 2)
    return dp_matrix

def print_dp_matrix(dp_matrix):
    for x in dp_matrix:
        print(x)

def backtrace_matrix(pattern,text,dp_matrix):
    v = len(pattern)
    h = len(text)
    cigar = []
    while v > 0 and h > 0:
        #Look for the followed path and write the corresponding letter in the cigar sequencce
        if dp_matrix[v][h] == dp_matrix[v-1][h] -2:
            v -= 1
            cigar.insert(0,"D")
        elif dp_matrix[v][h] == dp_matrix[v][h-1] - 4:
            h -= 1
            cigar.insert(0,"I")
        else:
            v -= 1
            h -= 1
            if pattern[v] == text[h]:
                cigar.insert(0,"M")
            else:
                cigar.insert(0,"X")
    if v > 0:
        for _ in range(v): cigar.insert(0,"D")
    if h > 0:
        for _ in range(h): cigar.insert(0,"I")
    return cigar

def pretty_print_alignment(pattern,text,cigar):
        (pattern_txt,i) = ("",0)
        operation_txt = ""
        (text_txt,j) = ("",0)
        for op in cigar:
            if op == "M":
                pattern_txt += pattern[i]
                i += 1
                operation_txt += "|"
                text_txt += text[j]
                j += 1
            elif op == "X":
                pattern_txt += pattern[i]
                i += 1
                operation_txt += " "
                text_txt += text[j]
                j += 1
            elif op == "I":
                pattern_txt += " "
                operation_txt += " "
                text_txt += text[j]
                j += 1
            elif op == "D":
                pattern_txt += pattern[i]
                i += 1
                operation_txt += " "
                text_txt += " "
        print(pattern_txt)
        print(operation_txt)
        print(text_txt)

dp_matrix = edit_distance_dp(pattern,text)
print_dp_matrix(dp_matrix)

cigar = backtrace_matrix(pattern,text,dp_matrix)
pretty_print_alignment(pattern,text,cigar)