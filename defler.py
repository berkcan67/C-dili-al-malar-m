# writter: berk can , written in englisch because of python syntax dont uses turkish words#

def saying_hello_screen(): 
    print(" Hello welcome to my application i want to ask you some questions")
    name = input(" please enter your name  :")
    surname = input(" please enter your surname  :")
    age = input("please enter your age  :")
    print("your name:" + name)
    print("your surname:" + surname )
    print("your age :" +age)
saying_hello_screen()

x = int(input("did you want to go a mathematical calculator site? İf you want please click 1 but if you dont want to go please click another one"))

if x ==1 :

    print("please click this link and go a calculator site:\n https://www.calculator.net")
else:
    print("goodbye")