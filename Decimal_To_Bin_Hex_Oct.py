def nonfractional(num,base):
    num=int(num)
    temp=''
    while(num>0):
        digit=num%base
        if digit>=10:
            temp+=chr(digit-10+65)
        else:
            temp += str(digit)
        num//=base
    if temp == '':
        temp = '0'
    return temp[::-1]

def fractional(num,base):
    if num == '' or float(num) == 0:
        return 0
    frac = float('0.' + num)
    temp = ''
    count = 0
    while frac > 0 and count < 10:
        frac *= base
        digit = int(frac)
        if digit>=10:
            temp+=chr(digit-10+65)
        else:
            temp += str(digit)
        frac -= digit
        count += 1
    return temp
        
def DecTo(num,base):
    s=str(num)
    L=s.partition('.')
    part1=nonfractional(L[0],base)
    part2=fractional(L[2],base)
    if part2:
        return f'{part1}.{part2}'
    else:
        return part1

decimal=float(input("Enter a Number: "))
conv={2:'Binary',8:'Octal',16:'Hexadecimal'}
for base in conv:
    if decimal<0:
        num=DecTo(decimal*-1,base)
        print(conv[base],': -',num,sep='')
    else:
        num=DecTo(decimal,base)
        print(conv[base],': ',num,sep='')
