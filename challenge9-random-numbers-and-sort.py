import random
import time

numbers = [6, 2, 1, 8, 4, 7, 9, 5]
random.shuffle(numbers)
quicksort = numbers.sort()
start = time.time()
quicksort
end = time.time()
duration = start - end
print(duration)