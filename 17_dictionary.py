
data= {'name':'hidayat', 'age':'21','address':'bwi'}

data['name'] = 'ahmada'
data['dream'] = 'programmer frontend'
del data['age']

for key,val in data.items():
    print(key, '-', val, '-')