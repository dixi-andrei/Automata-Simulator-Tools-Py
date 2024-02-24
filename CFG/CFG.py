# Importarea modulului random permite generarea unui număr aleatoriu
# pentru selectarea unei reguli în funcția emulate_cfg.
# Acest modul oferă funcții pentru lucrul cu numere aleatorii în Python.
import random

# Funcția citire primește un fișier de configurare (CFG) și returnează un dicționar
# care conține informațiile din fișierul de configurare.
# În fișierul de configurare, variabilele, terminalele și regulile sunt specificate într-un format specific.
def citire(f):
    d = {}
    for linie in f:
        linie = linie.strip()
        if linie in d.keys():
            return 0
        else:
            if linie[0] == "[":
                cheie = linie
                d[cheie] = []
            else:
                d[cheie] += [linie]
    return d

# Funcția variabile primește o listă de variabile și modifică lista
# pentru a elimina variabilele duplicate și a stabili variabila de start.
def variabile(lista):
    global start_var
    for x in lista:
        if "*" in x:
            copie_x = x
            x = x.split(", ")
            x = x[0]
            start_var = x
    for i in range(len(lista)):
        if lista[i] == copie_x:
            lista[i] = start_var
    return lista

# Deschide fișierul de configurare și aplică funcțiile de citire și variabile pentru a obține
# lista de variabile, lista de terminale și dicționarul de reguli.
f = open("dateincfg.in", "r")  #avem trei inputuri: dateincfg.in, dateinCFG(2.4).in, dateinCFG(2.6).in
d = citire(f)
lista_var = d["[Variables]"]
lista_var = variabile(lista_var)

lista_term = d["[Terminals]"]

dict_rules = {}
lista_rules = d["[Rules]"]

# Parcurge lista de reguli și construiește dicționarul de reguli.
for x in lista_rules:
    x = x.split("->")
    if x[0] not in dict_rules:
        dict_rules[x[0]] = []
        dict_rules[x[0]].append(x[1])
    else:
        dict_rules[x[0]].append(x[1])

# Funcția emulate_cfg primește dicționarul de reguli și un șir inițial.
# Ea aplică regulile CFG pentru a genera un nou șir până când nu mai există variabile neterminale.
def emulate_cfg(d, string):
    str_nou = ""
    nr = 0
    for var in string.split(","):
        if var in d:
            nr += 1
            index = random.randint(0, len(d[var])-1)
            str_nou += ","
            str_nou += d[var][index]
            str_nou += ","
        else:
            str_nou += var
    if nr != 0:
        return emulate_cfg(d, str_nou)
    else:
        return str_nou.replace('$', '')

# Apelează funcția emulate_cfg pentru dicționarul de reguli și variabila de start
# și afișează rezultatul.
print(emulate_cfg(dict_rules, start_var))
