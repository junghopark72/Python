def introduce_your_family(name, *family_names, **family_info):
    print('제 이름은', name, '입니다.')
    print('제 가족들의 이름은 아래와 같아요.')
    for name in family_names:
        print('  ', name)
    print('-' * 40)
    for key in family_info.keys():
        print(key, ':', family_info.get(key))

introduce_your_family('Chris', 'Jihee', 'Anna', 'Shinhoo', 집='용인', 가훈='행복하게 살자')

def concat(*args, sep="/"):
    return sep.join(args)
