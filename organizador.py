"""
programa organiza arquivos
Descrição: programa em Python que cria diretórios com nome 'documentos' e 'planilhas'
e move arquivos existentes paras os diretórios criados
utilizando a função OS e Shutil
Data:03/09/2022
Autor: vânia
versão:0.0.1
"""

import shutil
import os

#função cria diretorios 'documentos' e 'planilhas'

def criadiretorio():
    if os.path.exists('documentos')==False:
        os.mkdir('documentos')

    if os.path.exists('planilhas')==False:
        os.mkdir('planilhas')
    
#função move arquivo para os diretórios criados

def movearquivo():
    arquivos = os.listdir()
    for arquivo in arquivos:
        if ".xls" in arquivos:
            shutil.move(arquivo,f"./planilhas/{arquivo}")
        elif ".doc" in arquivos:
            shutil.move(arquivo,f"./documentos/{arquivo}")
        
#execução do programa

def main():
    criadiretorio()
    movearquivo()

if __name__ == "__main__":
    main()
