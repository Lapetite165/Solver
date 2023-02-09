##Culture de courgettes et de navets

#Données
#8l d’engrais A disponible → 2l/m2 pour courgettes, 1l/m2 pour navets
EngraisA = 8 #L
QttApourcourgette = 2 #L/m²
QttApournavet = 1 #L/m²
#7l d’engrais B disponible → 1l/m2 pour courgettes, 2l/m2 pour navets
EngraisB = 7 #L
QttBpourcourgette = 1 #L/m²
QttBpournavet = 2 #L/m²
#3l anti-parasite disponible → 1l/m2 pour navets
Antiparasite = 3 #L
QttAPpournavet = 1 #L/m²

#Objetif : maximiser poids
#Produire le maximum (en poids) de légumes, sachant que rendements = 4kg/m2 courgettes, 5kg/m2 navets
RendementC = 4 #kg/m²
RendementN = 5 #kg/m²

# A maximiser :
# 4x+5y

# Contraintes données: 
# Engrais A : 
# 2x+1y<=8 
# Engrais B : 
# x+2y<=7 
# Antiparasite : 
# y<=3 
# Contrainte intrinseque : 
# Le terrain existe dans la réalité :
# x+y>=0


##Importations
from ortools.linear_solver import pywraplp

def terrain():
    ##Solver
    solver = pywraplp.Solver.CreateSolver('GLOP') #Same for SCIP
    if not solver:
        return
    ##Définition des variables
    courgettes = solver.IntVar(0, solver.infinity(), 'courgettes')
    navets = solver.IntVar(0, solver.infinity(), 'navets')
    print('Number of variables =', solver.NumVariables())
    ##Définition des contraintes
    solver.Add(2*courgettes + navets <= 8)
    solver.Add(courgettes + 2*navets <= 7)
    solver.Add(navets <= 3)
    solver.Add(courgettes + navets >= 0)
    print('Number of constraints =', solver.NumConstraints())
    ##Définition de l'objectif
    solver.Maximize(4*courgettes + 5*navets)
    ##Utilisation du solver
    status = solver.Solve()
    ##Affichage de la solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('courgettes (kg) =', courgettes.solution_value())
        print('navets (kg) =', navets.solution_value())
    else:
        print('The problem does not have an optimal solution.')
    ##Statistiques du problème
    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())

terrain()