import math


def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num

def compute_zeroes(num):
    zeros = 0
    
    i = 5
    while num / i > 0:
        zeros += math.floor(num / i )
        i *= 5
    return zeros



if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter number: "))
        except ValueError:
            print("Value must be a number")
        except KeyboardInterrupt:
            print()
            break
        else:
            if num >= 0:
                fact = factorial(num)
                print("%i! = %i" % (num, fact))
                zeros = compute_zeroes(num)
                print("Number of Trailing Zeroes: %i" % zeros)
            else:
                print("Number must be positive")
            