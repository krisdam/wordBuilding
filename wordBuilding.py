# Given a corpus of text, this program counts the # of occurrences of each word and prints
# a histogram of that in descending order. 


# Import relevant libraries
import matplotlib.pyplot as plt

# Sample data (replace with your actual counts data)
counts = dict()

print (type(counts))
print ('Enter a line of text:')
line = input('')

words = line.split()

print ('Words:', words)

print ('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print ('Counts', counts)

names = list(counts.keys())
frequencies = list(counts.values())

sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse= True)
namers = [item[0] for item in sorted_items]
valuers = [item[1] for item in sorted_items]

plt.bar(namers, valuers)
plt.xlabel("Words")
plt.ylabel("Frequencies")
plt.title("Histogram of Name Frequencies")
plt.show()