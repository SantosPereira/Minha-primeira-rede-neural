'''
README:

O esquema básico de uma rede neural é ter uma entrada de dados, dar pesos a cada grupo de dados e fazê-los passar pelos neurônios.
Os nerônios são portões lógicos, de acordo com o que são programados vão testar condições lógicas como if, else, ==, !=, >, <, =>, =<.
E vão dar como saída outros valores, como True, False, 0, 1, ou qualquer outro valor.
'''
'''
Nesse link tem um exemplo:
https://www.youtube.com/watch?v=NZlIYr1slAk&t=50s
'''

###         O exemplo abaixo controla se um carro vai para a direita ou esquerda e se acelera

from time import sleep

### entrada de dados

direita = 10 # distância até a parede direita
esquerda = 15 # distância até a parede esquerda
frente = 20 # distância até a parede

right = False
left = False
xlr8 = False

################# neurônio
while True:
    sleep(0.25)
    if frente < 3:
        right = True
        xlr8 = True
    else:
        left = True
        xlr8 = True
    print(right)
    print(left)
    print(xlr8)
        
    right = False
    left = False
    xlr8 = False

