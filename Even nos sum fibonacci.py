n1 = 0
n2 = 1
nxt = n2
Sum = 0
# nxt is the variable that contains the fibonacci series
while nxt <= 4000000:
    n1,n2 = n2 , nxt
    nxt = n1 + n2
    if nxt % 2==0:
        Sum += nxt
print("Sum of Even terms of fibonacci series is ",Sum)
