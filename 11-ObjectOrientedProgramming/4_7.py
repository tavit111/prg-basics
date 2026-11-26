###
# Calculates basic statistics for a set of numbers
#
class Statistics:
    def __init__(self):
        self.numbers = []

    # Add a number from keyboard
    def add_number(self):
        number = float(input("Enter a number: "))
        self.numbers.append(number)

    # Display all numbers
    def show_numbers(self):
        print("Numbers:", *self.numbers)

    # Find the greatest number
    def maximum(self):
        return max(self.numbers)

    # Find the smallest number
    def minimum(self):
        return min(self.numbers)

    # Calculate arithmetic mean
    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    # Calculate median
    def median(self):
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)

        if n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    # Display calculated statistics
    def show_statistics(self):
        print("Minimum:", self.minimum())
        print("Maximum:", self.maximum())
        print("Arithmetic mean:", self.mean())
        print("Median:", self.median())


# Object creation
stats = Statistics()

# Read five numbers from keyboard
for i in range(5):
    stats.add_number()

# Display numbers and statistics
print()
stats.show_numbers()
stats.show_statistics()