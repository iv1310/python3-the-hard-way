from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

print(add(10, 12.5))

"""
If a function doesn't explicitly returns a value, we can use None to type hint the return value. 
"""
