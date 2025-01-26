def validate_hello(greetings):
    valid = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for word in valid:
        if word in greetings.lower():
            return True
    return False

print(validate_hello('hombre! Hola!'))