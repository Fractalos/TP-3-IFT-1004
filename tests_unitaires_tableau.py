# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:26:23 2020

@author: Utilisateur
"""

class Tableau():

    def __init__(self, dimension_rangee=5, dimension_colonne=5, nombre_mines=5):
    
        self.dimension_rangee = dimension_rangee
        self.dimension_colonne = dimension_colonne
        self.nombre_mines = nombre_mines
        
        est_minee = True
        est_voisine_d_une_mine =  True
        est_devoilee = True
        
        self.dictionnaire_cases = {(1,1) : est_minee, (2,3): est_minee, (5,5): est_devoilee, (1,4) : est_voisine_d_une_mine}

    def valider_coordonnees(self, rangee_x, colonne_y):
        
        rangee_valide = rangee_x >= 1 and rangee_x <= self.dimension_rangee
        colonne_valide = colonne_y >= 1 and colonne_y <= self.dimension_colonne
        return rangee_valide and colonne_valide

    def valider_coordonnees_a_devoiler(self, rangee_x, colonne_y):
        
        coordonnees = (rangee_x, colonne_y)
        return self.valider_coordonnees(rangee_x, colonne_y) and coordonnees not in self.dictionnaire_cases
            
    def obtenir_voisins(self, rangee_x, colonne_y):
        
        voisinage = ((-1, -1), (-1, 0), (-1, 1),
                     (0, -1),           (0, 1),
                     (1, -1),  (1, 0),  (1, 1))

        liste_coordonnees_cases_voisines = []
        case = (rangee_x, colonne_y) 

        for voisin in voisinage :                               # Pour toutes les cases voisines, on additionne la coordonnée en x (respectivement y)
            x, y  = case[0] + voisin[0], case[1] + voisin[1]    # de la case avec celle en x (respectivement y) de son voisin.
                                                                
            if self.valider_coordonnees(x,y):                   # On vérifie si la case voisine est dans le tableau, i.e. respecte ses dimensions.
                liste_coordonnees_cases_voisines.append((x,y))   

        return liste_coordonnees_cases_voisines    
    
    # def contient_mine(self, rangee_x, colonne_y):
        
    #     coordonnees = (rangee_x, colonne_y)
    #     return self.dictionnaire_cases[coordonnees].est_minee

    
if __name__ == '__main__':
    tableau_test = Tableau()
    
    def test_valider_coordonnees_a_devoiler():
        assert tableau_test.valider_coordonnees_a_devoiler(1,4)
        assert not tableau_test.valider_coordonnees_a_devoiler(6,5)
        assert tableau_test.valider_coordonnees_a_devoiler(5,5)
        assert not tableau_test.valider_coordonnees_a_devoiler(11, 10)
        assert not tableau_test.valider_coordonnees_a_devoiler(5, 0)

    def test_obtenir_voisins():
        assert tableau_test.obtenir_voisins(3, 3) == [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
        assert tableau_test.obtenir_voisins(1, 1) == [(1, 2), (2, 1), (2, 2)]
        assert tableau_test.obtenir_voisins(1, 1) == [(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]
        assert not tableau_test.obtenir_voisins(5, 3) == [(4, 2), (4, 3), (4, 4), (5, 2), (5, 4), (6, 2)]
        #print(tableau_test.obtenir_voisins(5, 3))


    print(tableau_test.valider_coordonnees_a_devoiler(1,4))
