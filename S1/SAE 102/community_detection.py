from time import time

##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

def create_network(list_of_friends):
    """ Retourne un réseau d'amis à partir d'un tableau d'amis en le parcourant une seule fois"""
    reseau = {}
    amis = list_of_friends
    i = 0
    while i < len(amis):
        if amis[i] not in reseau and amis[i+1] not in reseau:
            reseau[amis[i]] = [amis[i+1]]
            reseau[amis[i+1]] = [amis[i]]
        elif amis[i] in reseau and amis[i+1] not in reseau:
            reseau[amis[i]].append(amis[i+1])
            reseau[amis[i+1]] = [amis[i]]
        elif amis[i] not in reseau and amis[i+1] in reseau:
            reseau[amis[i+1]].append(amis[i])
            reseau[amis[i]] = [amis[i+1]]
        else:
            reseau[amis[i]].append(amis[i+1])
            reseau[amis[i+1]].append(amis[i])
        i += 2
    return reseau



# Question 2:
# Théoriquement, create_network sera légèrement plus rapide que dico_reseau car il n'y a pas besoin de vérifier si un ami a déjà été ajouté au set. Cependant, cette différence de performance sera très faible et ne sera probablement pas perceptible à moins que vous travailliez avec des réseaux très importants.

# On peut également mesurer le temps d'execution des 2 programmes de la manière suivante :
amis = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"), ("Eve", "Charlie")]

tic = time()
create_network(friends)
tac = time()
print("create_network a pris" ,{tac - tic:.6}, "secondes")


amis_dico = dico_reseau(friends)

tic = time()
dico_reseau(friends)
tac = time()
print("dico_reseau a pris", {tac - tic:.6},"secondes")

# Cela nous permettre de déterminer le temps d'execution entre les 2 fonctions, et on remarque facilement que le fonction create_network est plus rapide rien qu'en regardant le nombre de fonctions où doit passer dico_reseau. 

# Question 3:

def get_people(network):
    """ Obtient la liste de tous les amis à partir d'un réseau"""
    liste = list(network)
    return liste

# Question 4:

def are_friends(network, person1, person2):
    """ Détermine si une personne est amie avec une autre selon un réseau"""
    if person2 in network[person1]:
        return True
    return False


# Question 5:

def all_his_friends(network, person, group):
    """ Détermine si une personne est amie avec toutes les personnes du groupe à partir d'un réseau"""
    i=0
    while i< len(group):
        ami=group[i]
        if ami not in network[person]:
            return False
        i+=1
    return True


# Question 6:

def is_a_community(network, group):
    """ Détermine si le groupe est une communauté, c'est-à-dire si toutes les personnes du groupe sont amies entre elles"""
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            if group[i] not in network[group[j]]:
                return False
    return True


# Question 7:

def find_community(network, group):
    """ Trouve une communauté possible grâce à un groupe et un réseau d'amis selon l'heuristique suivante:
    - On part d'une communauté vide.
    - On considère les personnes les unes après les autres. Pour chacune des personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté."""
    community = []
    for person in group:
        if all_his_friends(network, person, community):
            community.append(person)
    return community

# Question 8 :

def order_by_decreasing_popularity(network, group):
    """ Retourne un tableau d'amis les plus populaires selon un groupe d'amis et un réseau d'amis"""
    popularity = {person: len(network[person]) for person in group}
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            if popularity[group[i]] < popularity[group[j]]:
                group[i], group[j] = group[j], group[i]
    return group

# Question 9 :

def find_community_by_decreasing_popularity(network):
    """ Trie l'ensemble des personnes du réseau selon l'ordre décroissant de popularité puis retourne la communauté selon l'heuristique suivante:
    - On part d'une communauté vide.
    - On considère les personnes les unes après les autres. Pour chacune des personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté."""
    community = []
    people = list(network)
    people = order_by_decreasing_popularity(network, people)
    for person in people:
        if all_his_friends(network, person, community):
            community.append(person)
    return community

# Question 10 :

def find_community_from_person(network, person):
    """ Retourne une communauté maximale contenant une personne selon l'heuristique suivante:
    - on choisit une personne du réseau,
    - on crée une communauté contenant juste cette personne,
    - on considère les amis de cette personne par ordre de popularité décroissante. Pour chacune de ces personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté."""
    community = [person]
    amis = network[person]
    amis = order_by_decreasing_popularity(network, list(amis))
    for ami in amis:
        if all_his_friends(network, ami, community):
            community.append(ami)
    return community


# Question 11 :

# Il est théoriquement possible de comparer les deux heuristiques de construction de communauté en termes de complexité, c'est-à-dire en étudiant le nombre d'opérations nécessaires à leur exécution en fonction de la taille du réseau et du nombre de personnes dans le groupe de départ.

# La fonction find_community_by_decreasing_popularity parcourt l'ensemble des personnes du réseau et pour chaque personne, elle construit une communauté en parcourant les amis de cette personne et en vérifiant si chaque ami est ami avec tous les membres de la communauté déjà créée. Elle trie également les amis de chaque personne en fonction de leur popularité décroissante avant de les parcourir.

# La complexité de cette fonction est donc en O(n), où n est le nombre de personnes dans le réseau. Cela signifie que le nombre d'opérations nécessaires à son exécution est proportionnel à n, ce qui signifie qu'elle est plus rapide que la fonction find_community_by_decreasing_popularity en théorie.

# Il est également possible de comparer les deux fonctions de manière expérimentale en mesurant le temps d'exécution de chacune d'elles sur des réseaux de différentes tailles et en comparant les résultats. Cependant, il est important de noter que la complexité théorique d'une fonction ne reflète pas toujours exactement son comportement en pratique, et que d'autres facteurs tels que la puissance de calcul de la machine utilisée peuvent également avoir un impact sur les temps d'exécution mesurés.

# Question 12 :

def find_max_community(network):
    """Retourne la plus grande communauté trouvée avec un réseau et suivant l'heuristique suivante:
    - on choisit une personne du réseau,
    - on crée une communauté contenant juste cette personne,
    - on considère les amis de cette personne par ordre de popularité décroissante. Pour chacune de ces personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté."""
    # On initialise la communauté maximale avec une liste vide
    max_community = []
    # On parcourt toutes les personnes du réseau
    for person in network:
        # On cherche la communauté maximale contenant cette personne
        community = find_community_from_person(network, person)
        # Si la communauté trouvée est plus grande que la communauté maximale actuelle, on met à jour la communauté maximale
        if len(community) > len(max_community):
            max_community = community
    # On retourne la communauté maximale trouvée
    return max_community
    
