def invert(dct):
    
    return {v: k for k, v in dct.items()}

print (invert({ "z": "q", "w": "f" }))
print (invert({ "a": 1, "b": 2, "c": 3 }))
print (invert({ "zebra": "koala", "horse": "camel" }))
