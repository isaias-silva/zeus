
import webbrowser
from ascii import *
me='+5521984191603'
def main():
  
    print(logo())
    while(1):
        print(menu())
        comand=input("comando:")
        if comand=='1':
            alvo=input('alvo:')
            webbrowser.open('www.google.com')
        if comand=='9':
             webbrowser.open('https://api.whatsapp.com/send?phone=$%s&text=$salve! retaliação domina'%(me))
        else:
            print('comando invalido')   
main()