# This is coding for making cache


import time
from functools import lru_cache

@lru_cache(maxsize=10)
def take_time(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("I am learning")
    take_time(5)
    print("I will be best in this")
    take_time(5)
    print("I want to fullfill my dreams")
    take_time(5)
    print("Thats I want to do")