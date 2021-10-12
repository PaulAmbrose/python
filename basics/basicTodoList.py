newList = []

def printItems(list):
    print("Your list contains...\n")
    for items in list:
        print(items)

def listItemNumber():
    print("Your list contains " + str(len(newList)) + " item(s)")

def addOrRemoveItem():
    addOrRemove = input("A = add items, B = remove items, C = print list items >> ")
    if addOrRemove == "A":
        newItem = input("Add >> ")
        newList.append(newItem)
    elif addOrRemove == "B":
        print("Remove an item")
        removeItem = input("Remove >> ")
        newList.remove(removeItem)
    elif addOrRemove == "C":
        print(newList)
    else:
        print("Invalid selection \n")

def main():

    listItemNumber()
    addOrRemoveItem()
    main()
main()