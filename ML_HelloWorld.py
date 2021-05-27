from sklearn import tree
import fileReader

irregular = 0
lisa = 1

Laranja = 0
Maça = 1

# Dados de treino
pomar = [[150, lisa],[130, lisa],[180, irregular],[160, irregular]]
resultado = [Maça,Maça,Laranja,Laranja]
# 

clf = tree.DecisionTreeClassifier()
clf.fit(pomar, resultado)

if __name__ == '__main__':
    dados = fileReader.read('data.csv')
    for i in range(0,len(list(dados)),2):
        peso = dados[i]
        superficie = dados[i+1]
        
        if superficie == 'lisa':
            superficie = 1
        else:
            superficie = 0

        resultadoExecucao = clf.predict([[peso, superficie]])

        if resultadoExecucao == 1:
            print('É uma maçã!')
        else:
            print('É uma laranja!')


def examinador():
    peso = input('Insira o peso: ')
    superficie = input('Insira o tipo da superfície: ')

    if superficie == 'lisa':
        superficie = 1
    else:
        superficie = 0
    
    resultadoExecucao = clf.predict([[peso, superficie]])

    if resultadoExecucao == 1:
        print('É uma maçã!')
    else:
        print('É uma laranja!')
