import hw4_util

def location_by_zip

def zip_by_location(zip_codes, location):
	city, state = location
	codes = []
	for data in (zip_codes):
		if data[3] == city and data[4] == state:
			codes.append(data[0])

	return codes


zip_codes = hw4_util.read_zip_all()

command = ''

while command != 'end':
	
	command = input("Command ('loc', 'zip', 'dist', 'end') => ")
	print(command)

	if command == 'loc':
		zipcode = input('Enter a ZIP code to lookup => ')
		print(zipcode)

	elif command == 'zip':
		city = input('Enter a city name to lookup => ')
		print(city)
		state = input('Enter a state name to lookup => ')
		print(state)
		city = city.title()
		state = state.upper()
		zips = zip_by_location(zip_codes, (city, state))
		if len(zips) == 0:
			print('No ZIP code found for {}, {}'.format(city, state))
		else:
			print('The following ZIP code(s) found for {}, {}: '.format(city, state), end='')
			for i in range(len(zips) - 1):
				print(zips[i], end=', ')
			print(zips[len(zips) - 1])
		print()

	elif command == 'dist':
		pass

	elif command == 'end':
		pass

	else:
		print('Invalid command, ignorin')