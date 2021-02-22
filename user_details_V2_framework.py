def films():
    temp = []
    # n = 0
    cont = True
    while cont is True:
        film = input("What is a favourite film of yours? ")
        temp.append(film)
        carry = input("Any more? (Y/N) ")
        if carry.lower() == "y":
            continue
        else:
            cont = False
    return temp


print(films())