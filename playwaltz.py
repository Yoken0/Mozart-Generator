import stdaudio
import stdio
import sys

# this line Uses readAllLines(returns a list using given input) to create waltz_measure list

waltz_measure = stdio.readAllInts()

# Creating the check for each condition

# 1) check if measure is exactly 32, since all waltz pieces are 32 measures
if len(waltz_measure) != 32:
    stdio.writeln("A Waltz must contain exactly 32 measures")

    # Creating a loop to check each measure individually

    for x in range(len(waltz_measure)):
        # this line checks if current measure is a minuet which will be all measure before the 16th measure
        if x < 16:
            # this line Check if measure falls under the possible range of minuet measures
            if int(waltz_measure[x]) > 176 or int(waltz_measure[x]) < 1:
                # this line prints to standard output the error message when the trio measure is inadequate
                sys.exit("A minuet measure must be from [1, 176]")

        else:
            # Check if measure falls under the possible range of minuet measures
            if int(waltz_measure[x]) > 96 or int(waltz_measure[x]) < 1:
                # this line prints to standard output the error message when the trio measure is inadequate
                sys.exit("A trio measure must be from [1, 96]")


# after checking all measures, play the minuets and trio measures individually
for measure in range(len(waltz_measure)):
    # this line creates this variable since you cannot call playFile with an array
    if measure < 16:
        # this line plays the .wav file that corresponds to the measure for the minuet
        stdaudio.playFile('data/M' + str(waltz_measure[measure]))
    else:
        # this line plays the .wav file that corresponds to the measure for the Trio
        stdaudio.playFile('data/T' + str(waltz_measure[measure]))
