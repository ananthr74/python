import math

class MathOperations:
    def __init__(self, numbers):
        self.numbers = numbers

    def square(self, x):
        return x ** 2

    def cube(self, x):
        return x ** 3

    def square_root(self, x):
        return math.sqrt(x)

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        if n % 2 == 0:
            mid1 = sorted_numbers[n // 2 - 1]
            mid2 = sorted_numbers[n // 2]
            return (mid1 + mid2) / 2
        else:
            return sorted_numbers[n // 2]

    def standard_deviation(self):
        mean = self.mean()
        squared_diff = [(x - mean) ** 2 for x in self.numbers]
        variance = sum(squared_diff) / len(self.numbers)
        std_dev = math.sqrt(variance)
        return std_dev

# Example usage:
numbers = [1, 2, 3, 4, 5]
calculator = MathOperations(numbers)

print("Square of 3:", calculator.square(3))
print("Cube of 3:", calculator.cube(3))
print("Square root of 25:", calculator.square_root(25))
print("Mean:", calculator.mean())
print("Median:", calculator.median())
print("Standard Deviation:", calculator.standard_deviation())

