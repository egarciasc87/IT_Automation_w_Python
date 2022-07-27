#Final project
#load text and calculate the numbers of times
#a specific word appears in the text

#1. read text from file
file = open("Text.txt")
text = file.read()
print(text)

#2. clean data
#remore punctuation marks (, . : ;)
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace(";", "")
text = text.replace(":", "")
text = text.replace("(", "")
text = text.replace(")", "")
text = text.replace("[", "")
text = text.replace("]", "")
print("\n\nNew text:\n", text)

#3. contar palabras
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
listWords = text.split()
wordCount = {}

for word in listWords:
    if len(word) <= 3:
        continue
    elif word in uninteresting_words:
        continue
    elif word not in wordCount:
        wordCount[word] = 0

    wordCount[word] += 1

print("\nDictionary:\n", wordCount)

#cloud = wordcloud.WordCloud()
#cloud.generate_from_frequencies(wordCount)
#cloud.to_file("myfile.jpg")
