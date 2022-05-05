#prime numbers from  1to 10

num = 1
while num <= 10:
    if num>1:
        i = 2
        while i<= num//2:
            if num%i==0:
                break
            i+=1
        else:
            print(num)
    num+=1
