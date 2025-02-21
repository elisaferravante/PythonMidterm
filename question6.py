# List (Mutable)
print("List Example:")
my_list = [11, 21, 31]
print("Original List:", my_list)

# Changing an element in list
my_list[1] = 25
print("Modified List:", my_list)

# Adding a new element in list
my_list.append(40)
print("After Append:", my_list)

# String (Immutable)
print("\nString Example:")
my_string = "Bonjour"
print("Original String:", my_string)

# Try to change a character (will give an error)
try:
    my_string[0] = "S"  # not allowed for strings
except TypeError as e:
    print("Error:", e)

# Instead creating a new string
new_string = "S" + my_string[1:]
print("New String:", new_string)