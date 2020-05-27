import csv 
from DataStructures.ngram import ngram

class reader:
    def __init__(self, trieTag):
        self.data = ngram()
        self.trieTag = trieTag

    def add_sentence(self, sentence):
        sentence.append('>')
        previous1 = '<'
        previous2 = '<'
        for c in sentence:
            self.data.insert(previous1, previous2, c)
            previous1 = previous2
            previous2 = c
        # print(sentence)

    def process(self):
        with open("Datas/pos_training.csv") as csvFile:
            readCSV = csv.reader(csvFile, delimiter = ',')
            count = 0
            lastSentence = []
            for row in readCSV:
                if count == 0:
                    count += 1
                    continue

                count = count + 1
                id = row[1]
                word = row[-2]
                tag = row[-1]

                if word == '.' or word == ',':
                    self.add_sentence(lastSentence)
                    lastSentence.clear()
                else:
                    lastSentence.append(tag)
            return self.data
        
