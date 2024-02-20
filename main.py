import random


letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def generator_of_password():
    pregunta = int(input("que tan larga sera su contraseña?:")) 
    PASSWORD = ""

    for i in range(pregunta):
        y = random.choice(letras)
        PASSWORD += y


    print("su contraseña es:",PASSWORD)


generator_of_password()
