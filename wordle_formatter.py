def wordle_formatter(string):
    '''
    Current wordle line is passed in.
    Green boxes are in uppercase. Yellow boxes are in lowercase.
    Blank spaces must be formatted as underscores.
    For example, __Nic means N is green, i & c are yellow, and the other two are black
    
    Prints all possible combinations of words and blanks given the current situation.
    
    For __Nic, it would print the following:
    icN__
    i_Nc_
    _iNc_
    ciN__
    c_N_i
    _cN_i
    __Nci
    '''
    wordle_line = list(string)
    
    valid_letters = [] # init valid letters per position as list of lists
    
    char_list = list(set(wordle_line[:])) # list of yellow letters and a blank
    for c in char_list[:]: # remove uppers
        if c.isupper():
            char_list.remove(c)

    for char in string:

        if char == "_": # if position is blank, all yellow letters and blanks can go in that index. But no greens.
            valid_letters.append(char_list)

        elif char.isupper(): # if position is green, only that letter is allowed at the index
            valid_letters.append([char])

        elif char.islower(): # if position is yellow, that char is not allowed at that index, but others are fair game
            temp_list = char_list[:]
            temp_list.remove(char)
            valid_letters.append(temp_list)

        else: 
            print(char)
            raise Exception("Something bad happened")

    all_permutations = list(itertools.product(*valid_letters))

    for permutation in all_permutations: # if same count of letters
        if sorted(wordle_line) == sorted(permutation):
            print(''.join(permutation).upper())
