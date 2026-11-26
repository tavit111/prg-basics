###
# Stadium sectors and number of fans
#
class C:
    def __init__(self, sectors):
        self.sectors = sectors

    # Change or add a sector
    def m1(self, s, n):
        self.sectors[s] = n

    # Calculate total number of fans in selected sectors
    def m2(self, s):
        total = 0

        for sector in s:
            if sector in self.sectors:
                total += self.sectors[sector]

        return total


# Object creation
stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

# Change number of fans in sector G
stadium.m1("G", 130)

# Display results
print("GD:", stadium.m2("GD"))
print("KEJ:", stadium.m2("KEJ"))