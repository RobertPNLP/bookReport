import re
import wikipedia as wiki
import nltk
from nltk.tokenize import word_tokenize

math = wiki.summary('math')
mathematicians = re.findall(r'[A-Z]\w+\s[A-Z]\w+',math)

errors = list()
summaryList = list()

def getArticals(mathematicians):
    
    for i in range(0,(len(mathematicians))):
            summaryList.append(wiki.summary(mathematicians[i]))
            
    return summaryList



def nameAndBirthday(guruSummary):
    for i in range(0,len(guruSummary)):
        try:

            birthday = re.search(r'\w+\s\w+[,\s]+\d\d\d\d',guruSummary[i]).group()
            print()
            print(mathematicians[i] + ' born on ' + birthday) # should pass this in 
            print()
        except:
            print('Error')

    print('Errors in wiki summary search:\t'+ str(len(errors)))


def occupation(guruSummary):
    guruTok = word_tokenize(guruSummary)
    guruPOS = nltk.pos_tag(guruTok)
    numSamples = 25
    if len(guruPOS) > numSamples:
        sample = guruPOS[0:numSamples]
    else:
        sample = guruPOS
    #print('sample')
    #print(sample)

    for x in range(0,len(sample)):
        if sample[x][1] == 'NN':    # 'NN' semms to hit the target
            print(sample[x])
            return sample[x]
    

numGuru = 4
guruSummary = getArticals(mathematicians)
nameAndBirthday(guruSummary)
goodGuessOccupation = occupation(guruSummary[numGuru])
print(mathematicians[numGuru] + ' seems like a ' + goodGuessOccupation[0] + ' guru')


