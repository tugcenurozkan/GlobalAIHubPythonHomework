#KULLANICIDAN BİLGİLERİNİ İSTE VE EKRANA YAZDIR İF İLE KOŞUL BİLDİR
firstname=input("Please write your firstname:")
lastname=input("Please write your lastname:")
dateOfBirth=int(input("Please write your birth year:"))
age=int(input("Please your age:"))

userinfo=[]
userinfo.append(firstname)
userinfo.append(lastname)
userinfo.append(dateOfBirth)
userinfo.append(age)

print("\n")

print("User's information:")

for i in userinfo:
  print(i)

print("\n")

if age<18:
    print("You can't go out  because it's too dangerous.")

else:
    print("You can go out to the street.")

print("\n")

