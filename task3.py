    
sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

wordTrees = []

for sentence in sentences:
    wordTrees.append(sentence.split(" "))
    
print(f'word_trees = {wordTrees}\n')

# word_trees = [['My', 'name', 'is', 'Ram'], ['He', 'is', 'a', 'good', 'person'], ['You', 'should', 'be', 'careful', 'while', 'coding'], ['He', 'can', 'do', 'better'], ['The', 'person', 'is', 'mysterious'], ['Jay', 'Shree', 'Ram'], ['It', 'is', 'my', 'pen.']]

wordCount = {}
for words in wordTrees:
    for word in words:
        wordCount[word] =  wordCount.get(word, 0) + 1
        
print(wordCount)