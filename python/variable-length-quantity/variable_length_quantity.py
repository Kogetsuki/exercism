def encode(numbers):
  bytes_ = []

  for n in numbers:
    chunks = []
    while True:
      chunks.append(n & 0x7F)
      n >>= 7
      
      if n == 0:
        break
      
    chunks = chunks[::-1]
    bytes_ += [c + 128 for c in chunks[:-1]] + [chunks[-1]]
            
  return bytes_
    

def get_chunks(bytes_):
  i = 0
  while i < len(bytes_):
    chunk = []
    while True:
      if i >= len(bytes_):
        raise ValueError("incomplete sequence")

      byte = bytes_[i]
      chunk.append(byte)
      i += 1
      
      if byte >> 7 == 0:
        break
      
    yield chunk
    
    
def decode(bytes_):
  chunks = list(get_chunks(bytes_))
  print(chunks)
    
  result = []
  for chunk in chunks:
    total = 0
    
    for i, c in enumerate(chunk):
      c %= 128
      shift_count = len(chunk) - i - 1
      
      while shift_count > 0:
        c <<= 7
        shift_count -= 1
        
      total += c

    result.append(total)
    
  return result
