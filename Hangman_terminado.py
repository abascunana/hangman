import random #importar función predefinida para valores
fruta = ["pera", "uva","lima","kiwi","limon"] #lista de palabras a adivinar por el juego

seleccion = None #la palabra correct #es igual a None para poder hacer uso de esta variable en varias funciones sin que intervenga lo que se haya declaradoo en un principio,seguir leyendo programa para más información
Despedida = False #Esta variable define si se quiere terminar el juego o no, es False porque si fuera True no nos dejaría hacer nada desde el principio

def menu(): #menú inicial del juego en el que se declara la palabra a adivinar
 
 menu = input("menú del ahorcado \nquieres jugar con una palabra de tu elección o con un diccionario aleatorio?  definir/aleatorio\n") #te pide si quieres definir la palabra a adivinar o una aleatoria ddel programa
 while menu != "aleatorio" or menu != "definir" : # si no es ninguna de las dos cosas no te deja continuar
     if menu == "aleatorio": # si es "aleatorio" declara la variable "seleccion" como una de la lista "fruta" e inicia el juego con esos valores en cuenta.Sale del bucle para que el menu no interfiera con el juego
         global seleccion
         seleccion = random.choice(fruta)
         #página utilizadahttps://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
         print(" /$$$$$$$$ /$$                 /$$                                                     /$$                ")
         print("| $$_____/| $$                | $$                                                    | $$                ")
         print("| $$      | $$        /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$       ")
         print("| $$$$$   | $$       |____  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$_____/ |____  $$ /$$__  $$ /$$__  $$")
         print("| $$__/   | $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/| $$        /$$$$$$$| $$  | $$| $$  \ $$      ")
         print("| $$      | $$       /$$__  $$| $$  | $$| $$  | $$| $$      | $$       /$$__  $$| $$  | $$| $$  | $$      ")
         print("| $$$$$$$$| $$      |  $$$$$$$| $$  | $$|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/      ")
         print("|________/|__/       \_______/|__/  |__/ \______/ |__/       \_______/ \_______/ \_______/ \______/      ")
         juego()
         break
 
     elif menu == "definir": # si es definir declara la variable "seleccion" como una a tu elección e inicia el juego con esos valores en cuenta.Sale del bucle para que el menu no interfiera con el juego
         seleccion = input("selecciona tu palabra,recuerda que sólo puede contener minúsculas y sin barrabasbajas.\n")

         #página utilizada https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
         print(" /$$$$$$$$ /$$                 /$$                                                     /$$                ")
         print("| $$_____/| $$                | $$                                                    | $$                ")
         print("| $$      | $$        /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$       ")
         print("| $$$$$   | $$       |____  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$_____/ |____  $$ /$$__  $$ /$$__  $$")
         print("| $$__/   | $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/| $$        /$$$$$$$| $$  | $$| $$  \ $$      ")
         print("| $$      | $$       /$$__  $$| $$  | $$| $$  | $$| $$      | $$       /$$__  $$| $$  | $$| $$  | $$      ")
         print("| $$$$$$$$| $$      |  $$$$$$$| $$  | $$|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/      ")
         print("|________/|__/       \_______/|__/  |__/ \______/ |__/       \_______/ \_______/ \_______/ \______/      ")
        
        
        
        
         if seleccion == "":
             print("no se puede adivinar la nada")
             break
         juego()
         break
     else: #te indica los únicos valores admitidos en la función y vuelve a pedir la variable menu
         print("selecciona 'aleatorio' o 'definir', no se permite nada más ")
         menu = input("¿quieres jugar con una palabra de tu elección o con una palabra aleatoria?  definir/aleatorio\n")
 
def listpal(palabra): #esta función hace lo mismo que el list() pero en strings
 x = []
 e = palabra # "e" será igual a la palabra que se introduzca en listpal(input(..))
 for i in range(len(e)): # bucle que revisa la largaria de "palabra"
     x = x + [e[i]] #append de todas las letras en "palabra"
 return x  #el resultado final será x,por lo que se le hace un return

def rep():
    global Despedida #en el global Despedida es definida como True debido a que no queremos salir desde el principio,esto cambiará dependiendo de las decisiones que tomemos en esta función
 # si despedida es False hace este bucle
    rep= input("quieres volver a jugar al ahorcado? si/no\n") #repetir el juego
    while rep != "si" or rep != "no" : #selección
        if rep == "si": # si rep es si inicia el menú del juego,mediante el cual puedes iniciar el juego en sí
            menu()
            break
        elif rep == "no": # si es "no" se despide y sale del blucle
            Despedida = True #si Despedida es True,marca la orden de salir del programa y sale del bucle
            print("Adiós")
            break
        else:
            print("introduce 'si' o 'no',no se permite nada más")
            rep= input("quieres volver a jugar al ahorcado? si/no\n")
    salir = Despedida
    return(salir)

