text = open("my_text.txt",encoding="utf-8").read().lower()
# store individual tokenized word
word_tokenized_text = word_tokenize(text)
sad_emotions_text = word_tokenized_text 
# list of sad words 
# sad_emotions_text = []
# sad_emotions = str(sad_emotions_text)
sad_emotions = []
# tokenizer = RegexpTokenizer("[\w']+")
# tokenizer.tokenize(sad_emotions_text)   
# add each tokenized word to array of emotions
for word in sad_emotions_text:
    sad_emotions.append(word)
print(sad_emotions)  
    