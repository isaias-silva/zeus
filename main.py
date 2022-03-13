from hashlib import new
import webbrowser
from ascii import *
def main():
  
    print(logo())
    while(1):
        print(menu())
        comand=input("comando:")
        if comand=='1':
            alvo=input('alvo:')
            webbrowser.open('www.google.com')
        else:
            print('comando invalido')   
main()