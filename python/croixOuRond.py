'''
Ce fichier permettra la création d'une fenêtre de jeu de morpion grace à la librairie tkinter et une classe
'''

'''Importations'''
from tkinter import * #pour l'affichage graphique
import tkinter as tk #pour l'affichage graphique
from tkinter import simpledialog
from tkinter import messagebox #pour l'affichage graphique

'''
classe Fenetre qui permet de créer une fenêtre de jeu de morpion
'''
class Fenetre (tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #initialisation de la classe
        self.title("Morpion") #titre de la fenêtre
        self.geometry("500x680") #taille de la fenêtre
        self.resizable(False, False) #empeche le redimensionnement de la fenêtre
        self.config(bg="Orange") #couleur de fond de la fenêtre

        #creation d'un label pour le titre
        Label(self, text="Bienvenue dans le Morpion", font=("Helvetica", 16), bg="#022e75", fg="white").pack(pady=10) #titre de la fenêtre
        
        #creation des boutons pour le joeur 1 et 2 cote à cote en longueur
        self.boutonJoueur1 = Button(self, text="Joueur 1", font=("Helvetica", 16), command=self.joueur1)
        self.boutonJoueur1.pack(padx=10, pady=5)
        self.boutonJoueur2 = Button(self, text="Joueur 2", font=("Helvetica", 16), command=self.joueur2)
        self.boutonJoueur2.pack(padx=10, pady=5)
        self.createLine() #appel de la fonction createGame
        self.zoneAppuyer() #appel de la fonction zoneAppuyer



    '''
    Methode qui permet de savoir si le joueur 1 est selectionné
    '''
    def joueur1(self):
        global joueur1
        global joueur2
        joueur1 = True
        joueur2 = False
        self.couleurBouton()
        print("joueur1")

    '''
    Methode qui permet de savoir si le joueur 2 est selectionné
    '''
    def joueur2(self):
        global joueur2
        global joueur1
        joueur2 = True
        joueur1 = False
        self.couleurBouton()
        print("joueur2")

    '''
    Methode qui permet de créer le canvas avec les lignes
    '''
    def createLine(self):
        #creation du canvas avec un fond transparent
        self.canvas = Canvas(self)
        self.canvas.configure(bg = '#022e75')

        #creation des lignes au milieu de la fenêtre 
        self.canvas.create_line(166, 0, 166, 500, fill="white", width=6)
        self.canvas.create_line(0, 166, 500, 166, fill="white", width=5)

        #creation des lignes au milieu de la fenêtre
        self.canvas.create_line(333, 0, 333, 500, fill="white", width=5)
        self.canvas.create_line(0, 333, 500, 333, fill="white", width=5)

        #affichage du canvas adapté à la taille de la fenêtre
        self.canvas.pack(fill=BOTH, expand=4)

    '''
    Methode qui permet de créer les zones cliquables    
    '''
    def zoneAppuyer(self):
        #creation des zones cliquables
        self.canvas.create_rectangle(0, 0, 166, 166, fill="#022e75", tags="zone1")
        self.canvas.create_rectangle(166, 0, 333, 166, fill="#022e75", tags="zone2")
        self.canvas.create_rectangle(333, 0, 500, 166, fill="#022e75", tags="zone3")
        self.canvas.create_rectangle(0, 166, 166, 333, fill="#022e75", tags="zone4")
        self.canvas.create_rectangle(166, 166, 333, 333, fill="#022e75", tags="zone5")
        self.canvas.create_rectangle(333, 166, 500, 333, fill="#022e75", tags="zone6")
        self.canvas.create_rectangle(0, 333, 166, 500, fill="#022e75", tags="zone7")
        self.canvas.create_rectangle(166, 333, 333, 500, fill="#022e75", tags="zone8")
        self.canvas.create_rectangle(333, 333, 500, 500, fill="#022e75", tags="zone9")

        #ajout d'un evenement lors d'un clic sur une zone
        
        self.canvas.tag_bind("zone1", "<Button-1>", self.clicZone1)
        self.canvas.tag_bind("zone2", "<Button-1>", self.clicZone2)
        self.canvas.tag_bind("zone3", "<Button-1>", self.clicZone3)
        self.canvas.tag_bind("zone4", "<Button-1>", self.clicZone4)
        self.canvas.tag_bind("zone5", "<Button-1>", self.clicZone5)
        self.canvas.tag_bind("zone6", "<Button-1>", self.clicZone6)
        self.canvas.tag_bind("zone7", "<Button-1>", self.clicZone7)
        self.canvas.tag_bind("zone8", "<Button-1>", self.clicZone8)
        self.canvas.tag_bind("zone9", "<Button-1>", self.clicZone9)   
        
    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''
    def clicZone1(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2 dans la zone 1
        print("zone1")
        if joueur1:
            # on met une valeur tag pour pouvoir la recuperer plus tard
            self.canvas.create_text(83, 83, text="X", font=("Helvetica", 50), fill="white", tags="texteZone1")
            self.changerJoueur()
            self.verifierGagner()
        
        elif joueur2:
            self.canvas.create_text(83, 83, text="0", font=("Helvetica", 50), fill="white", tags="texteZone1")
            self.changerJoueur()
            self.verifierGagner()
            
    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''
    def clicZone2(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        print("zone2")
        if joueur1:
            # on met une valeur tag pour pouvoir la recuperer plus tard
            self.canvas.create_text(250, 83, text="X", font=("Helvetica", 50), fill="white", tags="texteZone2")
            self.contenuZone()
            self.changerJoueur()
            self.verifierGagner()
            
        elif joueur2:
            # on met une valeur tag pour pouvoir la recuperer plus tard
            self.canvas.create_text(250, 83, text="0", font=("Helvetica", 50), fill="white", tags="texteZone2")
            self.contenuZone()
            self.changerJoueur()
            self.verifierGagner()
            
    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''
    def clicZone3(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        print("zone3")
        if joueur1:
            self.canvas.create_text(416, 83, text="X", font=("Helvetica", 50), fill="white", tags="texteZone3")
            self.changerJoueur()
            self.verifierGagner()   
        elif joueur2:
            self.canvas.create_text(416, 83, text="0", font=("Helvetica", 50), fill="white", tags="texteZone3")
            self.changerJoueur()
            self.verifierGagner()
            
    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''
    def clicZone4(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        print("zone4")
        if joueur1:
            self.canvas.create_text(83, 250, text="X", font=("Helvetica", 50), fill="white", tags="texteZone4")
            self.changerJoueur()
            self.verifierGagner()    
        elif joueur2:
            self.canvas.create_text(83, 250, text="0", font=("Helvetica", 50), fill="white", tags="texteZone4")
            self.changerJoueur()
            self.verifierGagner()
            
    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''
    def clicZone5(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        print("zone5")
        if joueur1:
            self.canvas.create_text(250, 250, text="X", font=("Helvetica", 50), fill="white", tags="texteZone5")
            self.contenuZone()
            self.changerJoueur()
            self.verifierGagner()              
        elif joueur2:
            self.canvas.create_text(250, 250, text="0", font=("Helvetica", 50), fill="white", tags="texteZone5")
            self.changerJoueur()
            self.verifierGagner()
            
    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''        
    def clicZone6(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        print("zone6")
        if joueur1:
            self.canvas.create_text(416, 250, text="X", font=("Helvetica", 50), fill="white", tags="texteZone6")
            self.changerJoueur()
            self.verifierGagner()
        elif joueur2:
            self.canvas.create_text(416, 250, text="0", font=("Helvetica", 50), fill="white", tags="texteZone6")
            self.changerJoueur()
            self.verifierGagner()         

    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''        
    def clicZone7(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        print("zone7")
        if joueur1:
            self.canvas.create_text(83, 416, text="X", font=("Helvetica", 50), fill="white", tags="texteZone7")
            self.changerJoueur()
            self.verifierGagner()
            
        elif joueur2:
            self.canvas.create_text(83, 416, text="0", font=("Helvetica", 50), fill="white", tags="texteZone7")
            self.changerJoueur()
            self.verifierGagner()
            
    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''        
    def clicZone8(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        print("zone8")
        if joueur1:
            self.canvas.create_text(250, 416, text="X", font=("Helvetica", 50), fill="white", tags="texteZone8")
            self.changerJoueur()
            self.verifierGagner()
        elif joueur2:
            self.canvas.create_text(250, 416, text="0", font=("Helvetica", 50), fill="white",  tags="texteZone8")
            self.changerJoueur()
            self.verifierGagner()

    '''
    appelle des fonctions qui permettent de si la zone à etait cliqué
    '''       
    def clicZone9(self, event):
        #ecrire un X pour le joeur 1 sinon un 0 pour le joeur 2
        #print("zone9")
        if joueur1:
            self.canvas.create_text(416, 416, text="X", font=("Helvetica", 50), fill="white", tags="texteZone9")
            self.changerJoueur()
            self.verifierGagner()
            
        elif joueur2:
            self.canvas.create_text(416, 416, text="0", font=("Helvetica", 50), fill="white", tags="texteZone9")
            self.changerJoueur()
            self.verifierGagner()
            
        
    '''
    methode qui permet de changer le tour du joueur
    '''
    def changerJoueur(self):
        global joueur1
        global joueur2
        if joueur1:
            joueur1 = False
            joueur2 = True
            #mettre la couleur du bouton en rouge
            self.couleurBouton()
        elif joueur2:
            joueur1 = True
            joueur2 = False
            #mettre la couleur du bouton en vert
            self.couleurBouton()


    '''
    mettre la couleur du bouton en rouge du joeur lorsque ce n'ees pas son tour
    '''
    def couleurBouton(self):
        if joueur1:
            #on désactive le bouton du joueur 2
            self.boutonJoueur2.config(state=DISABLED)
            #on active le bouton du joueur 1
            self.boutonJoueur1.config(state=NORMAL)
            self.boutonJoueur1.config(bg="green")
            self.boutonJoueur2.config(bg="red")

        elif joueur2:
            #on désactive le bouton du joueur 1
            self.boutonJoueur1.config(state=DISABLED)
            #on active le bouton du joueur 2
            self.boutonJoueur2.config(state=NORMAL)
            self.boutonJoueur1.config(bg="red")
            self.boutonJoueur2.config(bg="green")
           

    '''
    Methode qui permet de savoir la valeur du texte des tags 'texteZone1' à 'texteZone9'
    '''
    def contenuZone(self):
        idZone1 = self.canvas.find_withtag("texteZone1")
        idZone2 = self.canvas.find_withtag("texteZone2")
        idZone3 = self.canvas.find_withtag("texteZone3")
        idZone4 = self.canvas.find_withtag("texteZone4")
        idZone5 = self.canvas.find_withtag("texteZone5")
        idZone6 = self.canvas.find_withtag("texteZone6")
        idZone7 = self.canvas.find_withtag("texteZone7")
        idZone8 = self.canvas.find_withtag("texteZone8")
        idZone9 = self.canvas.find_withtag("texteZone9")

        #on recupere le contenu texte des tags 
        if idZone1 != None:
            texteZone1 = self.canvas.itemcget(idZone1, "text")
            self.verifierGagner()
            print("zone 1 texte : ",texteZone1)
        if idZone2 != None:
            texteZone2 = self.canvas.itemcget(idZone2, "text")
            print("zone 2 texte : ",texteZone2)
        if idZone3 != None:
            texteZone3 = self.canvas.itemcget(idZone3, "text")
            print("zone 3 texte : ",texteZone3)
        if idZone4 != None:
            texteZone4 = self.canvas.itemcget(idZone4, "text")
            print("zone 4 texte : ",texteZone4)
        if idZone5 != None:
            texteZone5 = self.canvas.itemcget(idZone5, "text")
            print("zone 5 texte : ",texteZone5)
        if idZone6 != None:
            texteZone6 = self.canvas.itemcget(idZone6, "text")
            print("zone 6 texte : ",texteZone6)
        if idZone7 != None:
            texteZone7 = self.canvas.itemcget(idZone7, "text")
            print("zone 7 texte : ",texteZone7)
        if idZone8 != None:
            texteZone8 = self.canvas.itemcget(idZone8, "text")
            print("zone 8 texte : ",texteZone8)
        if idZone9 != None:
            texteZone9 = self.canvas.itemcget(idZone9, "text")
            print("zone 9 texte : ",texteZone9)
                    
    '''
    methode qui permet de verifier si un joeur a selectionner 3 cases alignées
    '''
    def verifierGagner(self):
        global joueur1
        #print("verifier gagner")
        #on recupere les id des tags 'texteZone1' à 'texteZone9'
        idZone1 = self.canvas.find_withtag("texteZone1")
        idZone2 = self.canvas.find_withtag("texteZone2")
        idZone3 = self.canvas.find_withtag("texteZone3")
        idZone4 = self.canvas.find_withtag("texteZone4")
        idZone5 = self.canvas.find_withtag("texteZone5")
        idZone6 = self.canvas.find_withtag("texteZone6")
        idZone7 = self.canvas.find_withtag("texteZone7")
        idZone8 = self.canvas.find_withtag("texteZone8")
        idZone9 = self.canvas.find_withtag("texteZone9")

        #on recupere le contenu texte des tags pour toutes les zones
        if idZone1 != None:
            texteZone1 = self.canvas.itemcget(idZone1, "text")

        if idZone2 != None:
            texteZone2 = self.canvas.itemcget(idZone2, "text")

        if idZone3 != None:
            texteZone3 = self.canvas.itemcget(idZone3, "text")

        if idZone4 != None:
            texteZone4 = self.canvas.itemcget(idZone4, "text")

        if idZone5 != None:
            texteZone5 = self.canvas.itemcget(idZone5, "text")

        if idZone6 != None:
            texteZone6 = self.canvas.itemcget(idZone6, "text")

        if idZone7 != None:
            texteZone7 = self.canvas.itemcget(idZone7, "text")

        if idZone8 != None:
            texteZone8 = self.canvas.itemcget(idZone8, "text")

        if idZone9 != None:
            texteZone9 = self.canvas.itemcget(idZone9, "text")
        
        #on regarde si les 3 zones sont alignés et si elles sont égales à 'X' ou '0'
        if texteZone1 == texteZone2 and texteZone2 == texteZone3 and texteZone1 == "X" :
            #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()

            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone1 == texteZone2 and texteZone2 == texteZone3 and texteZone1 == "0":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()

            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone1 == texteZone4 and texteZone4 == texteZone7 and texteZone1 == "X":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()

            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone1 == texteZone4 and texteZone4 == texteZone7 and texteZone1 == "0":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()

            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()
        elif texteZone1 == texteZone5 and texteZone5 == texteZone9 and texteZone1 == "X":
            #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()

            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone1 == texteZone5 and texteZone5 == texteZone9 and texteZone1 == "0":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone2 == texteZone5 and texteZone5 == texteZone8 and texteZone2 == "X":
            #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone2 == texteZone5 and texteZone5 == texteZone8 and texteZone2 == "0":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()
        elif texteZone3 == texteZone6 and texteZone6 == texteZone9 and texteZone3 == "X":
            #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone3 == texteZone6 and texteZone6 == texteZone9 and texteZone3 == "0": 
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()
        elif texteZone3 == texteZone5 and texteZone5 == texteZone7 and texteZone3 == "X":
            #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone3 == texteZone5 and texteZone5 == texteZone7 and texteZone3 == "0":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()
        elif texteZone4 == texteZone5 and texteZone5 == texteZone6 and texteZone4 == "X":
            #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone4 == texteZone5 and texteZone5 == texteZone6 and texteZone4 == "0":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone7 == texteZone8 and texteZone8 == texteZone9 and texteZone7 == "X":   
            #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 1 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()

        elif texteZone7 == texteZone8 and texteZone8 == texteZone9 and texteZone7 == "0":
           #on affiche une messagebox pour annoncer que le joueur 1 a gagné et on demande si on veut rejouer
            reponse = messagebox.askyesno("Gagné", "Le joueur 2 a gagné, voulez-vous rejouer ?")
            if reponse == True:
                #on ferme la fenetre
                self.destroy()
                # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                joueur1 = True
                #on relance la fenetre
                fen = Fenetre()
                fen.mainloop()
            else:
                #on ferme la fenetre
                self.destroy()
                #on quitte
                self.quit()
        else:
            #on verifie si toutes les cases sont remplies et si il n'y a pas de gagnant on demande si on veut rejouer
            if texteZone1 != "" and texteZone2 != "" and texteZone3 != "" and texteZone4 != "" and texteZone5 != "" and texteZone6 != "" and texteZone7 != "" and texteZone8 != "" and texteZone9 != "":
                reponse = messagebox.askyesno("Match nul", "Match nul, voulez-vous rejouer ?")
                if reponse == True:
                    #on ferme la fenetre
                    self.destroy()
                    # on reinisialise le joueur1 pour que le prochain joeur soit le joueur1
                    joueur1 = True
                    #on relance la fenetre
                    fen = Fenetre()
                    fen.mainloop()
                else:
                    #on ferme la fenetre
                    self.destroy()
                    #on quitte
                    self.quit()
            
            
        
                                                

if __name__ == "__main__":
    fen = Fenetre()
    fen=mainloop() #boucle infinie pour afficher la fenêtre





  