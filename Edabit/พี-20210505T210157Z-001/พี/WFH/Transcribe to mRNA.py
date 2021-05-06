def dna_to_rna(dna):
	length = len(dna)
	rna = ""
	for i in range(length):
		if dna[i] == "A":
			rna = rna + "U"
		if dna[i] == "T":
			rna = rna + "A"
		if dna[i] == "G":
			rna = rna + "C"
		if dna[i] == "C":
			rna = rna + "G"
	return rna

print(dna_to_rna("GCGTAC"), "= GCGTAC")
print(dna_to_rna("ATTAGCGCGATATACGCGTAC"), "= ATTAGCGCGATATACGCGTAC")
print(dna_to_rna("CAGTATGCTGCAT"), "= CAGTATGCTGCAT")
print(dna_to_rna("CGATATA"), "= CGATATA")
print(dna_to_rna("GCAGCTACA"), "= GCAGCTACA")
