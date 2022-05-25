verbs = ['go', 'walk', 'fight', 'kill', 'use', 'eat', 'run', 'leave', 'hide']
nouns = ['bandit', 'city', 'guards', 'dragon', 'potion', 'bread', 'weapon', 'sword', 'magic', 'bow', 'door', 'road']
stops = ['the', 'at', 'from', 'in', 'of', 'nothing']


def scan(data):
    words = data.split()
    results = []

    for i in words:
        if i in verbs:
            return results.append([('verb', i)])
        elif i in nouns:
            return results.append([('noun', i)])
        elif i in stops:
            return results.append([('stop', i)])
        else:
            return 'Not an answer'
