temp1=float(input("Ingrese la temperatura del día 1:"))
temp2=float(input("Ingrese la temperatura del día 2:"))
temp3=float(input("Ingrese la temperatura del día 3:"))
humedad=float(input("Ingrese la humedad actual(%):"))

promediotemp=(temp1+temp2+temp3)/3

if promediotemp >30 and humedad <40:
    litro=10
    tiporiego="riego alto"
elif promediotemp>25 and humedad <60:
    litros=5
    tiporiego="riego medio"
else:
    litros=2
    tiporiego="riego bajo"

    print(f"{tiporiego}-litros de agua a usar:{litros}")