import csv
from DataStructures.Trie import Trie


class TrieCreator:
    def getTrie(self):
        wordTrie = Trie()
        wordTrie.insert("<s>", '<')
        wordTrie.insert("</s>", '>')
        with open("Datas/pos_training.csv") as csvFile:
            readCSV = csv.reader(csvFile, delimiter = ',')
            count = 0        
            for row in readCSV:
                if count == 0:
                    count += 1
                    continue

                # if count > 100000:
                #     break

                count = count + 1
                after = row[3].lower()
                tag = row[4]

                # print(after, tag)

                if len(tag) == 0:
                    continue

                flag = True
                for c in after:
                    if ord(c) not in range(97, 123):
                        flag = False
                        break
                
                if flag == False:
                    continue

                wordTrie.insert(after, tag)
                wordTrie.insert("<unk>", tag)
        return wordTrie
        
        
        
    

