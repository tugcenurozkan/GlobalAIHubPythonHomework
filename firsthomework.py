#KULLANICIDAN ALINAN VERİNİN ÇIKTISI VE TÜRÜNÜ VEREN PROGRAM
mylist=[]
num=0
while num<5:
     x= input("Enter a thing: ")
     mylist.append(x)
     num+=1

print(mylist)
number=0

for i in mylist:

 try:
   number==int (i)
   print (f'input:{i}','/','type is integer')
         
 except ValueError:  
  print('input {}'.format(i),'/','type is string')
  

  

     
