# 1- Utilizando a biblioteca numpy, crie uma matriz 4x4 com valores 1
import numpy as np

matrizT = np.ones((4,4), dtype=float)

print(matrizT)
# 2 - Com numpy, crie uma matriz de tamanho 6x6 com valores aleatórios
matrizcu = np.ones((6,6), dtype=float)
for i in range (6):
    for j in range (6):
        matrizcu[i][j] = np.random.randint(0, 12)
print (matrizcu)
# 3 - Pesquise uma biblioteca que pegue dados de algum site da web, então puxe dados sobre o covid de algum site de sua
# preferência
from bs4 import BeautifulSoup
python myfile.py


# 4 - Faça um programa que leia a quantidade de alunos em uma turma, então pegue seus nomes, notas e calcule a média,
# armazenando estes valores em uma matriz e salvando em um arquivo json posteriormente


# 5 - Com a biblioteca pandas, monte um gráfico com os dados passados pelo instrutor

# 6 - Faça um programa que sorteie um número entre 1 e 99 com a biblioteca numpy,
# então armazene o valor em um arquivo .txt

# 7 - Faça um programa que calcule a mediana de uma matriz criada pelo próprio programador com
# com valores aleatórios

# 8 - Faça um programa que descubra o maior valor em uma matriz numpy [NxN] (o usuário define o tamanho) criada com valores aleatórios

numero1 = int(input("Digite um valor X para matriz: "))
numero2 = int(input("Digite um valor Y para a matriz: "))
matrizpe = np.ones((numero1,numero2), dtype=float)
for i in range (numero1):
    for j in range (numero2):
     matrizpe[i][j] = np.random.randint(0,9)


maiorvalor = np.max(matrizpe)
print(matrizpe)
print(maiorvalor)




