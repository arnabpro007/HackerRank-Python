def mutate_string(string,position,character):
    temp = string[:position] + character + string[(position + 1):]
    return temp


def main():
    s = input("Enter your String: ")
    i,c = input().split(" ")
    s_new = mutate_string(s,int(i),c)
    print(s_new)
    
if __name__ == '__main__':
    main()
    