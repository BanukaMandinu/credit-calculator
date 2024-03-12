print("""---------------------------------
           Wellcome!!
---------------------------------""")
#Data of part 1
progress = []
trailer = []
retriver = []
exclude = []
valid_range = range(0, 121, 20)

#Data of part 2
data = []

def menu():
    while True:
        try:
            while True:
                global pass_mark
                pass_mark = int(input("\nPlease enter your credits at pass: "))
                if not pass_mark in valid_range:
                    print("Out or range!\n")
                else:
                     break
        except ValueError:
            print("Integer required!\n")
        else:
            break
    while True:
        try:
            while True:
                global defer_mark
                defer_mark = int(input("Please enter your credits as defer: "))
                if not defer_mark in valid_range:
                    print("Out or range!\n")
                else:
                    break
        except ValueError:
            print("Integer required!\n")
        else:
            break
    while True:
        try:
            while True:
                global fail_mark
                fail_mark = int(input("Please enter your credits at fail: "))
                if not fail_mark in valid_range:
                    print("Out or range!\n")
                else:
                    break
        except ValueError:
            print("Integer required!\n")
        else:
            break
    check()

def con():
    while True:
        print("\nWould you like to enter another set of data?")
        option = input("Enter 'Y' for yes or 'q' to quit and viwe results: ")
        if option == 'y': 
            menu()
            break
        if option == 'q':
            Histogram() 
            break
        else:
            print("Invalid input!")
        
def check(): #PASS/DEFER/FAIL Check
    if pass_mark + defer_mark + fail_mark != 120:
        print("Total incorrect!")
        menu()    
        
    elif pass_mark ==120 and defer_mark == 0 and fail_mark == 0:
        print("Progress.")
        progress.append("Progress")
        enter1 = "Progress - " + str(pass_mark) +', ' + str(defer_mark) +', '+ str(fail_mark)
        data.append(enter1)
        con()
        
    elif pass_mark == 100 and 0 <= defer_mark <= 20 and 0 <= fail_mark <= 20:
        print("Progress(module trailer).")
        trailer.append("Trailer")
        enter1 = "Progress(module trailer) - " + str(pass_mark) +', ' + str(defer_mark) +', '+ str(fail_mark)
        data.append(enter1)
        con()
        
    elif 0 <= pass_mark <=80 and 0 <= defer_mark <=120 and 0 <= fail_mark <= 60:
        print("Do not progress - module retriever. ")
        retriver.append("Retriver")
        enter1 = "Retriver - " + str(pass_mark) +', ' + str(defer_mark) +', '+ str(fail_mark)
        data.append(enter1)
        con()
        
    elif 0 <= pass_mark <=40 and 0 <=defer_mark <= 40 and 80 <= fail_mark <= 120:
        print("Exclude.")
        exclude.append("Exclude")
        enter1 = "Exclude - " + str(pass_mark) +', ' + str(defer_mark) +', '+ str(fail_mark)
        data.append(enter1)
        con()

def Histogram():
    print("---------------------------------------------------------------")
    print("Histogram")
            
    print('Progress',len(progress),' : ', len(progress) * '*' )
    print('Trailer', len(trailer),'  : ',len(trailer) * '*' )
    print('Retriver', len(retriver),' : ',len(retriver) * '*')
    print('Exclude',len(exclude),'  : ', len(exclude)* '*')

    outcomes = len(progress) + len(trailer) + len(retriver) + len(exclude)
    print()
    print(outcomes,"outcomes in total")
    print("---------------------------------------------------------------")
  
def text_file():
    print("part 3: ")
    for item1 in data:
        print(item1)
    f = open('Textfile.txt','a')
    for item1 in data:
        f.write(item1)
        f.write('\n')
    f.close()
    print("\nThe data has enterd to the Textfile.txt\n")
                            
menu()
text_file()
