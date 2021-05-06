def find_cadence(chords):
	if chords[-2:] == ["V", "I"]: return "perfect"
	if chords[-2:] == ["IV", "I"]: return "plagal"
	if chords[-2] == "V": return "interrupted"
	if chords[-1] == "V": return "imperfect"
	return "no cadence"

print(find_cadence(["I", "IV", "V"]))

print(find_cadence(["ii", "V", "I"]))

print(find_cadence(["I", "IV", "I", "V", "vi"]))