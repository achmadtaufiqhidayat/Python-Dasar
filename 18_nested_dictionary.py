data = {1:{'name':'josh', 'age':'21', 'job':'driver'},
        2:{'name':'mul','age':'27','job':'driver'}   }


for key, value in data.items():
    print("\nKeynya : ", key)

    for key2 in value:
        print(key2 + " -", value[key2])