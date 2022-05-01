list = [1,2,3,4,5,6,7,8,9]

for i in list[1:]:
    print(i)

def fizz_buzz(num):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        
for i in range(1,30):
    fizz_buzz(i)