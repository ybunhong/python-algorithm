import random
SEED, MIN, MAX, N= 10, 100, 1000, 10
random.seed(SEED)
S=random.sample(range(MIN, MAX), N)
print(min(S), S.index(min(S)))


import time
start = time.time()
print(min(S), S.index(min(S)))
end= time.time()

print(f"solve() elapsed time: {end - start}")
