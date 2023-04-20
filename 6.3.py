import random
a={'Иванов','Петров','Сидоров','Смирнов','Кузнецов','Волков','Андреев','Сергеев','Попов','Соловьев'}
b={'английский','испанский','китайский','немецкий'}
lang_с={}

for st in a:
   k=random.randint(1,4)
   lang_с[st]=random.sample(list(b),k)

unique_stud=set()
for i in lang_с :
   unique_stud=unique_stud.union(set(lang_с[i]))
ch=[i for i in lang_с if 'китайский' in lang_с [i]]
print('Языки,которые знают ученики:',sorted(unique_stud),({len(unique_stud)}))
print('Студенты знающие китайский:',ch)