
# num = input('Enter a number to sum up! ')
def sum_to(num):
    sum = 0
    for i in range(num + 1 ):
        sum += i
    return sum

print(sum_to(6))