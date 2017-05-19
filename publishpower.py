import random
import time
import paho.mqtt.client as mqtt
cont = 0
maxcounts= 60
# xs = []
energy = 0
mqttc= mqtt.Client("python_pub")
mqttc.connect("10.0.0.50",1883)
print("coneccted")
# vara = random.randint(1,28)
# mqttc.publish("panels/amp",str(vara))
# print("Amps: "+str(vara))
while True:
   varv = random.randint(10,12)
   vara = random.randint(1,28)
   varr = random.randint(10,20)
   varaca = random.randint(1,20)
   var_text = random.randint(15,30)
   var_tint = random.randint(15,25)
   varp = varv*vara
   varacp = 220*varaca
   mqttc.publish("panels/voltage",str(varv))
   print("Volts: "+str(varv))
   mqttc.publish("panels/amp",str(vara))
   print("Amps: "+str(vara))
   mqttc.publish("panels/power", str(varp))
   print("Power: "+str(varp))
   mqttc.publish("panels/radiation", str(varr))
   print("Radiation: "+str(varr))
   mqttc.publish("temp/exterior", str(var_text))
   print("Temp exterior: "+str(var_text))
   mqttc.publish("temp/interior", str(var_tint))
   print("Temp interior: "+str(var_tint))
   mqttc.publish("ac/power", str(varacp))
   print("AC Power: "+str(varacp))
   # xs.append(varp)
   energy += varp/maxcounts
   cont+=1
   if cont == maxcounts:
       print("Se llego a la hora de datos")
       #print("Longitud xs: " + str(len(xs)))
       mqttc.publish("panels/energy", str(energy))
       print("Energy Wh:  "+ str(energy))
       cont = 0
       energy = 0


   print("Contador: " + str(cont))
   time.sleep(10    )
mqttc.loop_forever()
