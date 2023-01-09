def generate_words(letters):
  words = []
  from itertools import permutations
  for perm in permutations(letters):
    words.append(''.join(perm))
  return words
words = generate_words(["n","b","c","x","u","x","t","p","k","r","u"])
def write_words_to_file(words, file_name):
  with open(file_name, 'w') as f:
    for word in words:
      f.write(word + '\n')
write_words_to_file(words, "words.txt")
