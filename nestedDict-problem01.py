"""
Sometimes, while working with Python dictionaries, we can have a problem in which we need to filter out certain values based on certain condition on a particular type,
e.g all values small than K. This task becomes complex when dictionary values can be heterogeneous.

Input : test_dict = {‘Gfg’ : 10, ‘for’ : ‘geeks’}
Output : {‘Gfg’: 10, ‘for’: ‘geeks’}

Input : test_dict = {‘Gfg’ : ‘geeks’}
Output : {‘Gfg’: ‘geeks’}
"""

# This method using type() + dictionary comprehension 

test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}

print("The original dictionary: " + str(test_dict))

K = 3

# Filter dictionary values in heterogeneous dict using type() + dict comprehension
res = { k:v for k,v in test_dict.items() if type(v) != int or v > K}

print("Values greater than K: " + str(res))


# This method using isinstance() + dict comprehension

reS = { k:v for k,v in test_dict.items() if not isinstance(v, int) or v > K}

print("Method2\nValues greater than K: " +str(reS))
