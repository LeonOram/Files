##def get_test_results():
##    test_results = []
##    for test in range(3):
##        test_results.append(int(input("Please enter a score: ")))
##    return test_results

def average_test_result(results):
    total = 0
    for test in results:
        test=int(test)
        total += test
    average = total/len(results)
    return average

def display_average_result(average):
    print("your average test result is: {0}".format(average))



def main():
    with open("test_data.txt",mode="r",encoding="utf-8") as test_file:
    #test_results = get_test_results()
        test_results=[]
        for line in test_file:
            test_results.append(line)
    average = average_test_result(test_results)
    display_average_result(average)

if __name__ == "__main__":
    main()
