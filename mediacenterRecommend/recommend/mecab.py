import MeCab
def keitaiso(message):
    output_words = []
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    node = tagger.parse(message)
    for row in node.split("\n"):
        word = row.split("\t")[0]
        if word == "EOS":
            break
        else:
            pos = row.split("\t")[1].split(",")[0]
            if pos == "名詞":
                output_words.append(word)
    return output_words

def readCSV(id):
    f = open(id + '.csv', 'r')
    fw = open(id + 'wakachi.csv', 'w')
    line = f.readline()
    while line:
        title = line.split(',')[0]
        words = keitaiso(title)
        for i in range(len(words)):
            fw.write(words[i])
            if i != len(words)-1:
                fw.write(",")
            else:
                fw.write('\n')
        line = f.readline()
    f.close()
    fw.close()
    return