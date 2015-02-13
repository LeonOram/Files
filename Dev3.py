import pickle
class people:
    def __init__(self):
        self.name=None
        self.dob=None

def open_file():
    with open("people.dat",mode="rb") as people_file:
        people = pickle.load(people_file)
    return people



def get_max_len(people):
    max_len = 0
    for person in people:
        if len(person.name) > max_len:
            max_len = len(person.name)
    return max_len

def write_table(people,name_max):
    for person in people:
        print("-"*(name_max + 13))
        print("|{0:<{1}}|{2:<10}|".format(person.name,name_max,person.dob))
    print("-"*(name_max + 13))

def main():
    people = open_file()
    max_len = get_max_len(people)
    write_table(people,max_len)
main()
