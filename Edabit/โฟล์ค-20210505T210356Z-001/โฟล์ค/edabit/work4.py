def jay_and_bob(txt):
    
    d = {'half':14 , 'quarter':7,
         'eighth':3.5, 'sixteenth':1.75}
    return "{} grams" .format(d[txt])

print (jay_and_bob("half"))
print (jay_and_bob("quarter"))
print (jay_and_bob("eighth"))