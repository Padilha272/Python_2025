"""
a = input('Digite o valor de a: ')
b = input('Digite o valor de b: ')
c = input('Digite o valor de c: ')

"""

print(12,34,2003, sep = '-', end = '##\n')
print(12,34,2003, sep = '-', end = '\n##')
print(56,78, sep = "-")
#print(a,b,c, sep = "   ")


def testes(a):
    if a%2==0:
        print("Par")
    else:
        print("impar")

testes(3)