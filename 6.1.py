capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington', Afghanistan = 'Kabul', Argentina = 'Buenos Aires', Armenia = 'Yerevan', Azerbaijan = 'Baku', Belarus = 'Minsk', Canada = 'Ottawa', China = 'Beijing', Egypt = 'Cairo', Finland = 'Helsinki', France = 'Paris', Germany = 'Berlin')
country=input('Введите страну с большой буквы:')
if country in capitals:
    print(capitals[country])
else:
    print('В базе нет страны c названием:',country)
for key in sorted(capitals):
    print(key,"-",capitals[key])