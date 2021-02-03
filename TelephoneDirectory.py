direc_dict={}

x=1
while x==1:
    special_information_dict={}
    phone=[]
    mail = []
    city = []
    person=input("Please write the name and surname of the person you want to add to the directory:")
    if person not in direc_dict.keys():
        x=3
        while x==3:
            phone_num=input("Please enter the person's phone number:")
            phone.append(phone_num)

            eMail = input("Please enter the person's e-mail:")
            mail.append(eMail)

            cityInfromation=input("Please enter the person's city informations:")
            city.append(cityInfromation)
            x=int(input("Enter 1 for new contact and 2 for Exit."))


        for i in range(len(phone)):
            special_information_dict["phone number"]=phone[i]
            special_information_dict["e-mail"] = mail[i]
            special_information_dict["city"] = city[i]
        direc_dict[person]=special_information_dict
    else:
        print("The person is in the directory!")
print("Contacts are as follows:")
for k in direc_dict.keys():
    print(k)

y=2
while y==2:
    isim=input("Please enter the name and surname of the person whose information you want to learn as in the directory:")
    if isim not in direc_dict:
        print("This name is not in the directory, please try again.")
        continue

    y=1
    while y==1:
        m=input("Write 'phone number' for the person's phone number, 'e-mail' for her/his e-mail, 'city' for city information, and 'all' for all information.")
        if m=="phone number":
            print(isim,"isimli kişinin telefon numarası =>", direc_dict[isim][m])
        elif m=="e-mail":
            print(isim, "isimli kişinin e-postası =>", direc_dict[isim][m])
        elif m=="city":
            print(isim, "isimli kişinin bulunduğu şehir =>", direc_dict[isim][m])
        elif m=="all":
            print(isim, "isimli kişinin bilgileri", direc_dict[isim])
        else:
            print("You entered incorrect data, please try again.")
            continue
        y=int(input("Click 1 to access the other information of the same person, 2 to switch to a new person, 3 to exit."))
print("Logging out ...")


