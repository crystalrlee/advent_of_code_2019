# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass,
# divide by three, round down, and subtract 2.
# What is the sum of the fuel requirements for all of the modules on your spacecraft?

def main():
    values = []

    with open("fuel-amounts.txt") as file:
        mass = [int(line.strip()) for line in file.readlines()]

    for num in mass:
        values.append((num//3)-2)

    answer = sum(values)
    print(answer)
    
main()
