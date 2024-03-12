print("""---------------------------------
           Wellcome!!
---------------------------------""")
ids = {}
valid_range = range(0, 121, 20)
 
def menu():
    while True:   
        try:
            global id_num
            id_num = input("\nPlease enter your UOW id: ")
            stdid = id_num[1:8]
            int(str(stdid))
            if not (id_num[0]) == 'w':
                print("Invalid ID! \nYou must have 'w' as the  frist character. \n")
            elif not len(id_num)==8:
                print("Invalid input! \nYou must have Eight characters. \n")
            elif id_num in ids:
                print("Invaid! You have entered the same id TWICE!\n")
            else:
                break
        except:
            print("Your UOW id must be in this form,\neg:w1234567")
    while True:
        try:
            while True:
                global pass_mark
                pass_mark = int(input("Please enter your credits at pass: "))
                if not pass_mark in valid_range:
                    print("Out or range.\n")
                else:
                     break
        except ValueError:
            print("Integer required\n")
        else:
            break
    while True:
        try:
            while True:
                global defer_mark
                defer_mark = int(input("Please enter your credits as defer: "))
                if not defer_mark in valid_range:
                    print("Out or range.\n")
                else:
                    break
        except ValueError:
            print("Integer required\n")
        else:
            break
    while True:
        try:
            while True:
                global fail_mark
                fail_mark = int(input("Please enter your credits at fail: "))
                if not fail_mark in valid_range:
                    print("Out or range.\n")
                else:
                    break
        except ValueError:
            print("Integer required\n")
        else:
            break
    check()

def con():
    while True:
        print("Would you like to enter another set of data?")
        option = input("Enter 'Y' for yes or 'q' to quit and viwe results: ")
        if option == 'y': 
            menu()
            break
        elif option == 'q':
            dic() 
            break
        else:
            print("Invalid input!\n")

def check():   
    if pass_mark + defer_mark + fail_mark != 120:
        print("Total incorrect\n")
        menu()    
        
    #PASS/DEFER/FAIL Check
    elif pass_mark ==120 and defer_mark == 0 and fail_mark == 0:
        print("Progress.\n")
        ids[id_num] = ": Progress - " + str(pass_mark) +', '+ str(defer_mark) +', '+ str(fail_mark)
        con()
        
    elif pass_mark == 100 and 0 <= defer_mark <= 20 and 0 <= fail_mark <= 20:
        print("Progress(module trailer).\n")
        ids[id_num] = ": Progress(module trailer) - " + str(pass_mark) +', '+ str(defer_mark) +', '+ str(fail_mark)
        con()
        
    elif 0 <= pass_mark <=80 and 0 <= defer_mark <=120 and 0 <= fail_mark <= 60:
        print("Do not progress - \n ")
        ids[id_num] = ": Do not progress - module retriever -  " + str(pass_mark) +', '+ str(defer_mark) +', '+ str(fail_mark)
        con()
        
    elif 0 <= pass_mark <=40 and 0 <=defer_mark <= 40 and 80 <= fail_mark <= 120:
        print("Exclude.\n")
        ids[id_num] = ": Exclude - " + str(pass_mark) +', '+ str(defer_mark) +', '+ str(fail_mark)
        con()
    
def dic():
    print()
    for x,y in ids.items():
        print(x,y)
    
menu()
