def split_and_join(line):
    temp = line.split(" ") #We are splitting based on spaces
    temp = "-".join(temp) #we are adding the elements here with - 
    return temp

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)