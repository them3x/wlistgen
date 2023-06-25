from datetime import datetime

class NBS():

	def basic(__init__, word):
		new = []

		numbers = ["123", "1234", "12345", "1111", "55555", "2000", "7777", "666", "4321", "54321", "1122", "1212", "1221"]

		years = []
		current_year = datetime.now().year

		for n in numbers:
			new.append(word + n)
			new.append(word + "@" + n)
			new.append(word + "#" + n)

		for i in range(1, 11):
			years.append(str(current_year - i))
			years.append(str(current_year - i)[-2:])

		for i in range(1, 11):
			years.append(str(current_year + i))
			years.append(str(current_year + i)[-2:])

		for y in years:
			new.append(word + y)
			new.append(word + "@" + y)
			new.append(word + "#" + y)

		return new
