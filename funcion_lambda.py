'''Una funcion lambda es una funcion anonima, se utiliza a la hora de programar para abreviar, 
consiste en resumir una funcion normal en una expresion lambda, todo lo que podemos hacer en
una funcion lambda se puede hacer con una funcion normal pero no todo lo que se puede hacer
en una funcion normal se puede hacer en una expresion lambda'''

#Ej:

'''def area_triangulo(base,altura):

	return(base*altura)/2

 
triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(5,5)


print(triangulo1)
print(triangulo2)#Con el uso del lambda vamos a simplicar esto.'''
#No se puede hacer funciones lambda donde hayan condicionales o bucles, solo cosas sencillas
area_triangulo=lambda base,altura: (base*altura)/2 #Asi es una funcion lambda

print(area_triangulo(2,7))
print(area_triangulo(5,7))

#-----Mas ejemplos-----
al_cubo=lambda numero: pow(numero, 3)#El pow hará que el primer numeros sea el que se vaya a multiplicarse por si mismo las veces que le digas en el segundo parametro(el exponente).

destacar_valor = lambda comision:"¡{}! $".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))