#!Similitud Coseno para 2 usuarios iterada a 3 y predicción


#Calificaciones de Pepito
PSherk = 5
PJackass = 5

#Calificaciones Ramona
RSherk = 1
RJackass = None

#Calificaciones Yakitori
YSherk = 4
YJackass = 2


#Similitud entre pepito y ramona
numerador =  PSherk * RSherk
denominador = (PSherk ** 2) ** 0.5 (RSherk ** 2)** 0.5
similitud = numerador/denominador

#Similitud entre Yakitori y ramona
numerador = YSherk * RSherk 
denominador = (YSherk ** 2) ** 0.5 (RSherk ** 2) ** 0.5
similitud_2 = numerador/denominador 

#Prediccion de Ramona(Jackass):


# El numerador es la suma de las calificaciones de los otros para 'Jackass', ponderadas por su similitud
numerador_prediccion = (similitud * PJackass) + (similitud_2 * YJackass)
# El denominador es la suma de las similitudes
denominador_prediccion = similitud + similitud_2 
# La predicción es la división de ambos.
prediccion_RJackass = numerador_prediccion / denominador_prediccion
