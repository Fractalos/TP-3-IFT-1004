# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:16:54 2020

@author: Utilisateur
"""

##  !!!
##
# message d'erreur ligne 37 : TypeError: argument of type 'bool' is not iterable
##
##  !!!

class Tableau():

    def __init__(self, dimension_rangee=5, dimension_colonne=5, nombre_mines=5):
    
        self.dimension_rangee = dimension_rangee
        self.dimension_colonne = dimension_colonne
        self.nombre_mines = nombre_mines
        
        est_minee = True
        est_voisine_d_une_mine =  True
        est_devoilee = True
        
        self.dictionnaire_cases = {(1,1) : est_minee, (2,3): est_minee, (5,5): est_devoilee, (1,4) : est_voisine_d_une_mine}

    def valider_coordonnees_tableau(self, rangee_x, colonne_y):
        
        rangee_valide = rangee_x >= 1 and rangee_x <= self.dimension_rangee
        colonne_valide = colonne_y >= 1 and colonne_y <= self.dimension_colonne
        return rangee_valide and colonne_valide

    def valider_coordonnees_a_devoiler(self, rangee_x, colonne_y):
        
        coordonnees = (rangee_x, colonne_y)
        return self.valider_coordonnees_tableau(rangee_x, colonne_y) and coordonnees not in self.dictionnaire_cases[coordonnees]
        
        
    def valider_coordonnees(self, rangee_x, colonne_y):

        #rangee_valide, colonne_valide = False, False

        # while not rangee_valide and not colonne_valide :
        #     rangee_a_tester = input('Entrez le numéro de ligne : ')
        #     colonne_a_tester = input('Entrez le numéro de colonne : ')
        #     rangee_valide, colonne_valide = rangee_a_tester.isnumeric(), colonne_a_tester.isnumeric()
        #     if rangee_valide and colonne_valide :
        #         couple_valide = Tableau.valider_coordonnees_a_devoiler(rangee_valide, colonne_valide())
        #         return couple_valide
        #     else :
        #         rangee_valide, colonne_valide = False, False
        #         print('Coordonnées non valides. Veuillez recommencer.')
            
        rangee_x_a_tester, colonne_y_a_tester = str(rangee_x), str(colonne_y)
        return rangee_x_a_tester.isnumeric() and colonne_y_a_tester.isnumeric() and self.valider_coordonnees_a_devoiler(rangee_x, colonne_y)
    
    
    
tableau_test = Tableau()
print(tableau_test.valider_coordonnees(1,1))
        
        
        
        
        
        
  
        