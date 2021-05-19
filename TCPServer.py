import socket
from datetime import date
import random
import threading
from math import pi

# Metoda IP


def IP(word):
    x = "ip adresa eshte: ", word[0]
    return x

# Metoda NRPORTIT


def NRPORTI(word):
    x = "nr portit eshte: ", word[1]
    return x

# Metoda NUMERO


def NUMERO(word):
    vowels = 0
    consonants = 0
    for i in word:
        if i in ['a', 'e', 'i', 'o', 'u', 'y', 'ë', 'A', 'E', 'I', 'O', 'U', 'Y', 'Ë']:
            vowels = vowels+1
        else:
            consonants = consonants+1
        y = "Numri i zanoreve eshte " + \
            str(vowels) + "dhe numri i bashketingelloreve eshte "+str(consonants)
        return y

# metoda reverse


def ANASJELLTAS(word):
    str2 = word[::-1]
    return str2

# metoda palindrom


def PALINDROM(word):
    word = word.casefold()
    rev_word = reversed(word)
    if list(word) == list(rev_word):
        y = "Fjala eshte palindrom"
        return y
    else:
        y = "Fjala nuk eshte palindrom"
        return y


# metoda koha
def KOHA():
    today = date.today()
    day = today.strftime("%d/%m/%Y")
    return day

# metoda loja


def LOJA():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    x = random.sample(mylist, 5)
    x = sorted(x)
    y = "Numra te cfardoshem te rangut:", str(x)
    return y

# metoda GCF


def GCF(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return "numri GCF: ", x


# Metoda CentimetertoInches
def KONVERTO(num):
    inc = num/2.54  # 1 inch = 2.54 centimeters
    y = "Cm to Inch: ", inc
    return y


# Metoda e pare shtese
def NUMRI(num):
    n1 = int("%s" % num)
    n2 = int("%s%s" % (num, num))
    n3 = int("%s%s%s" % (num, num, num))
    num1 = "n+nn+nnn= " + str(n1+n2+n3)
    return num1


# Metoda e dyte shtese
def SYPRINA(num):
    y = "Siperfaqja e rrethit me rreze " + \
        str(num) + " eshte: " + str(pi * num*2)
    return y 


class TCPserver(threading.Thread):
    def __init__(self, clientadress, clientSock):
        threading.Thread.__init__(self)
        self.csocket = clientSock
        print("U shtua komunikimi me klientin: ", clientadress)

    def run(self):
        while True:
            request = self.csocket.recv(128)
            request = request.decode('utf-8')
            request = request.upper()
            text = request.split(" ")
            print('Te dhenat nga klienti:' + request)
            try:
                if text[0] == "IP":
                    mesazhi = str(IP((clientadress)))
                elif text[0] == "NRPORTI":
                    mesazhi = str(NRPORTI(clientadress))
                elif text[0] == "NUMERO":
                    mesazhi = str(NUMERO(request[len(text[0]):len(request)]))
                elif text[0] == "ANASJELLTAS":
                    mesazhi = str(ANASJELLTAS(
                        request[len(text[0]):len(request)]))
                elif text[0] == "PALINDROM":
                    mesazhi = str(PALINDROM(text[1]))
                elif text[0] == "KOHA":
                    mesazhi = str(KOHA())
                elif text[0] == "LOJA":
                    mesazhi = str(LOJA())
                elif text[0] == "GCF":
                    try:
                        mesazhi = str(GCF(int(text[1]), int(text[2])))
                    except Exception:
                        mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden GCF dhe dy numra per te realizuar FUNKSIONIN."
                elif text[0] == "KONVERTO":
                    try:
                        mesazhi = str(KONVERTO(int(text[1])))
                    except Exception:
                        mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden KONVERTO dhe nje numer te plote."

                elif text[0] == "NUMRI":
                    try:
                        mesazhi = str(NUMRI(int(text[1])))
                    except Exception:
                        mesazhi = "ka ndodhur nje gabim ju lutem shkruani NUMRI dhe nje numer"

                elif text[0] == "SYPRINA":
                    try:
                        mesazhi = str(SYPRINA(int(text[1])))
                    except Exception:
                        mesazhi = "ka ndodhur nje gabim ju lutem shkruani SYPRINA dhe nje numer per rrezen e rrethit "

                elif text[0] == "EXIT":
                    mesazhi = "Klienti ka nderprere lidhjen me serverin"
                    break
                else:
                    mesazhi = str(dict[text[0]()](self.csocket))
            except Exception:
                mesazhi = "Ka ndodhur nje gabim."
            finally:

                self.csocket.send(mesazhi.encode())
        print('Perfundoj komunikimi')


serverName = 'localhost'
serverPort = 14000
Tserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Tserver.bind((serverName, serverPort))
print("Serveri eshte duke pritur kerkesen nga klienti!")

while True:
    Tserver.listen(5)
    clientSock, clientadress = Tserver.accept()
    thread = TCPserver(clientadress, clientSock)
    thread.start()
