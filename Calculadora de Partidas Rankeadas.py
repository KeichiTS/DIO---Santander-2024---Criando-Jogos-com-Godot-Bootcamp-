# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:34:06 2024

@author: KeichiTS
"""

vitorias = 100
derrotas = 40

def status_ranked(vitorias, derrotas):
    saldoVitorias = vitorias - derrotas
    
    if saldoVitorias <= 10:
        nivel = 'Ferro'
    elif saldoVitorias >= 11 and saldoVitorias <= 20:
        nivel = 'Bronze'
    elif saldoVitorias >= 21 and saldoVitorias <= 50:
        nivel = 'Bronze'
    elif saldoVitorias >= 51 and saldoVitorias <= 80:
        nivel = 'Bronze'
    elif saldoVitorias >= 81 and saldoVitorias <= 90:
        nivel = 'Bronze'
    elif saldoVitorias >= 91 and saldoVitorias <= 100:
        nivel = 'Bronze'
    else:
        nivel = 'Imortal'
        
    print("O Herói tem de saldo de " + str(saldoVitorias) + " está no nível de " + nivel)
    
status_ranked(vitorias, derrotas)