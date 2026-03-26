# 20_NumPy_Speed_Test.py
import time
import numpy as np

size = 1000000

start = time.time()
lst = list(range(size))
lst = [x*2 for x in lst]
print("List time:", time.time() - start)

start = time.time()
arr = np.arange(size)
arr = arr * 2
print("NumPy time:", time.time() - start)
