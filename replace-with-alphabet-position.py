from string import ascii_lowercase

def alphabet_position(text):
    alpha = list(ascii_lowercase)
    out = []
    for letter in text:
        if letter.lower() in alpha:
            out.append(alpha.index(letter.lower()) + 1)
    return " ".join(str(x) for x in out)

print(alphabet_position('The sunset sets at twelve o\' clock.'))
