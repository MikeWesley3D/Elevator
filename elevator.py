# Program to simulate an elevator
import argparse

# A constaatnt keeping track of the amount of time it takes to travel between
# floors
TRAVEL_TIME = 10

def parse_elevator_args():
	"""
	Parse elevator arguments
	"""
	parser = argparse.ArgumentParser(
		prog='elevator',
		description='A simple script to simulate an elevator and return the '
					'distance travlled along with the floors travelled to.'
	)
	# There are more features that could be added to the help output, this was
	# simplest

	# Which floor the elevator starts from, will default to 0
	parser.add_argument(
		'--start',
		type = int,
		default = 0,
		help='Floor number to start the elevator from'
	)
	# Could have it print an erro instead if the starting floor is required

	# A list of floors to travel to
	# Will print an error if no floors are specified
	parser.add_argument(
		'floors',
		nargs='+',
		type=int,
		help='A list of desired floors to travel to'
	)
	# Could also update it to print out just the starting floor and a distance
	# travelled as 0 if no floors were specified
	return parser.parse_args()

def elevator(args):
	"""
	Simulate an elevator

	Arguments:
		args: An argument parser containing arguments for the elevator start
			  and floors to travel to
	"""

	print(f'Starting at floor {args.start}')
	floors = args.floors

	# Need to keep track of the amount of floors travelled
	floors_traveled = 0
	# Need to keep track of the current floor
	current_floor = args.start
	# Need to add the distance travelled for every floor
	for next_floor in floors:
		if next_floor > current_floor:
			floors_traveled += (next_floor - current_floor)
		else:
			floors_traveled += (current_floor - next_floor)
		# Switch to the next floor
		current_floor = next_floor
	print(f'Distance travlled: {floors_traveled * TRAVEL_TIME}')
	# Add the starting floor to the list to be printed
	floors.insert(0, args.start)
	# Need to cast floor ints as strings before using join function
	print(f'Floors travelled to: {" ".join(str(x) for x in floors)}')


if __name__=="__main__":
	# Parse the arguments to the program
	args = parse_elevator_args()
	# Run the elevator script with parsed arguments
	elevator(args)