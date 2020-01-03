
def main():
    values = []

    with open("fuel-amounts.txt") as file:
        mass = [int(line.strip()) for line in file.readlines()]

    for num in mass:
        fuel = (num//3)-2
        values.append(fuel)
        fuel_for_fuel = fuel//3 - 2

        # checks if fuel needs fuel
        while fuel_for_fuel > 0:
            values.append(fuel_for_fuel)
            fuel_for_fuel = fuel_for_fuel//3 - 2 

    answer = sum(values)
    print(answer)

main()
