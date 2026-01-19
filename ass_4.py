# 1 take a string inpute and print its lenght
s = input("Enter a string: ")
print("Length =", len(s))


# 2 convert a sentence to lowercase
sentence = input("Enter a sentence: ")
print(sentence.lower())


# 3 replace spaces with underscores in a string 
text = input("Enter a string: ")
print(text.replace(" ", "_"))


# 4 first and last charater of string 
s = input("Enter a string: ")

print("First character =", s[0])
print("Last character =", s[-1])

# 5 reverse a string using slicing
s = input("Enter a string: ")
print("Reversed string =", s[::-1])

# 6 count many times a letter appears in a string
s = input("Enter a string: ")
ch = input("Enter a letter: ")

count = s.count(ch)
print("Count =", count)


# 7 check word is present in a sentence 
sentence = input("Enter a sentence: ")
word = input("Enter a word to check: ")

if word in sentence:
    print("Word is present")
else:
    print("Word is not present")


# 8 take name & age and print using f string formatting 
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and my age is {age}")

# 9 remove extra  spaces from the start and end of a string 
s = input("Enter a string: ")
print(s.strip())

# 10 join alist of words into a single string with between them
words = ["Python", "is", "easy"]
result = " ".join(words)

print(result)


#    step-2 

# 1 cteate a list  of your 5 favorite movies
# Create a list of my 5 favorite movies
favorite_movies = [
    "3 Idiots",
    "Inception",
    "Avengers: Endgame",
    "Interstellar",
    "Bahubali"
]

print(favorite_movies)


# 2 add a new movie to the list 
# Existing list of favorite movies
favorite_movies = [
    "3 Idiots",
    "Inception",
    "Avengers: Endgame",
    "Interstellar",
    "Bahubali"
]

# Add a new movie to the list
favorite_movies.append("KGF")

print(favorite_movies)


# 3 remove the first movie from the list 
# Existing list of favorite movies
favorite_movies = [
    "3 Idiots",
    "Inception",
    "Avengers: Endgame",
    "Interstellar",
    "Bahubali",
    "KGF"
]

# Remove the first movie from the list
favorite_movies.pop(0)

print(favorite_movies)


# 4 sort a list of  numbers movie from the list 
# List of movies
favorite_movies = [
    "Inception",
    "Avengers: Endgame",
    "Interstellar",
    "Bahubali",
    "KGF"
]

# Sort the movie list alphabetically
favorite_movies.sort()

print(favorite_movies)


# 5 reverse a list 
# List of movies
favorite_movies = [
    "Inception",
    "Avengers: Endgame",
    "Interstellar",
    "Bahubali",
    "KGF"
]

# Reverse the list
favorite_movies.reverse()

print(favorite_movies)


# 6 find  the  largest number  in a list 
# List of numbers
numbers = [10, 45, 23, 89, 67]

# Find the largest number
largest = max(numbers)

print("Largest number:", largest)

# 7 merge two  lists into one 
# First list
list1 = [1, 2, 3]

# Second list
list2 = [4, 5, 6]

# Merge two lists
merged_list = list1 + list2

print(merged_list)


# 8 access the last element of a list without using index number 
# List of elements
my_list = [10, 20, 30, 40, 50]

# Access the last element without using index number
last_element = my_list[-1]

print("Last element:", last_element)


# 9 create  a nested list and access a specific inner element
# Create a nested list
nested_list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Access a specific inner element (50)
element = nested_list[1][1]

print("Accessed element:", element)


# 10 count how many time an element oppear in a list 
# List of elements
my_list = [1, 2, 3, 2, 4, 2, 5]

# Element to count
element = 2

# Count how many times the element appears
count = my_list.count(element)

print("Element appears", count, "times")