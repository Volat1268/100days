import random

# a = random.randint(1, 10)
# b = random.randrange(1, 33, 2)
# c = random.random()
# d = random.uniform(1, 3)
# e_list = [random.uniform(10, 14) for i in range(5)]
# e_2 = e_list[1]
# e_choice = random.choice(e_list)
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e_list)
# print(e_2)
# print(f'random uniform float number #2 is {e_2:_<12.2f}')
# print(f'random uniform float number N2: {e_list[1]:/^12.2f}')
# print(e_choice)

lst = [random.randint(12, 33) for i in range(5)]
lst.append(99)
lst.extend(['citron', 'apple', 'orange'])
lst.insert(0, 'orange')
count_orange = lst.count('orange')
print(lst)
lst.remove('citron')
pop_index = lst.pop(-2)
pop_last = lst.pop()


print(lst)
print(count_orange)




