#use backtracking algorithm to detect graph isomorphism

#Matrices from wikipedia page on graph isomorphism:

    # a, b, c, d, g, h, i, j
G = [[0, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1, 1, 0, 1],
     [0, 0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 1, 1, 1],
     [1, 1, 1, 0, 0, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 0],
     [1, 0, 1, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 0]]

    # 1, 2, 3, 4, 5, 6, 7, 8
H = [[0, 1, 0, 1, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 1, 0, 0, 1, 0],
     [1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1],
     [0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0, 1, 0]]

def prometteur(G, H, v):
    for i in range(len(v)):
        for j in range(len(v)):
            if G[i][j] != H[v[i]][v[j]]:
                return False
    return True

def isomorphism(G, H, v = []):
    """
    G and H represent the same graph if and only if a permutation σ of the set {1, 2, . . . , m} exists
    such that for all i, j ∈ {1, 2, . . . , m}, G(i, j) = H(σ(i), σ(j)).

    :param G: symmetric adjacency matrix G ∈{0,1}m×m
    :param H: symmetric adjacency matrix H ∈{0,1}m×m
    :param v: promising vector
    :return: True if G and H are the same undirected graph. False if they are not

    ----

    G et H representent le même graphe si et seulement si une permutation σ de l’ensemble {1,2,...,m} existe
    telle que pour tout i,j ∈{1,2,...,m}, G(i,j) = H(σ(i),σ(j)).

    :param G: matrices d’adjacence symétriques G ∈{0,1}m×m
    :param H: matrices d’adjacence symétriques H ∈{0,1}m×m
    :param v: vecteur prometteur
    :return: True si G et H sont isomorphes (i.e representent le même graphe non orientée). False sinon
    """
    if not prometteur(G,H,v):
        return
    if len(v) == 8:
        return True
    for i in range(len(G)):
        if i in v:
            continue
        if isomorphism(G, H, v + [i]):
            return True
    return False

print(isomorphism(G, H))