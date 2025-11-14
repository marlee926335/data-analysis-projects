# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
# b) Within the function, use the 'list' function to split a string into a list of individual characters
# c) 'reverse' your new list.
# d) Use 'join' to create the reversed string and return that string from the function.
'''def reverse_characters(string):
    new_list = list(string)
    rev_list = new_list.reverse()
    rev_string = ''.join(new_list)
    return rev_string

print(f"today I'm feeling {reverse_characters("happy")}.")'''
# e) Create a variable of type string to test your new function. # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
# g) Use method chaining to reduce the lines of code within the function.


# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.
def reverse_characters(string):
    if type(string) == str :
        new_list = list(string)
        rev_list = new_list.reverse()
        rev_string = ''.join(new_list)
        return rev_string
    if type(string) == int :
        num_string = str(string)
        num_list = list(num_string)
        num_list.reverse()
        string_num = "".join(num_list)
        final_num = int(string_num)
        return final_num


'''print(f"today I'm feeling {reverse_characters(91294)}.")'''
# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.

def reverse_list(old_list):
    final_list = []
    for x in old_list:
        final_list.append(reverse_characters(x))
    return final_list


list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

print(reverse_list(list_test1))
print(reverse_list(list_test2))
print(reverse_list(list_test3))