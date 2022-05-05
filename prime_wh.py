Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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