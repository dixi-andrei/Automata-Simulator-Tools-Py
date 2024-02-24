# nu prea functioneaza cum ar trebui :(
def citire(f, g):
    d = {}
    for linie in f:
        linie = linie.strip()                       #functia citire determina sectiunile si creeaza dictionarul ce contine starile, sigma, delta
        if linie[0] != "#" and linie[0] != "":
            if linie in d.keys():
                g.write("Se repeta sectiunile")
                return 0
            else:
                if linie[0] == "[":
                    cheie = linie
                    d[cheie] = []
                else:
                    d[cheie] += [linie]
    return d

def ver_sigma(d, g):      #verific sigma sa fie corecta, sa nu aiba duplicates
    multime = set(d["[SIGMA]"])
    if len(multime) != len(d["[SIGMA]"]): #am gandit ca o multime de aceeasi lista de elemente din sigma, va trebui sa fie egala intre ele doar daca nu exista duplicate in sigma
        g.write("\n")
        g.write("Sigma are valori egale")  #mesaj in output
        return 0
    else:
        return 0
        print(d["[SIGMA]"])

def ver_states(d,g):  #verific starile, simbolurile sa fie aceleasi din sigma si sa nu existe mai multe stari initiale
    nr = 0
    for x in d["[STATES]"]:
        nr += x.count("S")  #numar aparatiile lui 1
    if nr != 1:             #in caz ca este diferit de 1 inputul nu este corect
        g.write("\n")
        g.write("Sunt mai multe stari")
        return 0

def ver_staridelta(d,g):    #verific ca starile din functia de tranzitie sa apartina multimii de stari
    lista_states = []
    lista_staridelta = []
    for x in d["[STATES]"]:
        if "," in x:
            x = x.split(",")            #aici adaugam starile in lista_states
            lista_states += [x[0]]
        else:
            lista_states += [x]
    for x in d["[DELTA]"]:
        x = x.split("->")
        y = x[0]
        z = x[1]
        y = y.replace("(","")
        y = y.split(",")            #y este (qx) (qx)->(qz)
        z = z.replace("(","")       #z este q(z) din (qx)->(qz)
        z = z.split(",")
        lista_staridelta += [y[0],z[0]]
    lista_staridelta = set(lista_staridelta)
    for x in lista_staridelta:
        if x not in lista_states:
            g.write("\n")
            g.write("Starile din delta nu apartin alfabetului")

def ver_alfabetdelta(d,g):          #in caz ca a1 din (q1, a1, s1) → (q2, a2, a3) nu apartine alfabetului sau este epsilon se va afisa o eroare
    lista_sigma = []
    lista_sigma_lista = []
    lista_alfabetdelta = [[],[]]
    for x in d["[SIGMA]"]:
        lista_sigma+= [x]
    for x in d["[STACK-SIGMA]"]:    #aici formam lista din simbolurile alfabetului
        lista_sigma_lista += [x]
    for x in d["[DELTA]"]:
        x = x.split("->")
        y = x[0]
        y = y.replace(")","")
        y = y.split(",")
        z = x[1]
        z = z.replace(")","")
        z = z.split(",")
        lista_alfabetdelta[0] += [y[1]]
        lista_alfabetdelta[1] += [y[2]]
        lista_alfabetdelta[1] += [z[1]]
    y = set(lista_alfabetdelta[0])          #y va fi simbolurile din delta care ar trebui sa apartina alfabetului
    z = set(lista_alfabetdelta[1])          #z va fi simbolurile din delta care ar trebui sa apartina alfabetului listei
    for x in list(y):
        if x not in lista_sigma:                        #daca x din lista alfabetului din delta nu apartine sigmei se va afisa un mesaj corespunzator
            g.write("\n")
            g.write("Sigma din delta nu apartine sigma")
    for x in list(z):
        if x not in lista_sigma_lista and x != "e":         #daca x din lista alfabetului din delta nu apartine listei sigmei se va afisa un mesaj corespunzator
            g.write("\n")
            g.write("Sigma-lista din delta nu apartine listei-sigma")

def getDelta(d):        #functia getDelta returneaza dictioarul functiilor de tranzitie
    dict = {}
    delta = d["[DELTA]"]
    for x in delta:
        x = x.split("->")           #tranzitia se va despartii in ["(q1, a1, s1)","(q2, a2, a3)"]
        x[0] = x[0].replace(")","")
        x[0] = x[0].replace("(","")   #x[0] va fi cheia adica (q1,a1,s1)
        x[0] = x[0].split(",")
        x[1] = x[1].replace(")","")
        x[1] = x[1].replace("(","")   #x[1] va fi valoarea (q2,a2,q3)
        x[1] = x[1].split(",")
        if tuple(x[0]) not in dict:             #cheia va fi tranzitia (q1, a1, s1)
            dict[tuple(x[0])] = tuple(x[1])     #iar valoarea va fi (q2, a2, a3)

    return dict


def emulatePDA(input_text, delta):
    stack = ['$']  # Inițializăm stiva cu simbolul de start '$'
    current_state = 'q0'  # Starea inițială

    for symbol in input_text:
        if not stack:  # Verificăm dacă stiva este goală
            return False

        key = (current_state, symbol, stack[-1])  # Cheia pentru a accesa tranziția în dicționarul delta

        if key in delta:
            new_state, pop_symbol = delta[key]  # Obținem noile stare și simbolul de eliminat

            # Verificăm dacă trebuie să eliminăm un simbol din stivă
            if pop_symbol != 'e':
                if stack[-1] == pop_symbol:
                    stack.pop()
                else:
                    return False  # Simbolul de eliminat nu corespunde simbolului din vârful stivei

            current_state = new_state  # Actualizăm starea curentă
        else:
            return False  # Nu există o tranziție definită pentru cheia curentă

    # Verificăm dacă am ajuns într-o stare finală și stiva este goală
    if current_state == 'q2' and len(stack) == 1 and stack[-1] == '$':
        return True
    else:
        return False


f = open("dateinPDA(2.4).in", "r")            #dateinDFA(2.4) sau dateinDFA(2.6)
with open("dateoutPDA.out","w") as g:
    d = citire(f, g)
    ver_sigma(d, g)  # apelarea functiilor
    ver_states(d, g)
    ver_staridelta(d, g)
    ver_alfabetdelta(d, g)
    dict_delta = getDelta(d)
    print(dict_delta)
    s = "0011"
    print(emulatePDA(s,dict_delta))
