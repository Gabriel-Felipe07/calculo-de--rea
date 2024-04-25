#importações
import math
import colorama
import os

#limpando o terminal antes de começar o programa
os.system("cls")

#aviso
print(colorama.Fore.RED + 'AVISO!!')
print(colorama.Style.RESET_ALL + 'Caso qualquer uma das medidas fiquem sem valor, o programa acusará erro')
print('\n')

#verificando se deseja jogar novamente
calcular_novamente = "s"
#iniciando um loop até que a resposta mude de "s" para "n"
while calcular_novamente == "s":

    #pedindo medidas
    medida_lado_A = float(input('Digite a medida do lado A: '))
    print('\n')
    medida_lado_B = float(input('Digite a medida do lado B: '))
    print('\n')
    medida_lado_C = float(input('Digite a medida do lado C: '))
    print('\n')

    #verificação de existencia
    if medida_lado_B + medida_lado_C < medida_lado_A or medida_lado_A + medida_lado_C < medida_lado_B or medida_lado_A + medida_lado_B < medida_lado_C:
        print(colorama.Fore.RED + 'As medidas Digitadas não formam um triângulo!')
        print('\n')
        print('Tente novamente!')
        print('\n')
        medida_lado_A = float(input(colorama.Style.RESET_ALL + 'Digite a medida do lado A: '))
        print('\n')
        medida_lado_B = float(input('Digite a medida do lado B: '))
        print('\n')
        medida_lado_C = float(input('Digite a medida do lado C: '))

    #calculo perimetro
    perimetro = medida_lado_A + medida_lado_B + medida_lado_C
    #calculo semiperimetro
    semiperimetro = perimetro / 2
    #tirando a raiz
    raiz = math.sqrt(semiperimetro * (semiperimetro - medida_lado_A) * (semiperimetro - medida_lado_B) * (semiperimetro - medida_lado_C))
    #mostrando os resultados 
    print(colorama.Fore.MAGENTA + f"Perímetro: {perimetro}")
    print('\n')
    print(colorama.Fore.GREEN + f"Semiperímetro: {semiperimetro}")
    print('\n')
    print(colorama.Fore.BLUE + f"Resultado: {raiz:.2f}")
    print('\n')

    #perguntando se deseja jogar novamente
    perguntando_calcular_novamente = str(input(colorama.Style.RESET_ALL + 'Deseja calcular novamente? (s/n) '))
    #verificando se a resposta é valida
    while perguntando_calcular_novamente.lower() != 's' and perguntando_calcular_novamente.lower() != 'n':
        print('\n')
        print(colorama.Fore.RED + 'Resposta inválida, tente novamente!')
        print('\n')
        perguntando_calcular_novamente = str(input(colorama.Style.RESET_ALL + 'Deseja calcular novamente? (s/n) '))
    #verificando se a resposta é negativa
    if perguntando_calcular_novamente.lower() == "n":
        calcular_novamente = 'n'
    #limpando o terminar se o usuario desejar calcular novamente
    if perguntando_calcular_novamente.lower() == "s":
        os.system("cls")


print(colorama.Fore.CYAN + 'Feito por Gabriel Belentani Felipe   Nº10    2ºA')
print('\n')
input(colorama.Style.RESET_ALL + 'Pressione qualquer tecla para sair...')
exit()