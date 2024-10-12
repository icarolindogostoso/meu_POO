while True:
    try:
        a,b,c = map(int,input().split()) # distancia, velocidade ladrao, velocidade guarda

        if c >= (a*b)/12:
            print('S')
        else:
            print('N')
    except EOFError:
        break