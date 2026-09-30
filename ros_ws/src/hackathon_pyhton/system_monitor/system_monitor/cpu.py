import psutil


#Número de cores do processador
print(len(psutil.Process().cpu_affinity()))
#Porcentagem média de uso da CPU 
print(psutil.cpu_percent(interval=0.1,percpu=False))
#Porcentagem de uso individual de cada core
print(psutil.cpu_percent(interval=0.1,percpu=True))
#Temperatura da CPU em graus Celsius


temperaturas = []
max = 0
for indice in psutil.sensors_temperatures().keys():
   temperaturas.append(psutil.sensors_temperatures()[indice][0].current)
max_temp = 0
for temp in temperaturas:
   if temp > max_temp:
      max_temp=temp
print(max_temp)

#Porcentagem de uso da RAM
#Quantidade total de memória em bytes
#Quantidade de memória utilizada em bytes