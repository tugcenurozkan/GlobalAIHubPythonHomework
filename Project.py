firstnames=("ali","veli","zeynep","lale","ömer","ezgi")
lastnames=("yıldız","kahraman","gümüş","demir","cengiz","mola")
print("                                    !!!YOU SHOULD ENTER LOWER LETTER!!!")
def course_kontrol():               
    if (course_list.count("")>2):  #boşluk sayısı 2 den fazla olamaz 2 ye eşit olabilir/ 3 dersten az alamaz
        return ("You Failed in Class")
    

def control():    #isim kontolü için
    for i in range(len(firstnames)):
        if(i_firstname==firstnames[i] and i_lastname==lastnames[i] and lastnames.index(i_lastname)==firstnames.index(i_firstname)):
            return ("Welcome")
   
#İsim girişi kontrolü           

t=0
for k in range(3):

    i_firstname=input("Please Enter Your First name:")
    i_lastname=input("Please Enter Your Last Name:")

    if not (control()) :
        if(t<2):
            print("Try Again!")
        else:
            print("Please Try Again Later!!!")
            exit()
        t+=1
    else:
        print(control())
        break

#kurs listesi düzenlemesi

course_list=[]
for i in range(5):
    courses=input("Please Enter Your Courses:")
    course_list.append(courses)
print()
print("Courses List ->>",course_list)


#3 den az ders almaması koşulu kontrolü (yukarda fonksiyon tanımlanmıştı) alıyorsa hata basıyor ekrana 

print(course_kontrol())

print()
#kurs notlarını kullanıcıdan alıp karşılaştırma
print("Please Enter Your Notes Of", course_list[0] ,"Course" )  

midterm=int(input("Please Enter Your Midterm Note:"))
final=int(input("Please Enter Your Final Note:"))
project=int(input("Please Enter Your Project Note:"))


notes_dictionary={}
notes_dictionary['midterm']=midterm
notes_dictionary['final']=final
notes_dictionary['project']=project

print()
print("Student's Notes ->>",notes_dictionary)  #ödevde istenilen dictionary görünümü
print()
grades=notes_dictionary["midterm"]*0.3+notes_dictionary["final"]*0.5+notes_dictionary["project"]*0.2
print("Student's Course Passing Grade ->>",grades)

print()

print("COURSE PASSING GRADE BY LETTER->>")

if(grades>=90):
    print("AA")
elif(70<=grades<90):
    print("BB")
elif(50<=grades<70):
    print("CC")
elif(30<grades<50):
    print("DD")
else:
    print("FF")
    print("Your Grades Is:",grades,"And You Take FF. This Is Failure..")

print()



