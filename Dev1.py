import pickle
class people:
    def __init__(self):
        self.name=None
        self.dob=None

def get_people():
    con=True
    people_list=[]
    while con == True:
        name = input("Please enter Name: ")
        if name != "":
            person = people()
            person.name=name
            dob = input("Please enter DoB (DD/MM/YYYY): ")
            person.dob = dob
            people_list.append(person)
        else:
            con=False
    return people_list

def write_to_file(people_list):
    with open("People.dat",mode="wb") as people_file:
        pickle.dump(people_list,people_file)

def main():
    people=get_people()
    write_to_file(people)

main()

