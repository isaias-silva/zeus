import webbrowser as wb
from ascii import *

def main():
  
    print(logo())
    while(1):
        print(menu())
        comand=input("comando:")
        if comand=='1':
            alvo=input('alvo:')

        if comand=='0':
            print("bye!")
            break
        if comand=='9':

            wb.open("https://api.whatsapp.com/send?phone=5521984191603&text=salve%20salve%20Zack%20black%2C%20%C3%A9%20o%20brabo%2C%20%C3%A9%20n%C3%B3s%2C%20a%20retalia%C3%A7%C3%A3o%20domina!")
        else:
            print('comando invalido')   
main()