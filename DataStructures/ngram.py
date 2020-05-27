# end of sentence should be > and start of sentence should be <

alpha = 1 / 2
beta = 1/ 3
theta = 1/ 6
delta = 0.2

def increase(mp, key):
    if key in mp:
        mp[key] += 1
    else:
        mp[key] = 1

def get(mp, key):
    if key in mp:
        return mp[key]
    return 0

class ngram:
    def __init__(self):
        self.total = 0
        self.trigram = dict()
        self.bigram = dict()
        self.unigram = dict()

        self.one = dict()
        self.two = dict()
    
    def vocab_count(self):
        return len(self.unigram)
    
    #three tags respectively appeared xyz
    def insert(self, x, y, z):
        self.total += 1
        increase(self.unigram, z)
        increase(self.bigram, (y, z))
        increase(self.trigram, (x, y, z))
        increase(self.one, y)
        increase(self.two, (x, y))
    
    def query(self, x, y, z):
        result = 0
        # print(get(self.unigram, z) + 1, get(self.bigram, (y, z)) + 1, get(self.trigram, (x, y, z)) + 1)
        result += alpha * (get(self.unigram, z) + delta) / (self.vocab_count() + self.total * delta)
        result += beta * (get(self.bigram, (y, z)) + delta) / (self.vocab_count() + get(self.one, y) * delta)
        result += theta * (get(self.trigram, (x, y, z)) + delta) / (self.vocab_count() + get(self.two, (x, y)) * delta)
        return result
    

