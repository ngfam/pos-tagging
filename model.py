from word_tag_prepare import TrieCreator
from training_data_reader import reader
import math

inf = -100000000

creator = TrieCreator()
wordTrie = creator.getTrie()
wordTrie.build()

datas = reader(wordTrie)
ngram = datas.process()

def calcProbability(sentence):
    sentence.append('</s>')
    n = len(sentence)

    tags = []
    for word in sentence:
        tags.append(wordTrie.searchTag(word)[1])
    
    f = [None] * (n + 1)
    trace = [None] * (n + 1)

    f[0] = [[0.0]]
    trace[0] = [[0]]

    previous1 = "<s>"
    previous2 = "</s>"
    
#    print(tags)

    bestx = 0
    besty = 0

    for i in range(n):
        word = sentence[i]
        tag = tags[i]
        tag1 = None
        tag2 = None 

        if i == 0:
            tag1 = [("<", 1.0)]
        else:
            tag1 = tags[i - 1]
        if i < 2:
            tag2 = [("<", 1.0)]
        else:
            tag2 = tags[i - 2]

        f[i + 1] = [[inf] * len(tag)] * len(tag1)
        trace[i + 1] = [[0] * len(tag)] * len(tag1)

        for j in range(len(tag1)):
            for k in range(len(tag)):
                for h in range(len(tag2)):
                    prob = tag[k][1]
                    coherence = ngram.query(tag2[h][0], tag1[j][0], tag[k][0])
                    finalProb = coherence * prob
                    if word == "<unk>":
                        finalProb = ((coherence + prob) / 2) * prob
                    finalProb = math.log2(finalProb)

                    if f[i][h][j] + finalProb > f[i + 1][j][k]:
                        f[i + 1][j][k] = f[i][h][j] + finalProb
                        trace[i + 1][j][k] = h
                    
                    if i == n - 1:
                        if f[i + 1][j][k] > f[i + 1][bestx][besty]:
                            bestx = j
                            besty = k

    tagResult = []
    for i in range(n):
        j = n - i
        tagResult.append(tags[j - 1][besty][0])        
        nxt = trace[j][bestx][besty]
        besty = bestx
        bestx = nxt
    
    tagResult.reverse()
    print(tagResult)

calcProbability(["this", "is", "very", "good"])


    

