# Ecrivez votre code ici !
Nombre1 = input ("Entrer un nombre entier")
Nombre2 = input ("Entrer un nombre entier")

#is.numeric permet de vérifier que le caractère entré est un nombre

if not Nombre1.isnumeric() or not Nombre2.isnumeric() :
    print ("Erreur: les deux nombres doivent etre des nombres entiers")
    raise SystemExit("Fin du programme")
Nombre1 = int(Nombre1)
Nombre2 = int(Nombre2)

operation = input(f"Entrer un signe entre '+', '-','*' et '/'  pour effectuer votre operation")
if operation not in ['+', '-', '*','/'] :
    print("Erreur:vous avez pas entrer le bon signe")
    raise SystemExit("Fin du programme")

if operation == "+":
    resultat = Nombre1 + Nombre2
    
elif operation == "-" :
    resultat = Nombre1 - Nombre2

elif operation == "*":
    resultat = Nombre1 * Nombre2

elif operation == "/":
    if Nombre2 == 0 :
        print("Erreur: impossible de diviser un nombre par Zero")
        raise SystemExit("Fin du programme")
    resultat = round (Nombre1 / Nombre2, 2)

print (f"le resultat de l'operation est : {round(resultat, 2)}")
    
    






