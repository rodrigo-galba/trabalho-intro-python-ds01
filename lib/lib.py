"""
Testes unitários para o módulo lib
"""
import os
import gdown
import hashlib

def download_dataset(link_txt, file_name):
    """
       Baixa um arquivo do serviço Google Drive.

       Args:
           link_txt (str): Link do arquivo no Google Drive.
           file_name (str): Nome do arquivo a ser baixado.
       """
    gdown.download(link_txt, file_name, quiet=False, fuzzy=True)

    if not os.path.exists(file_name):
        print(f"Arquivo '{file_name}' não encontrado.")
        return None

    with open(file_name, 'rb') as f:
        data = f.read()

    # Calcula o checksum do arquivo baixado
    calculated_checksum = hashlib.md5(data).hexdigest()
    # Valor fixo de checksum
    # Para calcular no shell, use md5sum $nome_arquivo | cut -d ' ' -f 1
    expected_checksum = "492427a42d710dfef65e41bcc592d64d"

    if expected_checksum != calculated_checksum:
        print(f"Checksum do arquivo não coincide: {expected_checksum} ≠ {calculated_checksum}")
        return None

    print(f"Checksum do arquivo coincide. Arquivo '{file_name}' é válido.")

    return None

def preencher_matriz_contratos(nome_arquivo: str):
    """
    Processa um arquivo com uma lista de contratos e
    retorna uma matriz contendo os dados dos contratos por fornecedor.
    :param nome_arquivo:
    :return:
    """
    # Converter as linhas de um arquivo em uma lista
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()

    # Ler a primeira linha
    cabecalho = linhas[0].split()
    m = cabecalho[0]
    n = cabecalho[1]
    t = cabecalho[2]

    # Remover a primeira linha
    linhas = linhas[1:]
    # Inicializa lista de contratos por fornecedor
    contratos = processa_contratos(linhas)
    return m, n, t, contratos

def processa_contratos(linhas):
    """
    Processa uma lista de contratos e
    retorna uma matriz contendo os dados dos contratos por fornecedor.
    :param linhas:
    :return:
    """
    fornecedores = inicializa_fornecedores(linhas)

    for i in range(len(linhas)):
        dados = linhas[i].split()
        codigo_fornecedor = int(dados[0]) - 1
        mes_inicio = int(dados[1])
        mes_fim = int(dados[2])
        valor = float(dados[3])
        fornecedores[codigo_fornecedor][mes_inicio][mes_fim] = valor

    return fornecedores

def inicializa_fornecedores(linhas):
    """
    Inicializa uma lista de fornecedores com meses iniciais, finais e valores de contrato.
    :param linhas:
    :return:
    """
    # Extrai valores unicos de cada linha
    fornecedores = set()
    for linha in linhas:
        dados = linha.split()
        codigo_fornecedor = int(dados[0])
        fornecedores.add(codigo_fornecedor)
    # Converter Set para List
    fornecedores = list(fornecedores)
    # Ordenar fornecedores por codigo
    fornecedores.sort()

    for i in range(len(fornecedores)):
        meses_inicio = []
        # Inicializa mes de inicio com 12 meses + 1
        for j in range(13):
            meses_inicio.append(list([float('inf')] * 13))
        fornecedores[i] = meses_inicio

    return fornecedores

def imprimir_matriz(matriz, k=None):
    """
    Exibe a matriz no console.
    :param matriz:
    :param k:
    :return:
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\n')
        print()
    return None

def exportar_csv(nome_arquivo, matriz):
    """
    Exporta uma matriz para um arquivo CSV.
    :param nome_arquivo:
    :param matriz:
    :return:
    """
    diretorio = nome_arquivo.split('/')[0]

    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)

    with open(nome_arquivo,'w', newline='') as file:
        # Escrever os dados da matriz em cada linha
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                file.write(str(matriz[i][j]) + ',')
            file.write(str('\n'))
    file.close()
    return None
