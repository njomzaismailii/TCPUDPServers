#Immportojme librarine per socket komunikim
import socket
import sys

serverName = 'localhost'    
serverPort = 14000
Tcpklienti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Tcpklienti.connect((serverName,serverPort))
try:
     Tcpklienti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     Tcpklienti.connect((serverName, serverPort))
except Exception :
         print("Nuk eshte realizuar lidhja mes klientit dhe serverit.")
else: 
    print("Mire se vini!")


while True:
     print("Per IP shtypni IP")
     print("Per Port shtypni NRPORTI")
     print("Per te pare sa bashtingllore dhe zanore ka nje fjale, shtypeni NUMERO dhe fjalen qe deshironi")
     print("Per te pare kohen shtypni KOHA")
     print("Per te pare lojen shtypni LOJA")
     print("Per te pare renditjen e nje fjale shkruani ANASJELLTAS dhe fjala qe deshironi")
     print("Per ta shikuar qe a eshte nje fjale palindrome shkruani PALINDROM dhe fjalen ")
     print("Per GCF dhe dy numera")
     print("Per konvertimin shruani KONVERTO dhe nje numer")
     print("Per shumezimin e nje numri shkruani NUMRI dhe numrin qe doni")
     print("Per syprinen e rrethit ju lutem shkruani SYPRINA dhe rrezen e rrethit")
     print("\nJu lutemi me poshte shkruani kerkesen tuaj!")
     request = input("Per te perfunduar shkruani EXIT! " + "\n\n\n")
     if request == "EXIT":
         Tcpklienti.send(str.encode(request))
         sys.exit()

     mesazhi = ''
     Tcpklienti.send(str.encode(request))
     data = Tcpklienti.recv(128)
     mesazhi += data.decode("utf-8")
     print("Te dhenat e qe u pranuan nga serveri: "+ str(mesazhi) +"\n\n")
Tcpklienti.close()