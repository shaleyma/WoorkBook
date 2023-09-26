class SapitoSaltarin:
    def __init__(self):       
        self.nombre = input("¿Cuál es tu nombre?:")
    def iniciar_juego(self):
        print(self.nombre, "Bienvenido(a) a SAPITO SALTARIN")       
        print("Tu misión será llevar al sapito al otro lado del lago donde encontrará un tesoro\n")
        print("*Reglas: Tendrás opción de ir hacia la {DERECHA} o {IZQUIERDA} si saltas de una hoja a otra y opción de {SI} y {NO} si tienes que tomar una decisión *")        
        print("*Recuerda: contestar las preguntas en MAYÚSCULA*\n")
        print("*Indicaciones: Tendrás que comer los insectos y caracoles que encuentres en el camino, estos te ayudarán a sobrevivir*")       
        print("¡Es hora de comenzar la aventura!")
    
    def parte1(self):
        print(self.nombre, "Tu sapito se encuentra en la primera hoja")

        intento = 0        
        while (intento == 0):
            direccion = input("\n¿A qué hoja quieres ir?: ")            
            if direccion == "DERECHA":
                print("\n¡Has logrado pasar a la siguiente hoja!\n")                
                return()        
            else:
                print("\nPERDISTE:", self.nombre, "¡Brincaste encima de una hoja débil! Caíste al agua") 
                exit()

    def parte2(self):       
        print(self.nombre, ", has encontrado un insecto en esta hoja")
        intento = 0       
        while intento == 0:
            accion = input("\n¿Quieres comer el insecto?: ")            
            if accion == "SI":
                print("\n¡Has ganado energía suficiente para continuar!\n")               
                return()
           
            else:
                print("\nPERDISTE: Has encontrado un obstáculo y no tienes energía suficiente para continuar", self.nombre, "¡Has perdido energía al no comer el insecto!")
                exit()       

    def parte3(self):   
        print("\n", self.nombre, ", Tu sapito pudo pasar a la siguiente hoja")      
        intento = 0
        while intento == 0:            
            accion = input("\n¿Comerás el caracol que se encuentra en esta hoja?: ")
            if accion == "SI":                
                print("\n ¡Has ganado mucha energía! ¡Puedes continuar!\n")
                return()           
            else:                
                print("\nPERDISTE: No tienes energía suficiente para continuar ")
                exit()

    def parte4(self):
         print("En la siguiente hoja hay un pez alrededor")
    
         intento = 0        
         while intento == 0:
            accion = input("\n¿Quieres esperar a que el pez se vaya?: ")           
            if accion == "SI":
                print("\n¡Lograste sobrevivir!\n")                
                return ()           
            else:
                print("\nPERDISTE: ¡Fuiste comido por el pez!")
                exit()

    def parte5(self):               
         print("Te encuentras en la siguiente hoja donde hay un insecto")

         intento = 0        
         while intento == 0:
            accion = input("\n¿Quieres comer el insecto?:")           
            if accion == "SI":
                print("\n¡Puedes continuar!\n")                
                return()
            else:               
                print("\nPERDISTE: ¡No tienes energía suficiente para continuar! \n")
                exit()

    def ParteFinal(self):        
        print("\n", self.nombre, ", Tu sapito pudo pasar a la siguiente hoja")
        intento = 0        
        while intento == 0:
            accion = input("\n¿A qué hoja quieres ir ahora?: ")           
            if accion == "DERECHA":
                print("\n¡¡GANASTE!!", self.nombre, "!" + " Te encuentras del otro lado y lograste conseguir el tesoro ¡¡FELICIDADES!!\n")
                return()
            else:                
                print("\nPERDISTE: ¡Te has resbalado!", self.nombre, "!" + "caíste al agua\n")
                exit()


if __name__ == "__main__": 
    juego = SapitoSaltarin() 
    juego.iniciar_juego()  
    juego.parte1() 
    juego.parte2() 
    juego.parte3() 
    juego.parte4() 
    juego.parte5()
    juego.ParteFinal()