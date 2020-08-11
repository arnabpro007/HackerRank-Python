def StringTraversal(string,substring):
    temp = 0
    for i in range(len(string)-len(substring)+1):
        if string[i:(i+len(substring))] == substring:
            temp = temp + 1
    return temp


def main():
    string = input("Enter your Main string:")
    substring = input("Enter the substring: ")
    temp = StringTraversal(string,substring)
    print(temp)
if __name__ == '__main__':
    main()
    