temporada=input("Ingrese la temporada (baja,meia,alta):")
salario=float(input("Ingrese su salario:"))
gastos=float(input("Ingrese sus gastos:"))

presupuesto=salario-gastos

if temporada=="baja" and presupuesto>=1300:
    recomendacion="viaje internacional"
elif temporada=="media" and presupuesto>=900:
    recomendacion="viaje nacional"
elif temporada=="alta" and presupuesto>=400:
    recomendacion="viaje local"

else:
    recomendacion="quedarse en casa"

print(f"presupuesto disponible:{presupuesto}")
print(f"recomendacion:{recomendacion}")