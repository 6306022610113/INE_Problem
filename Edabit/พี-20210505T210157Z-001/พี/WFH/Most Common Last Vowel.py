def common_last_vowel(txt):
	v = 'aeiou'
	for i in txt.lower()[::-1]:
		if i in v:
			return i

print(common_last_vowel("Hello World!"), )
print(common_last_vowel("Watch the characters dance!"), )
print(common_last_vowel("OOI UUI EEI AAI"), )
print(common_last_vowel("amy and acts"), )
print(common_last_vowel("munch munch munch tasty tasty brunch"), )