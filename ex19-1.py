from sys import argv

a, u = argv

def get_length(arg):
    return(len(arg))

# 1
print(get_length(u))

# 2
print(get_length(u+'leaf'))

# 3
print(get_length(u+'5'*4))

# 4
print(get_length('length\n'))

# 5
print(get_length('length'+'python'))

# 6
print(get_length('length' * 6))

# 7
temp = 'length'
print(get_length(temp))

# 8
print(get_length(temp+'python'))

# 9
print(get_length(temp*6))

# 10
print(get_length(open(input('filename: ')).read()))

# 11
print(get_length(input('A string: ')))

