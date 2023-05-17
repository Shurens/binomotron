import random

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  password="example",
  database = "binomotron"
)
cursor = mydb.cursor()

#Affichage d'un menu au tout début pour choisir l'option que l'on souhaite
choix=input("Sélectionnez votre choix :\n1 : Faire des groupes\n2 : Afficher l'adresse mail d'un étudiant\n3 : Afficher la liste des projets\n")


if choix == "1":
#Selection de tous les noms et prenoms de la table etudiants et stockage de ceux-ci 
# dans la variable liste_etudiants(qui est sous forme de tuple)
    query = "SELECT nom, prenom FROM etudiants"
    cursor.execute(query)
    liste_etudiants = cursor.fetchall()

#Mélange de la liste    
    random.shuffle(liste_etudiants)

#Formation de groupes en fonction du nombre qu'on insère dans l'input
    x= int(input("Entrez la taille des groupes :"))
    while len(liste_etudiants) >= x:
        association = []
        for i in liste_etudiants[:x]:
            association.append(liste_etudiants.pop())
        print(association)
#Affichage des étudiants qui ne formeront pas un groupe complet
    print(liste_etudiants)

if choix == "2":
    x= input("Entrez le nom d'un étudiant :").upper()
    query = "SELECT mail FROM etudiants WHERE nom = %s"
    cursor.execute(query,(x,))
    mail = cursor.fetchone()[0]
    
    print(mail)

if choix == "3":

    query = "Select libelle_du_projet FROM projets"
    cursor.execute(query)
    projets = cursor.fetchall()
    
    print(projets)

cursor.close()
mydb.close()
