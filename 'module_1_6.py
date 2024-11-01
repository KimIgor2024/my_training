#             "Словари и множества"

#    "Работа со словарями "

my_dict = {'Anton' :2001 ,'Igor' :2003 ,'Larisa' :2007}
print(my_dict)
print(my_dict['Igor'])
print(my_dict.get('Sasha' ,"такого ключа нет"))
my_dict.update({'Ira : 2015 ,'
                'Kolya' :2002})
#print(my_dict)
#my_dict.pop('Larisa')
print(my_dict)

a = my_dict.pop('Larisa')
print(my_dict)
print(a)

#     "Работа с множествами"
my_set = {1,1,1,2,2,3,3,'P,''p,''True'}
my_set = set(my_set)
print(my_set)
my_set1 = {1,2,3,'P,''p,''True'}
my_set2 ={5,6,8,9}
my_set3 = my_set1.union(my_set2)
print(my_set3)

my_set3 ={1, 2, 3, 5, 6, 8, 9, 'P,''p','True'}
my_set3.remove(3)
print(my_set3)
