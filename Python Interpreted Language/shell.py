import ERL

while True:
		text = input('ERL >>> ')
		result, error = ERL.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)