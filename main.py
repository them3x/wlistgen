import sys
import numbers, variations
import os


if len(sys.argv) == 1:
	print ("python3 " + sys.argv[0] + " word1 word2 etc...")
	exit(0)

words = sys.argv
del words[0]

print ("[!] Creating wordlist")

n = numbers.NBS()
vr = variations.VRAT()

words = vr.ITL(words)

final = []
for w in words:
	final += n.basic(w)

final += words
final = list(set(final)) # Shuffle the list

filename = "wordlist.txt"

def get_unique_filename(filename):
	counter = 1
	new_filename = filename
	print("[!] Saving to " + new_filename)
	while os.path.exists(new_filename):
		print ("[X] " + new_filename + " already exists")
		base, ext = os.path.splitext(filename)
		new_filename = f"{base}.{counter}{ext}"
		counter += 1
		print("[!] Saving to " + new_filename)

	return new_filename

unique_filename = get_unique_filename(filename)

with open(unique_filename, 'w') as file:
	for i in final:
		file.write(i + '\n')
print ("Done!")
