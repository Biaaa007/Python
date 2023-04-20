# Definesc operatiile matematice
def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b == 0:
        print("Nu se poate împărți la 0.")
        return None
    return a / b

def sterge():
    return 0

print("Acesta este un calculator")
print("Introduceti valorile si semnele pentru a efectua operatiile matematice.")
print("Introduceti C pentru a sterge.")

val1 = input("Valoarea nr.1 : ")
if val1 == 'C':
    val1 = sterge()
else:
    val1 = int(val1)

op = input("Operatia matematica: ")

val2 = input("Valoarea nr.2 : ")
if val2 == 'C':
    val2 = sterge()
else:
    val2 = int(val2)

if op == '+':
    rezultat = adunare(val1, val2)
elif op == '-':
    rezultat = scadere(val1, val2)
elif op == '*':
    rezultat = inmultire(val1, val2)
elif op == '/':
    rezultat = impartire(val1, val2)
else:
    rezultat = None

if rezultat is not None:
    print("Rezultat operatie:", rezultat)