def juego(): #el juego en sí  #caracteres especiales que no se tendrán que adivinar,viene
 mayac = ["A","À","á","à","â","Á", "E","È","é","è","ê","É", "I","í","Ì","Í", "O","ó","ò","Ò", "Ù","U","ú","ù","_"] #lista de letras mayúsculas y acentuadas
 num_intents = 0 #num de intentos inicial
 global fruta # lista de fruta
 repet = [] #lista vacía en la que se guardarán los inputs del usuario
 global seleccion # selección (cambiada por otras funciones) (palabra correcta)
 disec = listpal(seleccion) # palabra correcta diseccionada en una lista
 for i in range(len(disec)): #función busca esas letras en la palabra correcta y las cambia por minúsculas
    while disec[i] in mayac[0:6] : 
        disec[i] = "a"
    while disec[i] in mayac[6:12] :
        disec[i] = "e"
    while disec[i] in mayac[12:16] :
        disec[i] = "i"
    while disec[i] in mayac[16:20] :
        disec[i] = "o"
    while disec[i] in mayac[20:24] :
        disec[i] = "u"
    while disec[i] in mayac[24] : #he puesto esto para que cambie las barrabajas por espacio,debido a que además la palabra correcta no puede contener barrasbajas
        disec[i] = " "
    
 num_intents = 0  # empezamos con 0 intentos

 stickman = input("escribe en nombre de tu stickman\n") 
 while len(stickman) > 7:
        print("el nombre de tu stickman no puede ser de más de 7 carcteres")
        stickman = input("escribe en nombre de tu stickman\n") 

 print("Bienvenido al juego del ahorcado,tienes 6 intentos,recuerda,no puedes introducir más de una letra")
 barrabaja = len(disec) * "_" # barrabajas de la largaria de la palabra correcta
 i=0
 z = (listpal(barrabaja)) #hago un listpal de barrabaja debido a que no se puede sustituir un string en python
 for i in range(len(disec)):  

    if disec[i] not in [" ",".",":",";","(",")","=","!","¡",",","\"","\\","/"] : #si letra no está en estos elementps no hace nada
        z=z
    else:
        z[i]=disec[i] #de otra forma el string de barrabajas es igual a la coincidencia de caracteres especiales
    

 for i in range(len(seleccion)):
   if Despedida == False : 
        while "_" in z: #mientras no hayas ganado haz este bucle
         print("\n")
         
         mensaje= "adivina una letra: "
         
         print(z)
         letra = input(mensaje)
         if len(letra) > 1:
                 print("no se puede introducir más de una letra")
         
         repet = repet + [letra]
         
         i= 1
        
         
         if letra not in disec:
             num_intents +=1
         else:
           for i in range(len(disec)): # bucle que revisa la largaria de lista x
               if letra == disec[i]: #si letra está localizada en el elemento de seleccion
                z[i] = letra #concatena la letra adivinada en la posición necesaria en z
                i+=1
           print("vas bien")
           
           
                
         if "_" not in z:
           print("Ganaste :D",stickman,"está a salvo")
           print("    {}")
           print("   /__\"") #trofeo al ganar
           print(" /|    |\"")
           print("(_|    |_)") 
           print("   \  /")  
           print("    )(") 
           print("  _|__|_")
           print("_|______|_") 
           print("|__________|")            
           print(disec,"la palabra correcta","\n",repet,"lo que has introducido")
           rep()
           break
         
 #palo inicial del monigote, no cambia por lo que se deja siempre fuera del condicional
         print ("__________")
         print ("|        |")
 
          #cada if imprime el proceso del cuerpo del monigote dependiendo del número de intentos,desde el palo vacío hasta el cuerpo entero
         if num_intents == 0:
                 print ("|")
                 print ("|")
                 print ("|")
         elif num_intents == 1:
     
                     print ("|        O")
                     print ("|")
                     print ("|")
         elif num_intents == 2:               
             print ("|        O")
             print ("|         |")
             print ("|")
         elif num_intents == 3:
              print ("|        O")
              print ("|       /|")
              print ("|")
         elif num_intents == 4:
             print ("|        O")
             print ("|       /|\ ")
             print ("|")
         elif num_intents == 5:
             print ("|        O")
             print ("|       /|\ ")
             print ("|       / ")
         elif num_intents == 6:
                         
             print ("|        O")
             print ("|       /|\ ")
             print ("|       / \ ")
 
         print ("|")
         print ("|___")
         print(repet,"letras ya introducidas") #palo final del monigote, no cambia por lo que se deja siempre fuera del condicional
         
         if num_intents == 6:
            print(disec,"la palabra correcta","\n",repet,"lo que has introducido")
            print("Has perdido :C, no has podido salvar a ",stickman)
            print("    _____")
            print("  /~/~   ~\"") #tumba en el caso de que pierdas
            print(" | |       \"")
            print(" \ \         \"")
            print("  \ \"",stickman   ,"\"")
            print(" --\ \       .\''")
            print("--==\ \     ,,i!!i,")
            print("----------------------")
            rep()
            break
            
     


menu()


