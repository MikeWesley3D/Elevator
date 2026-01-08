# Elevator
Elevator Project

### Instructions
Run the `elevator.py` script with your locally installed python instance
```
<python3> elevator.py
```
Running the elevator script without any variables should give the following
```
usage: elevator [-h] [--start START] floors [floors ...]
elevator: error: the following arguments are required: floors
```
Running the script with the `-h` or `--help` flag should give the following
```
<python3> elevator.py -h
usage: elevator [-h] [--start START] floors [floors ...]

A simple script to simulate an elevator and return the distance travlled along with the floors travelled to.

positional arguments:
  floors         A list of desired floors to travel to

options:
  -h, --help     show this help message and exit
  --start START  Floor number to start the elevator from
```
The following optional flags are used:
    * **--start** The floor, as an integer, to start the elevator from

The following arguments are required:
    * **floors** A series of integers depicting to be travelled to in order

Example:
```
<python3> elevator.py --start 12 2 9 1 32
Starting at floor 12
Distance travlled: 560
Floors travelled to: 12 2 9 1 32
```
