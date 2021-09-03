def hcf_or_gcd(a, b):
    try:
        if (b == 0):
            return a
        else:
            return hcf_or_gcd(b, a % b)
    except Exception as error:
        print("there are some warnings", error)

while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
    except Exception as err:
        print("Please enter a number")
    else:
        if(a < 0 or b < 0):
            print("Enter a positive number")
        else:
            print(hcf_or_gcd(a, b))
            break
