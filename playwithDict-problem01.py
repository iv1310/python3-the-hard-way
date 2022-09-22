"""
This program just to provides a quick way to pretty print a dict which has dict as values.
The method is using loops. We just loop each dict element and it's corresponding values using brute manner in loops.
"""

test_dict = {'gfg' : {'rate' : 5, 'remark' : 'good'}, 'cs' : {'rate' : 3}}

print(f"The original dict is {test_dict}")

print("The pretty print dict is : ")
for sub in test_dict:
    print(sub)
    for sub_nest in test_dict[sub]:
        print(f"{sub_nest} : {test_dict[sub][sub_nest]}")
