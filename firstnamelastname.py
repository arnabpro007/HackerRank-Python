def print_full_name(first_name,last_name):
    temp = "Hello " + first_name + " " + last_name + " ! You just delved into python."
    print(temp) 

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print_full_name(first_name,last_name)


if __name__ == '__main__':
    main()
    