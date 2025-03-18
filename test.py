def askname ():
    persons_name = input("What is your name? ")
    name_list.append(persons_name)
def printname ():
    print(f"The name is (name_list{0})")
name_list = []
askname()
print()