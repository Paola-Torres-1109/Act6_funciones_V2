print("Mas sobre funciones")
#Aqui se escriben las funciones 
def suma_ab(a,b):
    s=a+b
    return s

def res_cd(c,d):
    r=c-d
    return r

def mult_ef(e,f):
    m=e*f
    return m

def div_gh(g,h):
    d=g/h
    return d


#Llamadas a funciones
print("Calculando suma")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma= suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es {suma}")

print("")
print("Calculando resta")
n3=int(input("Ingresa el primer numero "))
n4=int(input("Ingresa el segundo numero "))
resta= res_cd(n3,n4)
print(f"La resta de {n3} - {n4} es {resta}")

print("")
print("Calculando multiplicaion")
n5=int(input("Ingresa el primer numero "))
n6=int(input("Ingresa el segundo numero "))
mult= mult_ef(n5,n6)
print(f"La multiplicacion de {n5} * {n6} es {mult}")

print("")
print("Calculando division")
n7=float(input("Ingresa el primer numero "))
n8=float(input("Ingresa el segundo numero "))
div= div_gh(n7,n8)
print(f"La division de {n7} / {n8} es {div}")
