import json

def Register_Login():

        reg_log = int(input("Enter your choice: \n[1] Register \n[2] Login \n ->"))   
        while True:
            if reg_log == 1:
                print("REGISTER")
                adminname = (input("Enter Admin Name: "))
                adminpassword = (input("Enter Password: "))
                
                AdminData = {adminname: adminpassword}

                with open("Database/AdminDataBase.json", "a") as AdminDatabases:
                    json.dump(AdminData, AdminDatabases, indent=4)
                Register_Login()
                break
            elif reg_log == 2:
                pass
    
            else:
                print("Invalid Input!")
                