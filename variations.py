from itertools import combinations, product

class VRAT():
	def ITL(__init__, words):

		def replacing(s):
			replacements = [
				('a', '@'),
				('i', '1'),
				('o', '0'),
				('s', '5'),
				('e', '3'),]

			combinations = [s]  # começa com a string original
			for old, new in replacements:
				new_combinations = []
				for combination in combinations:
					if old in combination:
						new_combinations.append(combination.replace(old, new))
				combinations += new_combinations  # adicione as novas combinações

			return combinations

		def all_combinations(lst):
			new = []
			for r in range(1, len(lst) + 1):
				for combination in combinations(lst, r):
					new.append(''.join(combination))
			return new

		final = []

		new = []
		nnew = []
		for w in words:
			new.append(w.lower())

		nnew += all_combinations(new)
		final += nnew

		new = []
		nnew = []
		for w in words:
			new.append(w.upper())

		nnew += all_combinations(new)
		final += nnew

		new = []
		nnew = []
		for w in words:
			new.append(w.capitalize())

		nnew += all_combinations(new)
		final += nnew

		f = []
		for s in final:
			f += replacing(s)

		return list(set(f)) # IF EXISTS.. REMOVE DUPLICATE ITENS
