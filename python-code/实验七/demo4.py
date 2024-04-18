import string
import random
x = string.ascii_letters + string.digits
print(x)
print(''.join(random.sample(x,10)))