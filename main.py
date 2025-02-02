# Input list of numbers as strings with commas
numbers_with_commas = [
    "1,039,560",
    "1,039,557",
    "1,039,554",
    "1,039,555",
    "1,039,556",
    "1,039,558",
    "1,039,559"
]

# Remove commas and convert to integers, then join them as a comma-separated string
numbers_without_commas = ",".join(num.replace(",", "") for num in numbers_with_commas)
print(numbers_without_commas)
