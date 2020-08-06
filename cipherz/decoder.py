# This module is supposed to handle the decoding of the information in fill_tmp.txt
import dir
from cipherz import recover
from datetime import datetime

x = {'Date/time': ' ', 'Encoded_msg': ' ', 'Decoded_msg': ' '}


def fetch_Rand_tmp():
    accessrand = dir.rand_tmp()
    a = recover.recover(accessrand)
    return a


def decode():
    print('arrived')
    z = []
    f = open('decoded_msg.txt', 'a')
    accessfill = dir.fill_tmp()
    form = fetch_Rand_tmp()
    b = recover.recover(accessfill)
    for i in b:
        for o in form:
            if o == i:
                # print('Found!')
                v = form.index(o) + 1
                j = (form[v])
                z.append(j)
                break
        else:
            z.append(i)

    # Build decoded message using index-sourced data

    for a in z:
        x['Decoded_msg'] += a
        x['Decoded_msg'] += ' '

    dt = datetime.now()
    d_t = dt.strftime('%d/%m/%Y %H:%M')
    x['Date/time'] = d_t
    u = dir.fill_tmp()
    v = open(u, 'r')
    x['Encoded_msg'] = v.read()
    f.write(str(x))
    f.write('\n')
    f.close()
    print('werewolf')
