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
        Une fois la partie terminée, on affiche le tableau de cases complètement dévoilée
        et on indique un message sur l'issue de la partie (victoire ou défaite).
        """
        
        ### TODO: Modifier le code pour demander à l'utilisateur de choisir la taille
        ### du tableau (nombre de lignes et nombres de colonnes, ainsi que le nombre 
        ### de mines)     
        
        ## Il est mentionné dans les consignes de commencer à tester le jeu avec les
        ## valeurs par défaut. Cependant, suffirait-il de procéder comme suit ?
        ## JD Les valeurs par défauts sont déjà "hard codé" dans la fonction d'initialisation de Tableau.
        ## Selon-moi on peut y aller avec ce que tu suggères.

        # print('*** Options du jeu ***')
        # dimension_rangee = int(input('Entrez le nombre de lignes : '))
        # dimension_colonne = int(input('Entrez le nombre de colonnes : '))
        # nombre_mines = int(input('Entrez le nombre de mines : '))
        # self.tableau_mines = Tableau(dimension_rangee, dimension_colonne, nombre_mines))
        # peut-être pourrait-on directement mettre les inputs dans Tableau.
        #
        ## JD: je crois qu'on doit laisser les inputs dans la fonction jouer comme tu l'as fait. Dans tableau ces
        ## variables sont dans les attributs de la classe. Je n'ai pas fini mon analyse, mais si la fonction
        ## Tableau est appelée d'un autre endroit dans le programme on ne voudra peut-être pas poser la question
        ## à l'utilisateur.
        # Effectivement, je pense que tu as raison.

        self.tableau_mines = Tableau()
        
        compteur_tours = 0
        while not self.partie_terminee:
            compteur_tours +=1
            print(f'\n===> Tour #{compteur_tours} <===')
            self.tableau_mines.afficher_tableau()
            self.tour()
            
        self.tableau_mines.afficher_solution()

        ## JD Quand on sort de cette boucle c'est que la partie est terminée donc est-ce qu'on
        ## doit utilsier le return ou tout simplement afficher victoire ou défaite?
        
        # Comme expliqué dans mon commentaire ci-dessous (lignes 94-96), il faut de toutes manières afficher
        # le tableau solution, alors on pourrait mettre un return pour le tableau solution, 
        # devant la ligne 73, et mettre des prints pour défaite et victoire. Il nous
        # faut absolument un return sinon ça risque de retourner None par défaut avec le message de victoire/défaite.

        ### TODO: Afficher le message de victoire ou de défaite
        
        # peut-être faire une condition du genre : 
        #
        # if self.tableau_mines.contient_case_a_devoiler(): 
        #   print('Défaite!')
        # else :
        #   print('Victoire!') 
        #
        # return self.tableau_mines.afficher_solution()
        #
        # Il faudra faire attenton au return, pour ne pas que la méthode recrache 
        # None avec le message de victoire ou de défaite. On doit de toutes 
        # façon retourner le tableau solution
               
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
        # TODO: À programmer.
        
        # On demande les coordonnées d'une case à dévoiler avec
        # demander_coordonnees_case_a_devoiler(self) ?
        ## JD Oui je crois que c'est ça qu'on doit faire.

        # On dévoile la case avec devoiler_case() de tableau.py ?
        ## JD Oui.
        
        # On détecte si une mine a été actionnée avec contient_mine() de tableau.py ?
        ## JD Oui.

        # On créer une condition du genre :
        # if self.tableau_mines.contient_mine() or not self.tableau_mines.contient_cases_a_devoiler() :
        #   self.partie_terminee = True
        ## JD contient_mine() va nous retourner True alors oui on peut faire ça.

        pass
        
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
        # TODO: À programmer.
        
        # 1) utiliser .isnumeric() ?
        ## JD oui c'est ce que j'utiliserais.

        # 2) et 3) utiliser valider_coordonnees_a_devoiler ?
        ## JD Oui.
        pass

    
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
            colonne_y = input("Entrez le numéro de ligne: ")
            rangee_x = input("Entrez le numéro de colonne: ")
            validation = self.valider_coordonnees(rangee_x, colonne_y)

        return colonne_y, rangee_x


def test_demander_coordonnees_case_a_devoiler():

    test_partie = Partie()

    assert test_partie.demander_coordonnees_case_a_devoiler()


if __name__ == '__main__':

    print('Tests unitaires...')
    test_demander_coordonnees_case_a_devoiler()
    print('Tests réussis!')