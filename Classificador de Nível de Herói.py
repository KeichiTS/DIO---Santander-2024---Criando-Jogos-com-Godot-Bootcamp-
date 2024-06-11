# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:18:31 2024

@author: KeichiTS
"""

#1 Desafio Classificador de nível de Herói

var_heroi = ['DIOnizio', 9000]

if var_heroi[1] <= 1000:
    elo = 'Ferro'
    
elif var_heroi[1] >= 1001 and var_heroi[1] <= 2000:
    elo = 'Bronze'
    
elif var_heroi[1] >= 2001 and var_heroi[1] <= 5000:
    elo = 'Prata'
    
elif var_heroi[1] >= 5001 and var_heroi[1] <= 7000:
    elo = 'Ouro'

elif var_heroi[1] >= 7001 and var_heroi[1] <= 8000:
    elo = 'Platina'

elif var_heroi[1] >= 8001 and var_heroi[1] <= 9000:
    elo = 'Ascendente'

elif var_heroi[1] >= 9001 and var_heroi[1] <= 10000:
    elo = 'Imortal'
    
elif var_heroi[1] > 10000:
    elo = 'Radiante'
    
print('O Herói de nome ' + var_heroi[0] + ' está no nível de ' + elo)