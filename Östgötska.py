#get input
word = input().split()

countA = sum([1 for i in word
              if 'ae' in i])

wordLength = len(word)

if(countA/wordLength >= 0.4):
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
