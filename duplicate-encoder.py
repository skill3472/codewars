def duplicate_encode(word):
    word = word.lower()
    output = ''
    for i in range(len(word)):
        if i == 0:
            temp = word[1:]
        elif i == len(word)-1:
            temp = word[0:-1]
        else:
            temp = word[0:i] + word[i+1:]
        
        if word[i] in temp:
            output += ")"
        else:
            output += "("
    return output



print(duplicate_encode('test')) # Should be )(()