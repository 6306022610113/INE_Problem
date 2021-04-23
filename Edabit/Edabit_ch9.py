def format_ascii(s, width):
	s_new = [] 
	while s:
		new = s[:width]
		s_new.append(new)
		s = s[width:]

	s_new1 = '\n'.join(s_new)
	return(s_new1)

print(format_ascii("0123456789", 2))
print(format_ascii("................................", 8))
print(format_ascii("^^^^^^^^", 1))