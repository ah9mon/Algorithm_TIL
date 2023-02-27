a = 3
b = 6
c = - 5

import math

root1 = round((-b + math.sqrt(b ** 2 - 4 * a * c) )/2*a , 4)
root2 = round((-b - math.sqrt(b ** 2 - 4 * a * c) )/2*a , 4)
root_tuple = (root1, root2)
print(root_tuple)