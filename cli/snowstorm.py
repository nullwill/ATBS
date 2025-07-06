import os, random, time, sys

TOP = chr(9600)
BOTTOM = chr(9604)
FULL = chr(9608)

# Set the snowstorm density to the command line argument
DENSITY = 4 # Default snow density is 4%
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear() # Clear terminal window.

    # Loop over each row and column:
    for y in range(40):
        for x in range(80):
            if random.randint(0, 99) < DENSITY:
                # Print snow:
                print(random.choice([TOP, BOTTOM]), end = '')
            else:
                # Print empty space:
                print(' ', end='')
        print() # Print a newline.

    # Print the snow-covered ground:
    print(FULL * 80 + '\n' + FULL * 80)
    print('(Ctrl-C to stop.)')

    time.sleep(.2)