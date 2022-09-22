# In this program we'll see why does a nested loop performs better than the flattened loop. 

import time

# flattened loop
def loop(n):
    for i in range(n**3):
        pass

# nested loop
def nested(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass

for i in range(10, 100, 10):
    start = time.time()
    loop(i)
    print(f"For flattened loop: {time.time() - start}")

    start = time.time()
    nested(i)
    print(f"For nested loop: {time.time() - start}")
    print()
