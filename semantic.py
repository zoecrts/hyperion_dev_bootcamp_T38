import spacy

# Example 1
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Code compares similarity of words
# It's intersting that cat and monkey have the highest similarity as they are
# animals, and banana and monkey have higher similarity than banana and cat,
# assumedly due to the stronger association of banana with monkey rather than cat
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# Example 2
tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Example 3
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
