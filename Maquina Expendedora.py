import numpy as np
print ("Menú")
productos=np.array([["Papas 0,50$","Doritos 0,75$","Chifles 0,80$"],["Agua 0,45$","Gaseosa 1$","Jugo 0,75$"],["Chocolate 0,95$","Chicles 0,60$","Yogurt 0,30$"]])
print (productos)
producto=input("Porfavor selecciona tu producto:")
pago=int(input("Introduzca su dinero, recuerde que la máquina solo recibe monedas de 5ctvs, 10ctvs, 25ctvs, 50ctvs y 1$:"))
if producto=="papas":
      while True:
            if pago>=50:
                  print("Gracias por su compra")
                  cambio=(pago-50)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(50-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="doritos":
      while True:
            if pago>=75:
                  print("Gracias por su compra")
                  cambio=(pag-75)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(75-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="chifles":
      while True:
            if pago>=80:
                  print("Gracias por su compra")
                  cambio=(pago-80)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(80-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="agua":
      while True:
            if pago>=45:
                  print("Gracias por su compra")
                  cambio=(pago-45)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(45-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="gaseosa":
      while True:
            if pago>=1:
                  print("Gracias por su compra")
                  cambio=(pago-1)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(1-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="jugo":
      while True:
            if pago>=75:
                  print("Gracias por su compra")
                  cambio=(pago-75)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(75-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="chocolate":
      while True:
            if pago>=95:
                  print("Gracias por su compra")
                  cambio=(pago-95)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(95-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="chicles":
      while True:
            if pago>=60:
                  print("Gracias por su compra")
                  cambio=(pago-60)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(60-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break
if producto=="yogurt":
      while True:
            if pago>=30:
                  print("Gracias por su compra")
                  cambio=(pago-30)
                  print ("Su cambio es: "+str(cambio))
                  break
            else:
                  faltante=(30-pago)
                  print ("Ingresa "+str(faltante),"ctvs para completar tu compra")
                  dinero=int(input("Introduce el dinero:"))
                  print ("Su cambio es:"+str(dinero-faltante))
                  break

              
            
              


