print(range(100))
my_list = list(range(5,10))
print(my_list)
even = list(range(0, 10, 2))
odd = list(range(1,10,2))
print(odd)
print(even)

print("++++++++++++++++++++++++++++")
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0,10)
print(small_decimals)
print(small_decimals.index(3))

sevens = range(7, 1000000, 7)
x = int(input("Please enter a positive number less than on millon: "))
if x in sevens:
    print(f"{x} is divisible by seven!")
else:
    print(f"The number {x} is not divisible by seven!")

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in range(3,40,3):
    print(i)



