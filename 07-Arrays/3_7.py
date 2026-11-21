###
# Finds the longest name in an array
#
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]


names_by_len = sorted(names, key=len, reverse=True)
longest_name = names_by_len[0]

print("Names:", end=" ")
for name in names:
    print(name, end=" ")

print()
print("Longest name:", longest_name)