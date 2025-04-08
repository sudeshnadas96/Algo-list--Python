#Write a Python program to map two lists into a dictionary.
#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
def map_list(keys , values):
    if len(keys) == len(values): #to check whether thr length of two list is same
        mapped_dict = dict(zip(keys, values)) # creating a dictionary using the dict method
    return mapped_dict
print(map_list(["A" , "B", "C"] , [1, 2, 3])) # {"A": 1, "B":2, "C":3}