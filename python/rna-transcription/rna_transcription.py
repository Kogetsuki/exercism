def to_rna(dna_strand):
  complements = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
  }
 
  rna = "" 
  for nucleotide in dna_strand:
    rna += complements[nucleotide]

  return rna