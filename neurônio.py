'''
README:

O esquema básico de uma rede neural é ter uma entrada de dados, dar pesos a cada grupo de dados e faze-los passar pelos neurônios.
Os nerônios são portões lógicos, de acordo com o que são programados vão testar condições lógicas como if, else, ==, !=, >, <, =>, =<.
E vão dar como saída outros valores, como True, False, 0, 1, ou quaser outro valor.
'''
'''
Nesse link tem um exemplo:
https://www.youtube.com/watch?v=NZlIYr1slAk&t=50s
'''

###         O exemplo abaixo controla se um carro vai para a direita ou esquerda e se acelera


### entrada de dados
in1 = 10 #in == input data
in2 = 15
in3 = 20

##################### pesos
in1 = in1*1.1
in2 = in2*1.5
in3 = in3*1.7

################# neurônios
def tico():
    if in1 >= 11:
        right = True
    else:
        right = False

    if in2 >= 15:
        left = True
    else:
        left = False

    if in3 >= 27:
        xlr8 = True #acelerate
    else:
        xlr8 = False
def teco():
    pass
