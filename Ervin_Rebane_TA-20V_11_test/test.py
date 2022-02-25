#C:/Users/margu/Documents/GitHub/python-algajatele/11_test_of_input_output_arrays_conditionals/contacts.txt
# this function removes spaces and new lines for column from right and left

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
  def print_out_database(db, k):
      print("\n\nIndex \t Name \t\t Phone \t\t Age \t Email")
      mAge = 0
      for i in range(0, len(db)):
          row = db[i]
          print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")
          mAge +=int(row[2])
      if k==0: print("Medium age: ", round(mAge/len(db), 1), "\n") # Prints Medium age out of all users


  def List_u(k):
      db = read_database()
      print_out_database(db, k)
      
  
      
  def Add_u():
      uN= str(input("\tEnter the Name :"))
      uP= str(input("\tEnter the Phone:"))
      uA= str(input("\tEnter the Age :"))
      uE= str(input("\tEnter the Email :"))
      row = []
      row.append(uN)
      row.append(uP)
      row.append(uA)
      row.append(uE)
      db.append(row)
      write_database(db)
      print("User Added!")
      
  def Edit_u(db):
    while(True):
      try:
        uI = int(input("Enter the User index to edit: "))
        if(len(db) <= uI or uI < 0):
            print("Out of index.")
            continue
        else: break
      except:
        print("Please enter a number.")
        continue
    
    u = db[uI] #saving the selected row
    print(u, "\n")
    
    print("What you want to change?")
    while(True):
      Sel = input("Enter 'name', 'phone', 'age', 'email':")
      if (Sel != "name" and Sel != "number" and Sel != "age" and Sel != "email"):
        print("Please choose one of the valid options.")
        continue
      else: break
    
    if (Sel == 'name'):
      uN = input("Enter new name: ")
      u[0] = uN
    elif (Sel == 'number'):
      uP = input("Enter new number: ")
      u[1] = uP
    elif (Sel == 'age'):
      uA = input("Enter new age: ")
      u[2] = uA
    elif (Sel == 'email'):
      uE = input("Enter new email: ")
      u[3] = uE
    
    db[uI] = u
    write_database(db)
    print("User Changed!")

  def Rem_u(db):
    List_u(5)
    while(True):
        try:
            uI = int(input("\tEnter the User index to delete:"))
            if(len(db) <= uI or uI < 0): print("Out of index.")
            else:
                if (confirm("delete this user?")) == 2:
                    return False
                break
        except:
            print("Please enter a number.")
    
    db.pop(uI)
    write_database(db)
    print("User Removed!")
        


  def confirm(qq):
      iam_sure= str(input("\tYou want to "+qq+" (y/n)")) # Are you shure?
      if iam_sure == "y":
          print("picked '"+iam_sure+"'")
          return 1
      else:
          print("no? ok")
          return 2 
        
        
  print("\n\nCommands are:")
  print("1. list users")
  print("2. edit user")
  print("3. add user")
  print("4. remove user")
  print("5. exit")
  db = read_database()
  present_com = 9

  while present_com not in ['1', '2', '3', '4', '5']:
      present_com = input("\tWhat is your command?[1, 2, 3, 4, 5] : ")
        
  if (present_com == "1"): List_u(0)
  if (present_com == "2"): Edit_u(db)
  if (present_com == "3"): Add_u()
  if (present_com == "4"): Rem_u(db)
  if (present_com == "5"):
        if (confirm("exit now?")) == 1:
            return False


    
  continue

contacts_task()
