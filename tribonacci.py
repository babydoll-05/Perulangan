n = 10  
a, b, c = 0, 1, 1  
print(a, b, c, end=" ")
for _ in range(n - 3):  
    next_num = a + b + c  
    print(next_num, end=" ")
    a, b, c = b, c, next_num