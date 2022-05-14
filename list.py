my_lists = ["January", "February", "March"]
print(my_lists[2])
my_lists.append("April")
print(my_lists[3])
my_lists.remove("February")
print(my_lists)

# user_input = ""
# while user_input != "exit":
#     user_input = input("Hey user, enter the number of days as a comma separated list: \n")
#     # print(user_input)
#     set_user_input = user_input.split(", ")
#     print(set_user_input)
#     num_of_element = set(set_user_input)
#     print(num_of_element)

my_set = {"January", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)