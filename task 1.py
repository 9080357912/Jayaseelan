

# 1. Variables and Data Types
age = 5                 
weight = 30.5           
dog_name = "Buddy"      
is_training = True      
print("Variables and Data Types:")
print(f"age: {age}, type: {type(age)}")
print(f"weight: {weight}, type: {type(weight)}")
print(f"dog_name: {dog_name}, type: {type(dog_name)}")
print(f"is_training: {is_training}, type: {type(is_training)}\n")

# 2. Arithmetic Operations
bones = 10
toys = 4

print("Arithmetic Operations:")
print(f"{bones} + {toys} = {bones + toys}")
print(f"{bones} - {toys} = {bones - toys}")
print(f"{bones} * {toys} = {bones * toys}")
print(f"{bones} / {toys} = {bones / toys}")
print(f"{bones} % {toys} = {bones % toys}\n")

# 3. String Manipulations
greeting = "Woof"
dog_name = "Buddy"

print("String Manipulations:")
print(greeting + " " + dog_name)
print(dog_name.upper())
print(dog_name.lower())
print(dog_name.replace("Buddy", "Max"))
print(f"Length of dog_name: {len(dog_name)}\n")

# 4. Conditional Statements
weight = 30.5

print("Conditional Statements:")
if weight > 25:
    print(f"{dog_name} is a large dog")
elif weight == 25:
    print(f"{dog_name} is a medium-sized dog")
else:
    print(f"{dog_name} is a small dog")
print()

# 5. Loops
print("Loops:")
print("For Loop:")
for i in range(5):
    print(f"Iteration {i}")

print("\nWhile Loop:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
print()

# 6. Functions
def greet_dog(name):
    return f"Hello, {name}!"

print("Functions:")
print(greet_dog("Buddy"))
print()

# 7. Data Structures: Lists, Dictionaries, and Tuples
# List
dog_breeds = ["Beagle", "Bulldog", "Poodle"]
print("List:")
print(f"Dog breeds: {dog_breeds}")
dog_breeds.append("Golden Retriever")
print(f"Dog breeds after append: {dog_breeds}\n")

# Dictionary
dog = {
    "name": "Buddy",
    "age": 5,
    "favorite_toys": ["Ball", "Bone"]
}
print("Dictionary:")
print(f"Dog: {dog}")
dog["age"] = 6
print(f"Dog after age update: {dog}")
print(f"Dog's favorite toys: {dog['favorite_toys']}\n")

# Tuple
dimensions = (50, 20)  # Length and height of the dog's crate
print("Tuple:")
print(f"Dimensions: {dimensions}")
print(f"Length: {dimensions[0]}, Height: {dimensions[1]}")
