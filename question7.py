#given set of code
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
#continue here
#process list
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers bigger than 50 with random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    elif random_numbers[i] < 50:
        # Replace numbers smaller than 50 with "XX"
        random_numbers[i] = "XX"

# Print the final list
print("Modified List:", random_numbers)