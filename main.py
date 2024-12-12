
"""
Modulo principal.
Trabalho 01 da disciplina Introdução a Python
Curso Ciencia de Dados, turma 9, Unifor
"""
from lib import download_dataset
from lib import preencher_matriz_contratos
from lib import imprimir_matriz
from lib import exportar_csv

def main():
    """
        Função principal.
        Baixa arquivo de dados.
        Processa contratos por fornecedor.
        Exporta arquivo de contratos CSV.
    """
    # Download do dataset
    link_txt = "https://drive.google.com/file/d/1YjPaHv8aAVsXNzhHxum5gyUDFfY5iw1_/view?usp=sharing"
    file_txt = 'dataset/entrada.txt'
    #file_txt = 'dataset/entradagrande.txt'
    download_dataset(link_txt,file_txt)

    # Preencher a matriz de contratos
    m, n, t, matriz = preencher_matriz_contratos(file_txt)

    # Imprimir os resultados
    print(m, n, t, "\n")
    imprimir_matriz(matriz)

    # Exportar a matriz de contratos
    file_csv = "resultados/contratos.csv"
    #file_csv = "resultados/contratosgrande.csv"
    exportar_csv(file_csv, matriz)

if __name__ == "__main__":
    main()
