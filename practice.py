from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not
from sympy.logic.inference import satisfiable

#First order logic

Human=symbols("Human")
Mortal=symbols("Mortal")
Socretes=symbols("Socretes")

rule = Implies(Human, Mortal)

fact = And(Human)
query=Mortal

kb=And(rule,fact)
result=satisfiable(And(kb, Not(query)))

if not result:
    print('True')

else:
    print("False")