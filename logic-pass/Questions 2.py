lower = 0
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")
# num 7  
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
    if num > 1:
        # 2, 3, 4, 5, 6
        for i in range(2, num):
            print('testing', num, 'againents', i)
            if (num % i) == 0:
                break
        else:
            print(num)