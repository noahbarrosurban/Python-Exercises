def notas(*num, situação = False):
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num)/len(num)

    if r['media'] >= 7:
        r['situação'] = 'Boa'
    elif r['media'] >= 5:
        r['situação'] = 'Razoável'
    else:
        r[situação] = 'Bosta'

    return r

resp = notas(1.2)
print(resp)