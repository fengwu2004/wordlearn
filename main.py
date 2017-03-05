# import links

import  time

last = time.time()

sum = 0

for i in range(3000):

    for j in range(3000):

        sum += i + j

last = time.time() - last

print('finish', last)