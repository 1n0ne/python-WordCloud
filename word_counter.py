import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

uninteresting_words = ["the", "a", "in","to", "if","on", "is", "it", "of", "and", "or", "an", "as","for", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","well","via","due"]
#open,read & lower the file content and take off all the Punctuation marks 
words = re.findall(r'[a-zA-Z\']+', open('Sample-text-file-10kb.txt').read().lower()) 
#remove the uninteresting words
cleanwords=list(set(words) - set(uninteresting_words))
#convert the list to dict
word_could_dict=Counter(cleanwords)
#creat the world cloud & plot it
wordcloud = WordCloud(background_color = 'white',width = 1000, height = 500).generate_from_frequencies(word_could_dict)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
plt.savefig('yourfile.png', bbox_inches='tight')
plt.close()

