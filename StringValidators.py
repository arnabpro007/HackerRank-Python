def StringValidator(String):
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    i = 0
    while(i<len(String) and alnum == False):
        alnum = String[i].isalnum()
        i = i + 1
    i = 0
    while(i<len(String) and alpha == False):
        alpha = String[i].isalpha()
        i = i + 1
    i = 0
    while(i<len(String) and digit == False):
        digit = String[i].isdigit()
        i = i + 1
    i = 0
    while(i<len(String) and lower == False):
        lower = String[i].islower()
        i = i + 1
    i = 0
    while(i<len(String) and upper == False):
        upper = String[i].isupper()
        i = i + 1
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

def main():
    String = input("Enter your String: ")
    StringValidator(String)

if __name__ == '__main__':
    main()
    