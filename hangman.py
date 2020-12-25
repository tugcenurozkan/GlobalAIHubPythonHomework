#SIMPLE HANGMAN GAME
"""kelimedeki harf sayısı kadar tahmin hakkınız var ve tahmin ettiğiniz harfler doğruysa ve tekrar kullandıysanız
 -warning: you already guess the letter-
 şeklinde uyarı veriyor.Eğer zaten doğru tahmin edilmemişse ve tekrar tekrar aynı harfi giriyorsanız -invalid value- basıyor ekrana"""
import random
print()
user_name=input("PLEASE ENTER YOUR USER NAME:")
print()
print("WELCOME {}".format(user_name).upper(),"\n")

def get_word():
    words = ['çilek','armut','elma','muz','ananas','kereviz','sarımsak','brokoli','pırasa','ıspanak','ayva','kivi','fındık','ceviz','fıstık','kahve','çay','domates','salatalık','marul','kekik','kimyon']
    return random.choice(words)

word = get_word()
# print(word) hangi kelimenin random seçildiğini görerek kodun doğruluğunu test etmek için ekrana yazdırıp görebilirsiniz.
letter=list(word)   #burda seçilen kelime liste içine atılıp harflerin index ile alınmasını sağlamakta

word_progress = ["-"] * len(letter)   #kelime uzunluğu kadar "-" yi yeni bir liste içine attık bu şekilde ilerleme gözlemlenebilecek
print("THIS IS RANDOM WORD AND IT HAS",len(letter),"LETTER -->>",word_progress)  #başlangıçta görsellik açısında yazdırıldı.

print()

guessed_letter=[]  #daha önce tahmin edilenler "guessed_letter" listesinde saklansın(uyarı vermek için)

for i in letter:
	
    user_letter=input("PLEASE ENTER YOUR GUESS LETTER (LOWER CASE):")
    print()
    if user_letter in letter:
		
        if not user_letter in guessed_letter:  
                # print("YOUR GUESS IS TRUE", "-->")
                # index=letter.index(user_letter)
                # letter[index]=user_letter
                # print(letter[index])

            for j in range(len(letter)):  #random kelime üzerinde gezinmesi gerektiği için bu kelimenin uzunluğu baz alındı
                if word_progress[j] == "-" and letter[j] == user_letter:   #bu aşamada girilen kelime random seçilen kelime listesindeyse ve o kısım word_progress de "-"(aynı index dahilinde) ise "-" yerine artık girilen harfi koy
                    word_progress[j] = letter[j]							

            guessed_letter.append(user_letter)
            print("\n","THIS IS RANDOM WORD -->>",word_progress,"\n")
           
			
            if not '-' in word_progress:
               print("\n","YOU WIN THE GAME!!!","\n")
               break

        else:
            print("\n","WARNING:YOU ALREADY GUESS THE LETTER!!!","\n")   

    else:
        print ("\n","INVALID LETTER","\n")
    
if '-' in word_progress:
	print("\n","SORRY.. YOU KILLED THE MAN :/","\n")
	print("RANDOM WORD IS ->>",word.upper(),"\n")


	


    
