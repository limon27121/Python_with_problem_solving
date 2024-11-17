n = int(input("Enter your range: "))
sum = 0

# Loop through the first n even numbers
for i in range(2, 2 * n + 1, 2):  # Generates 2, 4, 6, ..., 2n
    sum += i**2

print("Total sum is:", sum)


