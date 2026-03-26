# 17_FizzBuzz_Logic.py
def fizzbuzz():
    fizz = buzz = fizzbuzz = 0

    for i in range(1, 51):
        if i % 15 == 0:
            print("FizzBuzz")
            fizzbuzz += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz += 1
        else:
            print(i)

    print("Fizz:", fizz)
    print("Buzz:", buzz)
    print("FizzBuzz:", fizzbuzz)

fizzbuzz()
