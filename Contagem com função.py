from time import sleep
def contador(i, f, p):
    print('-='*20)
    print(f'Contando de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    print('-='*20)

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem. Defina o início, o final e o passo: ')
ini = int(input('Início da sequência: '))
fim = int(input('Final da sequência: '))
pas = int(input('De quanto será o passo? '))
contador(ini, fim, pas)

