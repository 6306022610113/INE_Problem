def check(d1, d2, k):
    try:
        if d1[k] != d2[k]:
            return 'Not the same'
        return True
    except KeyError:
        return "One's empty"

dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
dict_second = { "people": 12, "sun": "star", "book": "bad" }

print(check(dict_first, dict_second, "horde")) 
print(check(dict_first, dict_second, "people"))  
print(check(dict_first, dict_second, "sun"))  