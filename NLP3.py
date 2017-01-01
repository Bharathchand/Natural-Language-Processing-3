import nltk
    
f=open('constitution.txt','rU')

raw = f.read()
raw = raw.upper()
raw = raw.decode('utf-8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

print sorted(set(text))
