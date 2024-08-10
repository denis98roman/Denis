try:
    a=int(input('VVedin chislo: '))
    b=int(input('Vvedit chislo: '))
    c=a/b
    print('rez=',c)
except ValueError:
    print("ne vidpovada")
except ZeroDivisionError:
    print('divizion by')
    
        