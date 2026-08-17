#Programa para Calculo de Salario neto
bruto = float(input("Salario bruto: "))
porcentaje = float(input("Porcentaje de impuestos (ej: 16): "))
deducciones = float(input("Deducciones: "))

descuento = bruto * (porcentaje / 100)
neto = bruto - descuento - deducciones
print(f"El salario neto es: {neto}")