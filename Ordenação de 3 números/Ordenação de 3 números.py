a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
maior: int
menor: int
medio: int

if a>b and a>c:
    maior = a
elif b>c and b>a:
    maior = b
else:
    maior = c

if a<b and a<c:
    menor = a
elif b<a and b<c:
    menor = b
else:
    menor = c

if b<a<c or c<a<b:
    medio = a
elif a<b<c or c<b<a:
    medio = b
else:
    medio = c

print(f"{menor}, {medio} e {maior}")