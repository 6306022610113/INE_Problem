def gimme_the_letters(spectrum):

    first , last = map(ord, spectrum.split('-'))
    return ''.join(chr(i) for i in range (first, last+1))

print (gimme_the_letters("a-z"))
print (gimme_the_letters("h-o"))
print (gimme_the_letters("Q-Z"))
print (gimme_the_letters("J-J")) 