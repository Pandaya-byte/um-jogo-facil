
import random

print('você vai rolar o dado? (s/n)')
aki = input('digite aki:')
s = 's'
n = 'n'
if aki == s:
    print('seu número é', random.randint(1, 6))
elif aki == n:
    print('que pena talvez na proxima vez (^^)/')
else:
    print('o você não digitou nem "s" nem "n"')
# acao = int(input("Digite '1' para sim e digite '2' para não: "))
# if(acao==1):
#     print("Você disse que sim!")
# else:
#     if(acao==2):
#         print("Você disse que não!")
#     else:
#         print("O número digitado não é '1' e nem '2'!!!")
