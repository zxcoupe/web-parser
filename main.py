import wikipedia

result = wikipedia.page("Atari")
print(result.summary)
for link in result.links:
#Тут переделать вывод в файл=
  print(link)

#Объединить с этим-

#не знаю нужна нет=
#import re
#тут открыть сохраненый файл
file = open("data.txt", "w")
#эти нам не нужна 
#file.write("One Up\nTwo Friends\nThree Musketeers")
#file.close()
 
pattern = "Atari1040ST"

file = open("data.txt", "r")
 
for word in file:
    if re.search(pattern, word):
        print(word)
#Источник: https://python-lab.ru/kak-iskat-fayl-s-pomoschyu-grep-v-python
