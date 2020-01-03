# An Intcode program is a list of integers separated by commas. To run one, start by looking at the first integer (called position 0).
# Here, you will find an opcode - either 1, 2, or 99.
# Opcode 1 adds together numbers read from two positions and stores the result in a third position.
# 2: multiplies, 3: halts program.

# The three integers immediately after the opcode tell you these three positions -
# the first two indicate the positions from which you should read the input values,
# and the third indicates the position at which the output should be stored.

# Find noun (at address 1) and verb (at address 2) that produce the output 19690720

def main():
    with open("list.txt") as file:
        intcode = file.read().strip().split(",")
    for j in range(len(intcode)):
        intcode[j] = int(intcode[j])


    for n in range(100):
        intcode[1] = n

        for m in range(100):
            copy_intcode = intcode.copy()
            copy_intcode[2] = m
            i = 0

            while True:
                if copy_intcode[i] == 99:
                    break

                elif copy_intcode[i] == 1:
                    #print(i, copy_intcode[i], copy_intcode[i+1], copy_intcode[i+2], copy_intcode[i+3])
                    copy_intcode[copy_intcode[i+3]] = copy_intcode[copy_intcode[i+1]] + copy_intcode[copy_intcode[i+2]]
                    i = i + 4

                elif copy_intcode[i] == 2:
                    #print(i, copy_intcode[i], copy_intcode[i+1], copy_intcode[i+2], copy_intcode[i+3])
                    copy_intcode[copy_intcode[i+3]] = copy_intcode[copy_intcode[i+1]] * copy_intcode[copy_intcode[i+2]]
                    i = i + 4

                else:
                    print("something went wrong.")

            if copy_intcode[0] == 19690720:
                print("Your number is: ",copy_intcode[0], " and verb is:", n, " noun is:", m)
                return


main()
