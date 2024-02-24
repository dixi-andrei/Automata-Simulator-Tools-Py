def citire(f, g):
    d = {}
    for linie in f:
        linie = linie.strip()
        if linie[
            0] != "#":                      # functia citire determina sectiunile si creeaza dictinarul ce contine starile, sigma, delta
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
    if len(multime) != len(d["[SIGMA]"]):          #verific daca multimea de simboluri sigma are duplicates
        g.write("\n")
        g.write("Sigma are valori egale")
        return 0
    else:
        print(d["[SIGMA]"])


def verifica_states(d, g):
    nr = 0
    for x in d["[STATES]"]:
        nr += x.count("S")                      #verific numarul de stari din states si verific daca exista doar o singura stare initiala
    if nr != 1:
        g.write("\n")
        g.write("Sunt mai multe stari")
        return 0


def verifica_staridelta(d, g):
    lista_delta = []
    lista_states = []
    for linie in d["[DELTA]"]:
        linie = linie.split(",")
        del linie[1]
        lista_delta.append(linie)              #verific daca starile din delta apartin multii de stari
    for linie in d["[STATES]"]:
        linie = linie.split(",")
        lista_states += [linie[0]]
    for linie in lista_delta:
        for x in linie:
            if x not in lista_states:
                g.write("\n")
                g.write("Starile din delta nu apartin multimii starilor")
                return 0


def emulate_nfa(d, g, s1):
    d_states = {}
    lista_finalstates = []
    for x in d["[STATES]"]:
        x = x.split(",")                    #emularea NFA-ului
        if "F" in x:
            lista_finalstates += [x[0]]
        if "S" in x:
            q0 = x[0]
    print(q0)
    for linie in d["[STATES]"]:
        linie = linie.split(",")
        d_states[linie[0]] = {}
        for x in d["[SIGMA]"]:
            d_states[linie[0]][x] = []
    for tranzitie in d["[DELTA]"]:
        tranzitie = tranzitie.split(",")
        d_states[tranzitie[0]][tranzitie[1]] += [tranzitie[2]]
    q = []
    q += d_states[q0][s1[0]]
    for s in s1:
        qc = []
        for x in q:
            y = d_states[x][s]
            if len(y) != 0:                         #aici implementez arborele de parsare
                qc += y
        q = qc
        for x in q:
            if len(d_states[x]["e"]) > 0:
                if d_states[x]["e"] not in q:
                    q += d_states[x]["e"]

    ok = 0
    for i in q:
        if i in lista_finalstates:               #daca in cel putin una din ramuri a ajuns in starea finala NFA-ul functioneaza
            ok = 1
    if ok == 1:
        print("Functioneaza")
    else:
        print("Nu functioneaza")


f = open("dateinNFA(1.7).in", "r")
with open("dateoutNFA.out", "w") as g:
    d = citire(f, g)                                #apelarea functiilor
    verifica_sigma(d, g)
    verifica_states(d, g)
    verifica_staridelta(d, g)
    s = "0111"                                     #stringul
    emulate_nfa(d, g, s)
    g.close()