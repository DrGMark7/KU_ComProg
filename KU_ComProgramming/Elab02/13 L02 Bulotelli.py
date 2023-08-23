if "n" == input("Is Bulotelli injured?(y/n) "):
    if "n" == input("Is Bulotelli late for the training?(y/n) "):
        print("Starter")
        exit()
    else:
        if "n" == input("Did Bulotelli perform well in training?(y/n) "):
            print("Not selected")
            exit()
        else:
            print("Substitute")
            exit()
else:
    print("Not available")