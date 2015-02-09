with open("New_File.txt",mode="w",encoding="utf-8") as file:
    cont = True
    while cont == True:
        name = input("Please enter the next name(-1 to quit): ")
        if name != "-1":
            file.write("{0}\n".format(name))
        else:
            cont = False
        
