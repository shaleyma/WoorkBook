nombre = input ("¿cual es tu nombre?: ")
print ("Bienvenido(a) a SAPITO SALTARIN\n")
print ("Tu mision sera llevar al sapito al otro lado del lago donde encontrara un tesoro\n")
print ("*Reglas: Tendras opcion de ir hacia la {DERECHA} o {IZQUIERDA} si saltas de una hoja a otra y opcion de {SI} y {NO} si tienes que tomar una decision *\n")
print ("*Recuerda: contestar las preguntas en MAYÃšSCULA y con la palabra indicada en cada opciÃ³n que se encuentra escrita tambiÃ©n en MAYÃšSCULA*\n")
print ("**Indicaciones: Tendras que comer los insectos y caracoles que encuentres en el camino, estos te ayudaran a sobrevivir*\n")
print ("\n¡¡Es hora de comenzar la aventura!!\n")
print (nombre + ",Tu sapito se encuentra en laprimera hoja\n")
intento = 0
while (intento == 0):
    direccion = input ("\n¿A que hoja quieres ir?: ")
    if direccion == ("DERECHA"):
        print ("\n ¡Has logrado pasar a la siguiente hoja!\n")
        intento = -1


        print (nombre + ", has encontrado un insecto en esta hoja\n")
       


        intento = 0
        while (intento == 0):
            color = input ("\n¿Quieres comer el insecto?: ")
            if color == ("SI"):
                print ("\n¡Has ganado enegia suficiente para continuar!\n")
                intento = -1


                print ("\n" + nombre + ", Tu sapito pudo pasar a la siguiente hoja")



                intento = 0
                while (intento == 0):
                    arma = input ("\n¿comeras el caracol que se encuentra en esta hoja?: ")
                    if arma == ("SI"):
                        print ("\n !Has ganado mucha energia ¡Tienes un salto doble!\n")
                        intento = -1


                        print ("En la siguiente hoja hay un pez alrededor")




                        intento = 0
                        while (intento == 0):
                            accion = input ("\n¿Quieres esperar a que el pez se vaya?: ")
                            if accion == ("SI"):
                                print ("\n¡Lograste sobrevivir!\n")
                                intento = -1
     
                                
                                print ("te encuentras en la siguiente hoja donde hay un insecto")
                                
                               
                                
                                intento = 0
                                while (intento == 0):
                                    accion = input ("\n ¿Quieres comer el insecto?:")
                                    if accion == ("SI"):
                                        print ("\n¡Puedes continuar!\n")
                                        intento = -1
                                             
                                        
                                        
                                        intento = 0
                                        while (intento == 0):   
                                            accion = input("\n¿A qué hoja quieres ir ahora?: ")
                                            if accion == "derecha":       
                                               print("\n¡¡GANASTE!! " + nombre + "!" + " Te encuentras del otro lado y lograste conseguir el tesoro ¡¡FELICIDADES!!\n")
                                            elif accion == "izquierda":      
                                                 print("\n¡Te has resbalado! " + nombre + "!" + "caíste al agua\n")
                                            else:       
                                                 print("\n*Entrada inválida*")
                                                 intento = -1
                                               
                                    
                                    elif accion == "NO":       
                                         print("\n No tienes energía suficiente para continuar \n")
                                    else:        
                                        print("\n*Entrada inválida*")
                                        intento = -1
                                            

                            elif accion == ("NO"):
                                print ("\nPERDISTE: ¡Fuiste comido por el pez!")
                                intento = -2
                            else:
                                print ("\n*Entrada invalida*")


                    elif arma == ("NO"):
                        print ("\nPERDISTE: No tienes energia suficiente para continuar ")
                        intento = -2
                    else:
                        print ("\n*Entrada invalida*")


            elif color == ("NO"):
                print ("\nPERDISTE: Has encontrado un obstaculo y no tienes energia suficiente para continuar" + nombre + "¡Has perdido energia al no comer el insecto! ")
                intento = -2
            else:
                print ("\n*Entrada invalida*")


    elif direccion == ("IZQUIERDA"):
        print ("\nPERDISTE: " + nombre + "¡Brincaste encima de  una  hoja débil!  caíste al agua")
        intento = -2
    else:
        print ("\n*Entrada invalida*")