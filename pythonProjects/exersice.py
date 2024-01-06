import csv

with open('fav.csv', 'r') as file:
         reader = csv.DictReader(file)

         languages = {}

         for row in reader:
                 language = row['language']
                 if language in languages:
                         languages[language]+=1
                 else:
                         languages[language]=1 

def get_val(dicts):
        return languages[dicts]   
for index,i in enumerate(sorted(languages, key=get_val, reverse=True), start=1):
        print(index, i,)
        
                 
                
                 



