import pickle
class people:
    def __init__(self):
        self.name=None
        self.dob=None
        
def search(list_,is_in):
    found = False
    found_at = ""
    count = 0
    while not found and count < len(list_):
        if list_[count] == is_in:
            found_at = count
            found = True
        count = count+1
    return found,found_at

def get_data():
    with open("people.dat",mode="rb") as people_file:
        people = pickle.load(people_file)
    names=[]
    for person in people:
        names.append(person.name)
    return names,people

def get_target():
    target = input("Pleade enter the name to search for: ")
    return target

def copy_destroy(people,index):
    new_list = []
    for count,person in enumerate(people):
        if count != index:
            new_list.append(person)    
    with open("people.dat",mode ="wb") as people_file:
        pickle.dump(new_list,people_file)
        


def main():
    target = get_target()
    names,people = get_data()
    found,found_at = search(names,target)
    if found == True:
        copy_destroy(people,found_at)
    else:
        print("{0} Was not found".format(target))

main()
