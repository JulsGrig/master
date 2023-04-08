a=[1,2,6,8,8,12,43,76,76,104,115]
dubl = [x for i, x in enumerate(a) if x in a[:i]]
print('Повторяющиеся:', dubl)