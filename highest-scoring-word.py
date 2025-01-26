from string import ascii_lowercase

def high(x):
    alpha = list(ascii_lowercase)
    words = x.split()
    highest = 0
    highestWord = ''
    for word in words:
        score = 0
        for letter in word:
            score += alpha.index(letter) + 1
        if score > highest:
            highest = score
            highestWord = word
    return highestWord