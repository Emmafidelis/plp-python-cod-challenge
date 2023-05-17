counter = input("Enter file name: ")

word = input("Enter word to be searched: ")
k = 0

with open(counter, 'r') as file:
  for line in file:
    words = line.split()
    for i in words:
      if(i == word):
        k += 1
print("occurence of the word:")
print(k)