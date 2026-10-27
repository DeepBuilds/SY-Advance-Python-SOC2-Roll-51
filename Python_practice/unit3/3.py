from collections import Counter
with open('input.txt','w') as f:
  f.write('python is mice\n')
  f.write('python is mice\n')
  f.write('python iass msice\n')
  f.write('python is micsae\n')
  
with open('input.txt','r') as f:
  text=f.read().lower()
words=text.replace('.','').split()
freq=Counter(words)
with open("word_freq","w") as f:
  for word,count in freq.items():
    f.write(f"{word}:{count}\n")
print('input processed')