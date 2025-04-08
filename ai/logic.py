from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not
from sympy.logic.inference import satisfiable

## First Order Logic

Human = symbols('Human')
Mortal = symbols("Mortal")
Socrates = symbols('Socrates')

rule = Implies(Human,Mortal)
fact = And(Human)

query=Mortal

kb = And(rule,fact)
result = satisfiable(And(kb, Not(query)))

if not result:
    print('Scorates is Mortal(Provable)')
else:
    print("Cannot prove if Socrates is Mortal.")


##Prepositional Logic

P=symbols('P')
Q=symbols('Q')

rule = Implies(P,Q)

fact = And(P)
query = Q

kb=And(rule,fact)
result=satisfiable(And(kb, Not(query)))

if not result:
    print("Ground is Wet")
else:
    print("Cannot prove that ground is wet")