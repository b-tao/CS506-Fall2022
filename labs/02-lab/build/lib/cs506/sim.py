def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i]-y[i])
    return res

def jaccard_dist(x, y):
    similar = 0
    for i in range(len(x)):
        for a in range(i):
            if x[i] == y[a]:
                similar += 1

    total = len(x)*2-similar
    index = 100*similar/total
    return 100-index

def cosine_sim(x, y):
    similar = 0
    for i in range(len(x)):
        for a in range(i):
            if x[i] == y[a]:
                similar += 1

    total = len(x)*2-similar
    return 100*similar/total

# Feel free to add more
