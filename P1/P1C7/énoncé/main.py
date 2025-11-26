# Écrivez votre code ici !
#1.creation du dictionnaire fruits
fruits = {
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange",}
fruits["kiwi"] = "vert"
print(fruits)
couleur_banane = fruits["banane"]
print(couleur_banane)
fruits["pomme"] = "vert"
fruits.pop("banane")
print(fruits.keys())
