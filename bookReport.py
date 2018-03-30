import re
import wikipedia as wiki
import nltk
from nltk.tokenize import word_tokenize

def askUserToSearchWiki():
    artical = input('Who would you like to look up on Wikipedia?')
    summary = wiki.summary(artical)

    return summary

def GetSingleName(summary):
    name = re.findall(r'[A-Z]\w+\s[A-Z]\w+',summary)

    return name[0]
    
def getArticals(mathematicians):
    summaryList = list()
    for i in range(0,(len(mathematicians))):
            summaryList.append(wiki.summary(mathematicians[i]))
            
    return summaryList

def Birthday(artical):
    
    try:

        birthday = re.search(r'\w+\s\w+[,\s]+\d\d\d\d',artical).group()
        return birthday
    
    except:
        birthday = 'error'

    return birthday 

def occupation(guruSummary):
    guruTok = word_tokenize(guruSummary)
    guruPOS = nltk.pos_tag(guruTok)
    numSamples = 25
    NN_miss_list = ['[',']']
    
    if len(guruPOS) > numSamples:
        sample = guruPOS[0:numSamples]
    else:
        sample = guruPOS

    for x in range(0,len(sample)):
        if sample[x][1] == 'NN':    # 'NN' semms to hit the target
            NN_hit = sample[x][0]

            if NN_hit in NN_miss_list:
                pass
            else:
                return NN_hit
    
rawArtical = askUserToSearchWiki()
print(GetSingleName(rawArtical))
print(Birthday(rawArtical))
print(occupation(rawArtical))
