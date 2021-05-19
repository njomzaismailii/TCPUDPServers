import socket
from datetime import date
import random
from math import pi

serverName = 'localhost'
serverPort = 14000
uServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
uServer.bind((serverName, serverPort))
print("Serveri eshte duke pritur kerkesen nga klienti!")


#Metoda IP
def IP(word):
    x="ip adresa eshte: ",word[0]
    return x

#Metoda NRPORTIT
def NRPORTI(word):
    x="nr portit eshte: ", word[1]
    return x

#Metoda NUMERO
def NUMERO(word):
      vowels=0
      consonants=0
      for i in word:
       if i in ['a', 'e','i', 'o', 'u','y','ë' ,'A', 'E','I', 'O', 'U','Y','Ë']:
            vowels=vowels+1
       else:
        consonants=consonants+1 
       break    
      y="Numri i zanoreve:"+ str(vowels) + "Numri i bashketingelloreve:"+str(consonants)
      return y

#metoda reverse
def ANASJELLTAS(word):
      str2 = word[::-1]
      return str2

#metoda palindrom
def PALINDROM(word): 
      word = word.casefold()
      rev_word=reversed(word)
      if list(word) == list(rev_word):
         y="Fjala eshte palindrom"
         return y
      else:
         y="Fjala nuk eshte palindrom"
         return y


#metoda koha
def KOHA():
     today=date.today()
     day=today.strftime("%d/%m/%Y")
     return day

#metoda loja 
def LOJA():
      mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
                19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
      x = random.sample(mylist,5)
      x=sorted(x)
      y= "Numra te cfardoshem te rangut:", str(x)
      return y

#metoda GCF
def GCF (num1, num2):
      if num1>num2:
        num1, num2 =num2, num1   
      for x in range (num1, 0, -1):
        if num1 % x==0 and num2%x==0:
            return "numri GCF: ", x


# Metoda CentimetertoInches 
def KONVERTO(num):
      inc = num/2.54  # 1 inch = 2.54 centimeters
      y="Cm to Inch: ", inc
      return y


##Metoda e pare shtese
def NUMRI(num):
      n1 = int( "%s" % num )
      n2 = int( "%s%s" % (num, num) )
      n3 = int( "%s%s%s" % (num, num, num) )
      num1="n+nn+nnn= "+ str(n1+n2+n3)
      return num1


##Metoda e dyte shtese
def SYPRINA(num):    
     y="Siperfaqja e rrethit me rreze " + str(num) + " eshte: " + str(pi * num*2)
     return y



while True:
        request,address=uServer.recvfrom(128)
        request = request.upper()
        request = request.decode()
        text = request.split(" ")
        print('Te dhenat nga klienti:' + request)
        if text[0] == "IP":
         mesazhi = str(IP(address))
         uServer.sendto(str.encode(mesazhi),address)

        elif text[0] == "NRPORTI": 
         mesazhi = str(NRPORTI(address))
         uServer.sendto(mesazhi.encode(),address)

        elif text[0] =="NUMERO" :
         mesazhi = str(NUMERO(request[len(text[0]):len(request)]))
         uServer.sendto(mesazhi.encode(),address)

        elif text[0] =="ANASJELLTAS" :
         mesazhi = str(ANASJELLTAS(request[len(text[0]):len(request)]))
         uServer.sendto(mesazhi.encode(),address)

        elif text[0] =="PALINDROME" :
         mesazhi = str(PALINDROM(text[1]))
         uServer.sendto(mesazhi.encode(),address)

        elif text[0] == "KOHA" :
         mesazhi = str(KOHA())
         uServer.sendto(mesazhi.encode(),address)

        elif text[0] == "LOJA" :
         mesazhi = str(LOJA())
         uServer.sendto(mesazhi.encode(),address)
      
        elif text[0] == "GCF" :
          try:
           mesazhi = str(GCF(int(text[1]),int(text[2])))
          except Exception:
           mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden GCF dhe dy numra per te realizuar metoden."
           uServer.sendto(mesazhi.encode(),address)

        elif text[0] == "KONVERTO" :
          try:
           mesazhi = str(KONVERTO(int(text[1])))
          except Exception :
           mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden Konverto dhe nje numer te plote."
           uServer.sendto(mesazhi.encode(),address)
  
        elif text[0]=="NUMRI":
                try:
                        mesazhi=str(NUMRI(int(text[1])))
                except Exception:
                        mesazhi = "ka ndodhur nje gabim ju lutem shkruani NUMRI dhe nje numer"  
                        uServer.sendto(mesazhi.encode(),address)

        elif text[0]=="SYPRINA":
                try:
                        mesazhi=str(SYPRINA(int(text[1]))) 
                except Exception:
                        mesazhi="ka ndodhur nje gabim ju lutem shkruani SYPRINA dhe nje numer per rrezen e rrethit "     
                        uServer.sendto(mesazhi.encode(),address)

        elif text[0]=="EXIT":
                    break
        print("Komunikimi perfundoi!")
        