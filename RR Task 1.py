with open("students.txt",mode="r",encoding="utf-8") as file:
    for count,line in enumerate(file):
        print("{0}. {1}".format(count+1,line),end='')
