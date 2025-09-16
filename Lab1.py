#!Similitud Coseno para 2 usuarios iterada a 3

# Calificaciones de Pepito
PSherk = 5
PJackass = 5

# Calificaciones Ramona
RSherk = 1
RJackass = None

# Calificaciones Yakitori
YSherk = 4
YJackass = 2

# Similitud entre pepito y ramona
numerador =  PSherk * RSherk
denominador = (PSherk**2)**0.5  * (RSherk**2)**0.5
similitud = numerador/denominador


#Similitud entre pepito y yakitori
numerador2 = PSherk * YSherk 
denominador2 = (PSherk**2)**0.5 * (YSherk**2)**0.5

similitud2 = numerador2/denominador2


#Prediccion Ramona
prediccionR = (similitud * PJackass + similitud2 * YJackass) / (similitud + similitud2)

#Resultados de la prediccion
print("La prediccion de Ramona es: ", round(prediccionR,2))