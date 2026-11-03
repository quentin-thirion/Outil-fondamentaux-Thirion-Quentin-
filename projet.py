import random
import time
 
 

 
def vers_binaire(n):
    if n == 0:
        return "0"
    chiffres = ""
    while n > 0:
        chiffres = str(n % 2) + chiffres
        n = n // 2
    return chiffres
 
 
def presque_egaux(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance
 
 

 
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
 
def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True
 
 
def facteurs(n):
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        resultat.append(n)
    return resultat
 
 
def fibonacci(n):
    precedent, courant = 0, 1
    for _ in range(n):
        precedent, courant = courant, precedent + courant
    return precedent
 
 

 
def evaluer(P, x):
    total = 0
    for coefficient in reversed(P):
        total = total * x + coefficient
    return total
 
 
def deriver(P):
    return [i * P[i] for i in range(1, len(P))]
 
 

 
def produit(A, B):
    n, p, q = len(A), len(A[0]), len(B[0])
    C = [[0] * q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            for k in range(p):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C
 
 

 
def aire(polygone):
    somme = 0
    n = len(polygone)
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        somme = somme + (x1 * y2 - x2 * y1)
    return abs(somme) / 2
 
 
def dedans(P, polygone):
    x, y = P
    n = len(polygone)
    interieur = False
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            x_croisement = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_croisement:
                interieur = not interieur
    return interieur
 
 

# les questions
# Chaque fonction renvoie (énoncée, bonne reponse et explication)
#--------------------------------------------------------------------
 
def question_reste():
    n = random.randint(100, 999)
    d = random.randint(3, 12)
    enonce = f"Quel est le reste de la division euclidienne de {n} par {d} ?"
    return enonce, n % d, f"{n} = {n // d} x {d} + {n % d}"
 
 
def question_binaire():
    n = random.randint(5, 100)
    enonce = f"Ecris {n} en binaire."
    return enonce, vers_binaire(n), "On divise par 2 et on lit les restes a l'envers."
 
 
def question_flottants():
    egal = (0.1 + 0.2 == 0.3)
    proche = presque_egaux(0.1 + 0.2, 0.3)
    choix = random.choice([
        ("En Python, est-ce que 0.1 + 0.2 == 0.3 ? (oui|non)", egal,
         "0.1 + 0.2 donne 0.30000000000000004 a cause de l'ecriture binaire."),
        ("Avec presque_egaux(0.1 + 0.2, 0.3), que renvoie-t-on ? (oui|non)", proche,
         "On compare avec une tolerance au lieu de ==."),
    ])
    return choix[0], "oui" if choix[1] else "non", choix[2]
 
 
def question_premier():
    n = random.randint(10, 200)
    enonce = f"{n} est-il un nombre premier ? (oui|non)"
    reponse = "oui" if est_premier(n) else "non"
    return enonce, reponse, f"Facteurs de {n} : {facteurs(n)}"
 
 
def question_pgcd():
    g = random.randint(2, 9)
    a = g * random.randint(2, 9)
    b = g * random.randint(2, 9)
    enonce = f"Quel est le PGCD de {a} et {b} ?"
    return enonce, pgcd(a, b), "On applique l'algorithme d'Euclide."
 
 
def question_facteurs():
    n = random.randint(20, 300)
    enonce = f"Quel est le plus grand facteur premier de {n} ?"
    return enonce, facteurs(n)[-1], f"{n} = " + " x ".join(str(f) for f in facteurs(n))
 
 
def question_fibonacci():
    n = random.randint(5, 20)
    enonce = f"Avec F(0) = 0 et F(1) = 1, que vaut F({n}) ?"
    return enonce, fibonacci(n), "Chaque terme est la somme des deux précédents."
 
 
def texte_poly(P):
    termes = []
    for i in range(len(P) - 1, -1, -1):
        c = P[i]
        if c == 0:
            continue
        if i == 0:
            termes.append(str(c))
        elif i == 1:
            termes.append(f"{c}x")
        else:
            termes.append(f"{c}x^{i}")
    return " + ".join(termes)
 
 
def poly_aleatoire():
    P = [random.randint(-4, 4) for _ in range(3)]
    P.append(random.randint(1, 4))        
    return P
 
 
def question_horner():
    P = poly_aleatoire()
    x = random.randint(-3, 3)
    enonce = f"Si P(x) = {texte_poly(P)}, que vaut P({x}) ?"
    return enonce, evaluer(P, x), "On peut utiliser la methode d' Horner."
 
 
def question_derivee():
    P = poly_aleatoire()
    x = random.randint(-3, 3)
    enonce = f"Si P(x) = {texte_poly(P)}, que vaut P'({x}) ?"
    return enonce, evaluer(deriver(P), x), f"P'(x) = {texte_poly(deriver(P))}"
 
 
def question_matrices():
    A = [[random.randint(0, 4) for _ in range(2)] for _ in range(2)]
    B = [[random.randint(0, 4) for _ in range(2)] for _ in range(2)]
    i, j = random.randint(0, 1), random.randint(0, 1)
    enonce = (f"A = {A} et B = {B}"
              f"Quel est le coefficient ligne {i + 1}, colonne {j + 1} de A x B ?")
    C = produit(A, B)
    return enonce, C[i][j], f"A x B = {C}"
 
 
def question_aire():
    if random.randint(0, 1) == 0:
        w, h = random.randint(2, 9), random.randint(2, 9)
        forme = [(0, 0), (w, 0), (w, h), (0, h)]
        nom = "rectangle"
    else:
        w, h = random.randint(2, 9), random.randint(2, 9)
        forme = [(0, 0), (w, 0), (0, h)]
        nom = "triangle"
    enonce = f"Quelle est l'aire du {nom} de sommets {forme} ?"
    return enonce, aire(forme), "On utilise la formule des lacets."
 
 
def question_point():
    carre = [(0, 0), (4, 0), (4, 4), (0, 4)]
    P = (random.randint(-2, 6) + 0.5, random.randint(-2, 6) + 0.5)
    enonce = f"Le point {P} est-il dans le carre {carre} ? (oui|non)"
    reponse = "oui" if dedans(P, carre) else "non"
    return enonce, reponse, "On compte les croisements d'un rayon avec les côtés."
 
 

QUESTIONS = [
    ("Nombres", question_reste),
    ("Nombres", question_binaire),
    ("Nombres", question_flottants),
    ("Arithmetique", question_premier),
    ("Arithmetique", question_pgcd),
    ("Arithmetique", question_facteurs),
    ("Arithmetique", question_fibonacci),
    ("Polynomes", question_horner),
    ("Polynomes", question_derivee),
    ("Matrices", question_matrices),
    ("Geometrie", question_aire),
    ("Geometrie", question_point),
]
 
 
# le jeu
# --------------------------------------------------------------
 
def verifier(reponse, attendu):
    reponse = reponse.strip().lower()
    if attendu in ("oui", "non"):
        return reponse[:1] == attendu[:1]
    if isinstance(attendu, str):        
        return reponse == attendu
    try:
        valeur = float(reponse.replace(",", "."))
    except ValueError:
        return False
    return presque_egaux(valeur, attendu)
 
 
def demander_nombre():
    while True:
        try:
            n = int(input("Combien de questions (1 a 20) ? "))
            if 1 <= n <= 20:
                return n
        except ValueError:
            pass
        print("Entre un entier entre 1 et 20.")
 
 
def jouer(historique):
    n = demander_nombre()
    score = 0
    par_theme = {}
    debut = time.perf_counter()
 
    for numero in range(1, n + 1):
        theme, fonction = random.choice(QUESTIONS)
        enonce, attendu, explication = fonction()
        print(f"Question {numero}/{n} [{theme}]")
        print(enonce)
        reponse = input("> ")
 
        if theme not in par_theme:
            par_theme[theme] = [0, 0]
        par_theme[theme][1] += 1
 
        if verifier(reponse, attendu):
            print("Bravo !")
            score += 1
            par_theme[theme][0] += 1
        else:
            print(f"Raté. La réponse était : {attendu}")
            print("Indice :", explication)
 
    temps = time.perf_counter() - debut
    print("\n===== Resultat =====")
    print(f"Score : {score}/{n} (note : {20 * score / n:.1f}/20)")
    print(f"Temps : {temps:.0f} secondes")
    for theme in par_theme:
        bonnes, total = par_theme[theme]
        print(f"  {theme:<13} {bonnes}/{total}")
    historique.append((score, n))
 
 
def afficher_historique(historique):
    if len(historique) == 0:
        print("Aucune partie jouée.")
        return
    for i in range(len(historique)):
        score, n = historique[i]
        print(f"Partie {i + 1} : {score}/{n}")
    meilleure = max(historique, key=lambda p: p[0] / p[1])
    print(f"Meilleure partie : {meilleure[0]}/{meilleure[1]}")
 
 
def main():
    historique = []
    print(" Quiz de maths ")
    while True:
        print("1. Jouer")
        print("2. mes scores")
        print("0. Quitter")
        choix = input("Ton choix : ")
        if choix == "1":
            jouer(historique)
        elif choix == "2":
            afficher_historique(historique)
        elif choix == "0":
            print("Bien joué ! ")
            break
        else:
            print("Choix inconnu.")
 
 
if __name__ == "__main__":
    main()
 
