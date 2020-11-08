print(
"""Kien Do 300163370
ITI1520 - Devoir 4
30 octobre, 2020
""")


def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Entrez le nom du fichier: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("Il n'y a pas aucun fichier avec ce nom. Essayez encore une fois.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    '''(str)->str
    Retourne une nouvelle chaine de caracteres a partir de la chaine word,
    en minuscule, sans les caracteres specieux et sans les chiffres

    La chaine retournee ne doit pas contenir:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 \t \n

    >>> clean_word("co-operation.")
    'cooperation'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'
    >>> clean_word("SEO : 5 outils gratuits pour trouver des mots-cles pertinents")
    'seo   outils gratuits pour trouver des motscles pertinents'
    '''
    word = word.lower()
    # enleve les caractères spéciaux
    for i in word:
        # enleve les caractères spéciaux
        # garde les caractères minuscules et espaces en utilisant le code ASCII
        if (ord(i) < 97 or ord(i) > 122) and (ord(i) != 32):
            word = word.replace(i, "")
    return word


def test_letters(w1, w2):
    '''(str,str)->bool
    La fonction retourne True si les mots w1 et w2 ont exactement les memes
    lettres, et False sinon

    >>> test_letters("mais", "amis")
    True
    >>> test_letters("lapin", "pinla")
    True
    >>> test_letters("lapin", "alpin")
    True
    >>> test_letters("alin", "alpin")
    False
    '''
    return sorted(w1) == sorted(w2)


def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Pour la chaine s qui represente le texte, la fonction retourne une liste avec ces exigences:
    - les mot ne contient pas des caracteres specieux our des chiffres)
    - il n'y a pas de mots qui se repetent dans la liste
    - la liste est triee en ordre alphabetique (vous pouvez utilser s.sort() ou sorted())

    La fonction doit applelez la fonction clean_word.

    Vous pouvez utiliser s.split() pour obtenir une liste coupee par des espaces.

    >>> create_clean_sorted_nodupicates_list("Consultez notre site de web pour tout savoir de l'actualite internationale, nationale et regionale.")
    ['consultez', 'de', 'et', 'internationale', 'lactualite', 'nationale', 'notre', 'pour', 'regionale', 'savoir', 'site', 'tout', 'web']

    '''
    ns = s.split()
    list_finale = list()
    list_mots = list()
    # enleve les caractères spéciaux et met les caractères en minuscule
    for i in ns:
        list_mots.append(clean_word(i))
    list_mots.sort()
    # enleve les mots qui se répètent dans la liste
    for x in list_mots:
        if x not in list_finale:
            list_finale.append(x)
    return list_finale


def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - word est une chaine de caractere qui represente un mot
    - wordbook est une liste des mots (sans des mots repetes)

    La fonction retourne une liste des anagrammes de mot word dans la liste wordbook
    Il faut utiliser la foction test_letters

    >>> word_anagrams("liste", wordbook)
    ['lites']
    >>> word_anagrams("lapin", wordbook)
    ['alpin', 'plain']
    >>> word_anagrams("elephant", wordbook)
    []
    '''
    l_anagrams = list()
    if word not in wordbook:
        return l_anagrams
    for i in range(len(wordbook)):
        if len(word) == len(wordbook[i]) and word != wordbook[i] and sorted(word) == sorted(wordbook[i]):
            l_anagrams.append(wordbook[i])
    return l_anagrams


def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l est une liste des mots (sans des mots repetes)
    - wordbook est une liste des mots (sans des mots repetes)

    La fonction retourne une liste des entiers ou l'entier de index i represente
    le nombre des anagrammes dans la liste wordbook pour le mot de index i dans liste l.

    Quand un mot dans la liste l est le meme que le mot dans la liste wordbook, on ne le compte pas.

    >>> count_anagrams(["liste","amis", "lapin", "anee", "race", "oreilles"], wordbook)
    [1, 4, 2, 0, 5, 2]
    '''
    l_anagrams = list()
    for i in range(len(l)):
        compteur = 0
        if l[i] in wordbook:
            for z in range(len(wordbook)):
                if len(l[i]) == len(wordbook[z]) and l[i] != wordbook[z] and sorted(l[i]) == sorted(wordbook[z]):
                    compteur += 1
        l_anagrams.append(compteur)
    return l_anagrams


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l est une liste des mots (sans de repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans la liste wordbook pour le mot des index i dans la liste l.

    La fonction retournes tous les mots de la liste l qui ont exactement k anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> k_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2],2)
    ['lapin', 'oreilles']

    '''
    l_k_anagram = list()
    for i in range(len(anagcount)):
        if k == anagcount[i]:
            l_k_anagram.append(l[i])
    return l_k_anagram


def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans liste wordbook pour le mot de index i dans la liste l.

    La fonction retournes tous les mots de l avec le nombre maximal des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> max_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['race']
    '''
    l_max_anagram = list()
    plus_haut = 0
    # trouve la valeur plus haut dans anagcount
    for i in anagcount:
        if i > plus_haut:
            plus_haut = i
    # ajoute les mots dans la liste l qui correspondent avec la valeur plus haut
    for x in range(len(anagcount)):
        if anagcount[x] == plus_haut:
            l_max_anagram.append(l[x])
    return l_max_anagram


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i integer dans la liste
    represente le nombre des anagrammes dans wordbook pour le mot de index i en l.

    La fonction retournes tous les mots de l sans des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> zero_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['anee']
    '''
    l_zero_anagram = list()
    for i in range(len(anagcount)):
        if anagcount[i] == 0:
            l_zero_anagram.append(l[i])
    return l_zero_anagram


##############################
# main
##############################
wordbook = open("french_noaccents.txt").read().lower().split()
list(set(wordbook)).sort()

print("Est-ce que vous voulez:")
print("1. Analyser les anagrammes d'un texte donne dans un fichier?")
print("2. Aide pour le jeu de Scrabble?")
print("Entrez un caractere different de 1 ou 2 pour arreter: ")
choice = input()

if choice == '1':
    file_name = get_file_name()
    rawtx = open(file_name).read()
    l = create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l, wordbook)

    print("\nParmis les mots dans le fichier, les mots suivantes ont le plus grand nombre des anagrammes:")
    l_max_ana = max_anagram(l, anagcount)
    print(l_max_ana)

    print("\nVoici leurs anagrammes:")
    for i in range(len(l_max_ana)):
        print("Les anagrammes de", l_max_ana[i], "sont:", word_anagrams(l_max_ana[i], wordbook))

    print("\nVoici les mots dans le fichiers qui n'ont pas des anagrammes:")
    print(zero_anagram(l, anagcount))

    print("\nSi vous êtes intéresé s'il y a un mot dans le fichier qui a exactement k anagrammes")
    k = int(input("Entrez un entier k: "))
    print("\nVoici le mot (mots) dans le fichier avec exactement", k, "anagrammes:")
    print(k_anagram(l, anagcount, k))



elif choice == '2':
    l_lettres_exactes = list()

    s = input("\nEntrez les letteres que vous avez, sans des espaces: ")
    while ' ' in s:   # error trap des espaces
        print("\nERREUR: Vous avez entré des espaces!!")
        s = input("Entrez les letteres que vous avez, SANS des espaces: ")

    option = int(input("""\nEst-ce que vous voulez d'aide a former un mot avec 
    1. toutes ces lettres
    2. toutes sauf une des ces lettres?\n"""))

    if option == 1:
        print("Voici les mots avec exactement ces lettres:")
        l_lettres_exactes.clear()
        for i in wordbook:
            if test_letters(s, i):
                l_lettres_exactes.append(i)
        print(l_lettres_exactes)

    elif option == 2:
        print("Les lettres que vous avez données sont:", s)
        print("Si on elimine une des ces lettres.")

        for i in range(len(s)):
            q = list(s)  # e.g.: donne la list ["a", "b", "c", "d"]
            q.remove(s[i])  # enleve le caractère en position i
            ns = "".join(q)  # converte q à une chaîne de caractères e.g.: "bcd" si on enleve le premier caractère
            print("\nSans la lettre en position", i, "on a les lettres", ns)
            l_lettres_exactes.clear()
            for x in wordbook:
                if test_letters(ns, x):
                    l_lettres_exactes.append(x)
            if len(l_lettres_exactes) != 0:
                print("Voici les mots avec exactement ces lettres:")
                print(l_lettres_exactes)
            else:
                print("Il n'y a aucun mot avec ces lettres,", ns)


else:
    print("Au revoir!")


