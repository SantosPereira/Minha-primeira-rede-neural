import csv
data = []
def read(filepath):
    file = open(filepath, 'r')
    read = csv.reader(file)
    for linha in read:
        for i in range(0,11):
            linha = str(linha).replace('"','')
            linha = str(linha).replace("'",'')
            linha = str(linha).replace("[",'')
            linha = str(linha).replace("]",'')
            linha = str(linha).replace(",",'')
        linha = linha.split()
        data.append(int(linha[0]))
        data.append(linha[1])
    return data
