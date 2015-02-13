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
    return names

def get_target():
    target = input("Pleade enter the name to search for: ")
    return target

def main():
    target = get_target()
    names = get_data()
    found,found_at = search(names,target)
    if found == True:
        print("{0} was found at index {1}".format(target,found_at))
    else:
        print("{0} was not found".format(target))

main()
