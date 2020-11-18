# -*- coding: utf-8 -*-
"""
Module contenant la description de la classe Partie qui permet de jouer une partie du jeu démineur.
Dois être démarré en appelant la méthode jouer(). Cette classe contient les informations sur une partie et
utilise un objet tableau_mines (une instance de la classe Tableau).

Auteurs: Charlotte Lavoie-Bel et Jean-Dominique Doyon
"""

from tableau import Tableau


class Partie():
    """
    Contient les informations sur une partie du jeu Démineur, qui se jouera avec
    un tableau de mines. Des méthodes sont disponibles pour faire avancer la partie 
    et interagir avec l'utilisateur.

    Attributes:
        tableau_mines (Tableau): Le tableau de cases où les mines sont cachées avec lequel se
                déroule la partie.
        partie_terminee (bool): True lorsque l'utilisateur a terminé de jouer la partie (victoire ou défaite)
    """

    def __init__(self):
        """
        Initialisation de la Partie. 
        
        Note: L'instance de la classe Tableau, qui sera manipulée par les méthodes de la classe,
              sera initialisée lors de l'appel de la méthode Partie.jouer().
        """
        self.tableau_mines = None
        self.partie_terminee = False

    def jouer(self):
        """
        Tant que la partie n'est pas terminée, on joue un tour de la partie. 
        Une fois la partie terminée, on affiche le tableau de cases complètement dévoilé
        et on indique un message sur l'issue de la partie (victoire ou défaite).
        """        
        print('*** Options du jeu ***')
        dimension_rangee = int(input('Entrez le nombre de lignes : '))
        dimension_colonne = int(input('Entrez le nombre de colonnes : '))
        nombre_mines = int(input('Entrez le nombre de mines : '))
        self.tableau_mines = Tableau(dimension_rangee, dimension_colonne, nombre_mines)
        
        compteur_tours = 0
        while not self.partie_terminee: # Tant qu'une mine n'a pas été actionnée ou qu'il reste des cases à dévoiler
            compteur_tours +=1          # on continue la partie et on incrémente le compteur de tours.
            print(f'\n===> Tour #{compteur_tours} <===')
            self.tableau_mines.afficher_tableau() # On affiche le tableau « mis à jour ».
            self.tour()
            
        self.tableau_mines.afficher_solution() # Si la partie est terminée, on affiche le tableau solution.

        if self.tableau_mines.contient_cases_a_devoiler() and self.tableau_mines.nombre_cases_sans_mine_a_devoiler > 0: # On affiche l'issue de la partie ##TODO
            print()                                        # selon qu'il reste ou non des cases
            print("Défaite!")                              # à dévoiler.
        else:
            print()
            print("Victoire!")
               
    def tour(self):
        """ 
        Jouer un tour, c'est-à-dire:
        
        À chaque tour:
            - On demande à l'utilisateur les coordonnées d'une case à dévoiler
            - On dévoile la case
            - On détecte si une mine a été actionnée, 
              auquel cas affecte True à l'attribut self.partie_terminee.
            - On détecte si toutes les cases ont été dévoilées, 
              auquel cas affecte True à l'attribut self.partie_terminee.
        """

        # Demander à l'utilisateur les coordonnées d'une case à dévoiler.
        coordonnees = self.demander_coordonnees_case_a_devoiler()

        # Pour séparer le tuple retourné par demander_coordonnees_case_a_devoiler.
        rangee_x, colonne_y = coordonnees[0], coordonnees[1]
        #Tableau.devoiler_case(self, rangee_x, colonne_y) # On dévoile la case.
        self.tableau_mines.devoiler_case(rangee_x, colonne_y)

        # On détecte si une mine a été actionnée ou s'il reste des cases à dévoiler.
        if self.tableau_mines.contient_mine(rangee_x, colonne_y) == True or self.tableau_mines.contient_cases_a_devoiler() == False or self.tableau_mines.nombre_cases_sans_mine_a_devoiler == 0:#TODO changer -2 devrait être 0
            self.partie_terminee = True

    def valider_coordonnees(self, rangee_x, colonne_y):
        """
        Méthode qui valide les coordonnées reçues en paramètres.
        Les coordonnées doivent:
            1) être des caractères numériques;
            2) être à l'intérieur des valeurs possibles des rangées et des colonnes 
                du tableau; et 
            3) correspondre à une case qui n'a pas encore été dévoilée.

        Args:
            rangee_x (str):     Chaîne de caractères contenant la rangée
            colonne_y (str):    Chaîne de caractères contenant  la colonne

        Returns:
            bool : True si les coordonnées sont valides, False autrement.
        """

        if rangee_x.isnumeric() and colonne_y.isnumeric(): #1) Vérifie si les coordonnées sont des caractères numériques.
            rangee_x, colonne_y = int(rangee_x), int(colonne_y)
            return self.tableau_mines.valider_coordonnees_a_devoiler(rangee_x, colonne_y) # 2) et 3) Vérifier si les coordonnées respectent 
        else :                                                                            # les dimensions du tableau et ne sont pas dévoilées
            return False                                                                  # avec la méthode valider_coordonnees_a_devoiler.
    
    def demander_coordonnees_case_a_devoiler(self):
        """
        Méthode qui demande à l'utilisateur d'entrer la coordonnée de la case qu'il veut dévoiler.
        Cette coordonnée comporte un numéro de rangée et un numéro de colonne.
        Tant que les coordonnées ne sont pas valides, on redemande de nouvelles coordonnées.
        Une fois les coordonnées validées, on retourne les deux numéros sous forme d'entiers.

        Returns:
            int: Numéro de la rangée
            int: Numéro de la colonne

        """
        validation = False

        while not validation:
            print()
            colonne_y = input("Entrez le numéro de colonne : ")
            print()
            rangee_x = input("Entrez le numéro de ligne : ")

            validation = self.valider_coordonnees(rangee_x, colonne_y)
            
            if not validation :
                print()
                print('Coordonnées invalides. Veuillez recommencer.')

        return int(rangee_x), int(colonne_y)