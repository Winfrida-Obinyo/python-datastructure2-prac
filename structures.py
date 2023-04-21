# # Write a Python function that takes a listof numbers
# # as an argument and returns the sum and product of all the numbers.
def list_operations(my_list):
    sum_of_list = sum(my_list)
    product = 1
    for item in my_list:
        product *= item
    return sum_of_list, product

my_list = [1, 2, 3, 4, 5]
print(list_operations(my_list))

 # Write a Python program to create a tuple 
 # of strings and sort them in alphabetical order.
def sort_alphabetical_order(tuple_string):
    sort_string = tuple(sorted(tuple_string))
    return sort_string
      
tuple_string=('adiddas','puma','socks','jackets')
print (sort_alphabetical_order(tuple_string))

# # Write a Python program to create a dictionary 
# # with keys as strings and values as integers, and 
# # find the sum of all the values in the dictionary.
    
def dictionary(cars):
    dict = sum(cars.values())
    return dict

cars = { 
"tuktuk":40,
"toyota":20,
"honda":24
}
print (dictionary(cars))

# Write a Python program to create a set of integers 
# and then add a new element to the set.
    
def add_element(names):
  name = list(names)
  name.append(23)
  sety = set(name)
  return sety

names={21,34,67,89}
print(add_element(names))

