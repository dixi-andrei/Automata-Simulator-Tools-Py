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

def verifica_sigma(d, g):
    multime = set(d["[SIGMA]"])
    if len(multime) != len(d["[SIGMA]"]):
        g.write("\n")                               #verific sigma sa fie corecta, sa nu aiba duplicates
        g.write("Sigma are valori egale")
        return 0
    else:
        print(d["[SIGMA]"])

def verifica_states(d,g):
    nr = 0
    for x in d["[STATES]"]:                  #verific starile, simbolurile sa fie aceleasi din sigma si sa nu existe mai multe stari initiale
        nr += x.count("S")
    if nr != 1:
        g.write("\n")
        g.write("Sunt mai multe stari")
        return 0

def verifica_staridelta(d,g):
    lista_delta = []
    lista_states = []
    for linie in d["[DELTA]"]:                  #verific daca starile din tranzitii apartin multimii de stari
        linie = linie.split(",")
        del linie[1]
        lista_delta.append(linie)
    for linie in d["[STATES]"]:
        linie = linie.split(",")
        lista_states += [linie[0]]
    for linie in lista_delta:
        for x in linie:
            if x not in lista_states:
                g.write("\n")
                g.write("Starile din delta nu apartin multimii starilor")
                return 0

def verifica_delta(d,g):
    dict = {}
    lista_delta = []
    for linie in d["[DELTA]"]:
        linie = linie.split(",")
        lista_delta.append(linie)
    for linie in lista_delta:                      #verific daca exista tranzitii duplicate in lista de tranzitii
        cheie = linie[0]+","+linie[1]
        if cheie not in dict.keys():
            dict[cheie] = 1
        else:
            dict[cheie] = dict[cheie] + 1
    for x in dict.values():
        if x > 1:
            g.write("\n")
            g.write("Tranzitia din delta este incorecta")
            return 0

def emulate_dfa(d,s1):
    if "[STATES]" in d.keys():
        l = d["[STATES]"]
        lista_starifinale = []                      # simulez DFA-ul pe un sir de intrare s1 si afisez in consola daca functioneaza
        for x in l:
            if "," in x:
                y = x.split(",")
                if "S" in y[1:]:
                    q_start = y[0]
                if "F" in y[1:]:
                    lista_starifinale += [y[0]]
    dict_tranzitii = {}
    if "[DELTA]" in d.keys():
        lista_delta = d["[DELTA]"]
        for x in lista_delta:
            y = x.split(",")
            dict_tranzitii[(y[0],y[1])] = y[2]
    q = q_start
    for s in s1:
        tuplu = (q,s)
        q = dict_tranzitii[tuplu]
    if q in lista_starifinale:
        print("Functioneaza")
    else:
        print("Nu functioneaza")

f = open("dateinDFA(1.6).in", "r")             #dateinDFA(1.6) sau dateinDFA(1.5)
with open("dateoutDFA.out","w") as g:
    d = citire(f, g)
    verifica_sigma(d, g)                        #apelarea functiilor
    verifica_states(d, g)
    verifica_staridelta(d, g)
    verifica_delta(d, g)
    s1 = "0110"                             #stringul
    emulate_dfa(d, s1)
    g.close()