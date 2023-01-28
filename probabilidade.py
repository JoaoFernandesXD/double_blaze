import pandas as pd
import random
from login import *
URL = 'https://www.historicosblaze.com/br/blaze/doubles'

ler = pd.read_csv('historico.csv', sep=';')
cores = ler['cor'].tolist()

def probabilidade():

    historico = cores

    #calculando frequencia relativa
    frequencia_relativa = pd.Series(historico).value_counts(normalize=True)

    #calculando probabilidade
    probabilidade = frequencia_relativa.to_dict()

    #criando funcao para simular proxima rodada
    print('Analisando os Dados')
    def proxima_rodada(probabilidade):
        sorteio = random.choices(list(probabilidade.keys()), weights=probabilidade.values(), k=1)
        return sorteio[0]

    for i in range(5):
        print(f'Pode Apostar no ',proxima_rodada(probabilidade))


def main():
    login()
    probabilidade()

if __name__ == '__main__':
        main()
    






