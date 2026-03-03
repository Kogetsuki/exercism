CODON_TO_AMINO = {
  "AUG": "Methionine",
  "UUU": "Phenylalanine",
  "UUC": "Phenylalanine",
  "UUA": "Leucine",
  "UUG": "Leucine",
  "UCU": "Serine",
  "UCC": "Serine",
  "UCA": "Serine",
  "UCG": "Serine",
  "UAU": "Tyrosine",
  "UAC": "Tyrosine",
  "UGU": "Cysteine",
  "UGC": "Cysteine",
  "UGG": "Tryptophan",
  "UAA": "STOP",
  "UAG": "STOP",
  "UGA": "STOP",
}

  
def proteins(strand):
  result = []

  for i in range(0, len(strand) - 2, 3):
    codon = strand[i:i+3]
    amino = CODON_TO_AMINO[codon]
    
    if amino == "STOP":
      break
    
    result.append(amino)

  return result