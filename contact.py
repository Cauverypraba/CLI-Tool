import json

# Read data from JSON file
with open('data.json', 'r') as store:
    data = json.loads(store.read())
store.close()

def modify(data):
    """
    Method to modify information in JSON file 
    """
    with open('data.json', 'w') as file:
        file.write(data)
        file.close()    

print("----------Welcome to CLI Tool for managing contacts-----------")        
print("Choose any one of the options \n 1. Create contacts\n 2. Search a contact\n 3. View all")

input_option = int(input())

# Create contact when user selects option: 1
if input_option == 1:
    name = input("Enter contact name : ")
    number = input("Enter contact number : ")
    email = input("Enter email : ")
    insert_data = {'name': name,'number': number,'email': email}
    if name == "":
        print("Error: name field can't be empty")
    else:
        data += [insert_data]
        modify(json.dumps(data))   
        print("Information added successfully!!")
# Search for a contact if user selects option: 2
elif input_option == 2:
    name = input("Enter contact name : ")
    for info in data:
        if name.lower() in info["name"].lower():
            print("Name: "+info["name"]+"\nTelephone: "+info["number"]+"\nEmail: "+info["email"])
            print("Do you want to update or delete this contact? y/n")
            ch = input()
            if ch == 'y':
                print("Choose any one 1. Update the contact 2. Delete the contact")
                input_modify_option = int(input())
                # Update the contact with data provided by user
                if input_modify_option == 1:
                    print("Leave empty to be unchange")
                    number = input("Enter mobile number: ")
                    email = input("Enter Email address: ")

                    # Form a dict to be modified
                    insert_data = {"name":info["name"], "number":number, "email":email}

                    # Iterate through each keys and change values of contact provided by user
                    for key in insert_data.keys():
                        if insert_data[key] != "":
                            info[key] = insert_data[key]
                    modify(json.dumps(data))
                    print("Contact modified successfully!!")
                # Delete the contact with user confirmation
                elif input_modify_option == 2:
                    print("Are you sure to delete the contact? y/n")
                    confirm_delete = input()
                    if confirm_delete == 'y':
                        data.remove(info)
                        modify(json.dumps(data))    
                        print("Contact deleted successfully!!")
# Display all the contacts if user selects option: 3
elif input_option == 3:
    for info in data:
        print("Name: "+info["name"]+"  Telephone: "+info["number"]+"  Email: "+info["email"])
