import random
import string

# print(random.random())
# print(random.randint(1,10))
# print(random.choices(1,3,5,6,10))
# print(random.choices(1,3,5,6,10))
print("[]".join(random.choices(string.ascii_letters + string.digits,k = 4)))


