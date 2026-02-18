from statistics import mean

media = mean([100, 90])
print(media)

'''
# Libreria Statistics
La biblioteca statistics es un módulo integrado en Python (desde la versión 3.4) diseñado para realizar cálculos estadísticos básicos sobre datos numéricos reales. 

A diferencia de bibliotecas externas como NumPy o Pandas, statistics está enfocada en el nivel de calculadoras científicas y es ideal para conjuntos de datos pequeños donde no se quieren instalar dependencias adicionales. 

# Funciones Principales
Según la documentación oficial de Python, estas son sus herramientas más comunes: 

# Medidas de Tendencia Central:
mean(): Media aritmética ("promedio").
fmean(): Media aritmética rápida de punto flotante.
median(): Mediana (valor central).
mode(): Moda (el valor más frecuente).
multimode(): Devuelve una lista con todas las modas encontradas.

# Medidas de Dispersión:
stdev(): Desviación estándar de una muestra.
variance(): Varianza de una muestra.
pstdev(): Desviación estándar de una población.
quantiles(): Divide los datos en intervalos con igual probabilidad.

# Relación entre Variables:
correlation(): Coeficiente de correlación de Pearson.
covariance(): Covarianza de una muestra para dos variables.
linear_regression(): Devuelve la pendiente e intersección de una regresión lineal simple.
'''