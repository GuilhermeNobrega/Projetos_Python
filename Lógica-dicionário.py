# Below are the examples of getting the index of specified Key

# Initialize dictionary
my_dict = {'course' : 'Python', 'fee' : 4500, 'duration' : '45 days'}

# Example 1: Get the index position of the specified key
# In Dictionary using list() and index()
# Initialize the index
index = None
if "fee" in my_dict:
    index = list(my_dict).index("course")
print("Index of fee:", index) 


#-----------------------------


# Initialize dictionary
my_dict = {'course': 'Python', 'fee': 4500, 'duration': '45 days'}

# Specify the key you're looking for
key_to_find = 'fee'

# Use the get() method to retrieve the value and index
if key_to_find in my_dict:
  index = list(my_dict).index(key_to_find)
else:
  index = None

if index is not None:
    print(f"Index of {key_to_find}: {index}")
else:
    print(f"The key '{key_to_find}' is not present in the dictionary.")



#https://sparkbyexamples.com/python/get-the-index-of-key-in-python-dictionary/
