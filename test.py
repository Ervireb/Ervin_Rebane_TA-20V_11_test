#C:/Users/margu/Documents/GitHub/python-algajatele/11_test_of_input_output_arrays_conditionals/contacts.txt
# this function removes spaces and new lines for column from right and left

# Sorry not fully finished yet, mind if i give it back later?
# TODO: Add ask for do u want to exit w/o save
def contacts_task():
    while (True):
        def strip(string):
            return string.strip()


        # this function reads database from contacts.txt file
        def read_database():
            file = open("contacts.txt", encoding="utf-8")
            rows = []
            for row in file:
                rows.append(list(map(strip, row.split(", "))))
            return rows

        # this function writes contacts to file
        def write_database(db):
            file = open("contacts.txt", mode="w", encoding="utf-8")
            rows = []
            for row in db: 
                rows.append(", ".join(row))
            file.write("\n".join(rows))
            file.close()

        # this function prints all contacts from db that is in memory
        def print_out_database(db):
            print("Index \t Name \t\t Phone \t\t Age \t Email")
            for i in range(0, len(db)):
                row = db[i]
                print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")

        def List_u():
          db = read_database()
          print_out_database(db)
          
        #================================================================================================================
        #================================================================================================================

        def Add_u():
            uIndex= str(input("Enter the Index of the User:"))
            uName= str(input("Enter the Name of the User:"))
            uPhone= str(input("Enter the Phone of the User:"))
            uAge= str(input("Enter the Age of the User:"))
#             if uAge== "": uAge="2021.1.1"
            uEmail= str(input("Enter the Email of the User:"))
            
            print("You entered: ")
            print("uIndex="+uIndex)
            print("uName="+uName)
            print("uPhone="+uPhone)
            print("uAge="+uAge)
            print("uEmail="+uEmail)

#             Software sw = new Software()
#             {
#                 Name = Uname,
#                 Version = UVersion,
#                 Developer = UDeveloper,
#                 InstallDate = Convert.ToDateTime(UInstallDate),
#                 User = UUser
#             };

 
        def confirm(qq):
            iam_sure= str(input("You want to "+qq+" (y/n)")) # Are you shure?
            if iam_sure == "y":
                print("picked '"+iam_sure+"'")
                return 1
            else:
                print("no? ok")
                return 2 #its wrong for now
#             print("a") if iam_sure == "y" else return 1 #its wrong for now
            
            
          
#         def print_out_commands():
        print("\n\nCommands are:")
        print("1. list users")
        print("2. edit user")
        print("3. add user")
        print("4. exit")
        present_command = 9

        while present_command not in [1, 2, 3, 4]:
            present_command = int(input("What is your command? [1, 2, 3, 4]: "))
            
        if present_command == 1: List_u()
        if present_command == 2: print("2")
        if present_command == 3: Add_u()
        if present_command == 4:
#             confirm("exit w/o save?")
#             print("okNext")
            if (confirm("exit now?")) == 1:
                return False


        
        continue
    
contacts_task()