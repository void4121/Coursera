with open("lorem.txt") as file:
    for line in file:
        print(line.strip().upper())

print ("\n")

file = open("lorem.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
