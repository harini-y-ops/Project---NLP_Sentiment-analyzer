import string 
text=input("Enter a sentence: ")
text=text.lower()
text=text.translate(str.maketrans("","",string.punctuation))
words=text.split()
word_count=len(words)
print("The total number of words are: ",len(words))
longest_word=max(words,key=len)
print("The longest word is: ",longest_word)
def freq():
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
        print("Frequence of the word is: ",freq)
    
positive_words = ["good","great","amazing","powerful","excellent","happy"]
negative_words = ["bad","terrible","slow","sad","boring","weak"]
positive=0
negative=0
for word in words:
    if word in positive_words:
        positive+=1
    elif word in negative_words:
        negative+=1
if positive>negative:
    print("Sentiment : Positive")
elif negative>positive :
    print("Sentiment:Negative")
else:
    print("Sentiment : Neutral")
score= positive-negative
print("Sentiment score: ",score)
