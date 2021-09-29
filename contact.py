import json

with open('data.json', 'r') as store:
    data = json.loads(store.read())
store.close()

def modify(data):
    with open('data.json', 'w') as file:
        file.write(data)
        file.close()    

print("----------Welcome to CLI Tool for managing contacts-----------")        
print("Choose any one of the options \n 1. Create contacts\n 2. Search a contact\n 3. View all")

i = int(input())
if i == 1:
    name = input("Enter contact name : ")
    number = input("Enter contact number : ")
    email = input("Enter email : ")
    obj = {'name': name,'number': number,'email': email}
    if name == "":
        print("Error: name field can't be empty")
    else:
        data += [obj]
        modify(json.dumps(data))    
        print("Information added successfully!!")

elif i == 2:
    name = input("Enter contact name : ")
    for x in data:
        if name.lower() in x["name"].lower():
            print("Name: "+x["name"]+"\nTelephone: "+x["number"]+"\nEmail: "+x["email"])
            print("Do you want to update or delete this contact? y/n")
            ch = input()
            if ch == 'y':
                print("Choose any one 1. Update the contact or 2. Delete the contact")
                input1 = int(input())
                if input1 == 1:
                    print("Leave empty to be unchange")
                    number = input("Enter mobile number: ")
                    email = input("Enter Email address: ")
                    obj = {"name":x["name"],"number":number,"email":email}
                    for j in obj.keys():
                        if obj[j]!="":
                            x[j]=obj[j]
                    modify(json.dumps(store))


