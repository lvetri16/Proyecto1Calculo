import flet as ft


#funcion que permite invertir los numeros que se convierten pasandolos como cadenas
def invertir(cadena):
    invertido=""
    for i in range(len(cadena)-1,-1,-1):
        invertido+=cadena[i]
    return invertido

#convertores de binario

def binario_ternario(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def binario_cuaternario(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def binario_octal(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_octal(num)))

def binario_hexadecimal(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

def binario_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(2**i) 
        i+=1 
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

#convertores de ternario

def ternario_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(3**i)
        i+=1  
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

def ternario_binario(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_binario(num)))

def ternario_cuaternario(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def ternario_octal(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_octal(num)))

def ternario_hexadecimal(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

#convertores de cuaternario

def cuaternario_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(4**i) 
        i+=1 
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

def cuaternario_binario(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_binario(num)))

def cuaternario_ternario(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def cuaternario_octal(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_octal(num)))

def cuaternario_hexadecimal(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

#convertores de octal

def octal_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(8**i) 
        i+=1 
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

def octal_binario(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_binario(num)))

def octal_ternario(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def octal_cuaternario(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def octal_hexadecimal(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

#convertores de hexadecimal

def hexadecimal_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(16**i) 
        i+=1 
    for i in numerot:
        if i=="A":
            lista2.append(10)
        elif i=="B":
            lista2.append(11)
        elif i=="C":
            lista2.append(12)
        elif i=="D":
            lista2.append(13)
        elif i=="E":
            lista2.append(14)
        elif i=="F":
            lista2.append(15)
        else:
            lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum  

def hexadecimal_binario(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_binario(num)))

def hexadecimal_ternario(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def hexadecimal_cuaternario(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def hexadecimal_octal(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_octal(num)))
 
#convertores de decimal

def decimal_binario(numero):
    resto=0
    bin=""
    while numero>0:
        resto = numero%2
        numero=numero//2
        bin+=str(resto)
    return bin
     

def decimal_octal(numero):
    resto = 0
    octal=""
    while numero>0:
        resto = numero%8
        numero=numero//8
        octal+=str(resto)
    return octal

def decimal_cuaternario(numero):
    resto = 0
    cuat=""
    while numero>0:
        resto = numero%4
        numero=numero//4
        cuat+=str(resto)
    return cuat

def decimal_hexadecimal(numero):
    resto=0
    hexa=""
    while numero>0:
        resto = numero%16
        if resto==10:
            hexa+="A"
            numero=numero//16
        elif resto==11:
            hexa+="B"
            numero=numero//16
        elif resto==12:
            hexa+="C"
            numero=numero//16

        elif resto==13:
            hexa+="D"
            numero=numero//16
        elif resto==14:
            hexa+="E"
            numero=numero//16
        elif resto==15:
            hexa+="F"
            numero=numero//16
        else:
            hexa+=str(resto)
            numero=numero//16
    return hexa

def decimal_terciario(numero):
    resto=0
    terc=""
    while numero>0:
        resto = numero%3
        numero=numero//3
        terc+=str(resto)
    return terc
print(ternario_decimal(1021))

#validaciones de numeros

#validacion decimal

def validar_decimal(numero):
    if str(numero)=="":
        return False
    for i in numero:
        if numero.isnumeric()==False:
            return False
        else:
            return True

#validacion de binario

def validar_binario(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>1 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True
    
#validacion de ternario

def validar_ternario(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>2 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True

#validacion de cuaternario

def validar_cuaternario(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>3 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True

#validacion de octal

def validar_octal(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>7 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True

#validar hexadecimal

def validar_hexadecimal(numero):
    cont=0
    cont=0
    if str(numero)=="":
        return False
    for i in numero:
        print(i)
        if i=="A":
            cont+=1
        elif i=="B":
            cont+=1
        elif i=="C":
            cont+=1
        elif i=="D":
            cont+=1
        elif i=="E":
            cont+=1
        elif i=="F":
            cont+=1
        else:
            if i.isnumeric()==False:
                return False
            else:
                cont+=1
        
    if cont!=0:
        return True       

def evento_convertir(lista_convertir, lista_convertidos, campo_texto_ingresar, campo_texto_resultados, page):
    if str(lista_convertir.value) != str(lista_convertidos.value):
        if str(lista_convertir.value) == "de binario":
            if str(lista_convertidos.value) == "a ternario":
                if validar_binario(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = binario_ternario(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a cuaternario":
                if validar_binario(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = binario_cuaternario(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a octal":
                if validar_binario(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = binario_octal(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a decimal":
                if validar_binario(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = binario_decimal(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a hexadecimal":
                if validar_binario(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = binario_hexadecimal(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
        elif str(lista_convertir.value) == "de ternario":
            if str(lista_convertidos.value) == "a binario":
                if validar_ternario(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = ternario_binario(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a cuaternario":
                if validar_ternario(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = ternario_cuaternario(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a octal":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a decimal":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a hexadecimal":
                campo_texto_resultados.value = "error"
        elif str(lista_convertir.value) == "de cuaternario":
            if str(lista_convertidos.value) == "a binario":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a ternario":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a octal":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a decimal":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a hexadecimal":
                campo_texto_resultados.value = "error"
        elif str(lista_convertir.value) == "de octal":
            if str(lista_convertidos.value) == "a binario":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a ternario":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a cuaternario":
                campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a decimal":
                if validar_octal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = octal_decimal(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a hexadecimal":
                if validar_octal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = octal_hexadecimal(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
        elif str(lista_convertir.value) == "de decimal":
            if str(lista_convertidos.value) == "a binario":
                if validar_decimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = decimal_binario(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a ternario":
                if validar_decimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = decimal_terciario(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a cuaternario":
                if validar_decimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = decimal_cuaternario(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a octal":
                if validar_decimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = decimal_octal(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a hexadecimal":
                if validar_decimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = decimal_hexadecimal(int(campo_texto_ingresar.value))
                else:
                    campo_texto_resultados.value = "error"
        elif str(lista_convertir.value) == "de hexadecimal":
            if str(lista_convertidos.value) == "a binario":
                if validar_hexadecimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = hexadecimal_binario(campo_texto_ingresar.value)
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a ternario":
                if validar_hexadecimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = hexadecimal_ternario(campo_texto_ingresar.value)
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a cuaternario":
                if validar_hexadecimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = hexadecimal_cuaternario(campo_texto_ingresar.value)
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a octal":
                if validar_hexadecimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = hexadecimal_octal(campo_texto_ingresar.value)
                else:
                    campo_texto_resultados.value = "error"
            elif str(lista_convertidos.value) == "a decimal":
                if validar_hexadecimal(str(campo_texto_ingresar.value)):
                    campo_texto_resultados.value = hexadecimal_decimal(campo_texto_ingresar.value)
                else:
                    campo_texto_resultados.value = "error"
    else:
        campo_texto_resultados.value = "error"
    page.update()

def main1(page: ft.Page):
    lista_convertir = ft.Dropdown(
                                label="Elige una opcion",
                                width=200,
                                options=[
                                    ft.dropdown.Option("de binario"),
                                    ft.dropdown.Option("de ternario"),
                                    ft.dropdown.Option("de cuaternario"),
                                    ft.dropdown.Option("de octal"),
                                    ft.dropdown.Option("de decimal"),
                                    ft.dropdown.Option("de hexadecimal")
                                ],
                            )

    lista_convertidos=ft.Dropdown(
                                label="Elige una opcion",
                                width=200,
                                options=[
                                    ft.dropdown.Option("a binario"),
                                    ft.dropdown.Option("a ternario"),
                                    ft.dropdown.Option("a cuaternario"),
                                    ft.dropdown.Option("a octal"),
                                    ft.dropdown.Option("a decimal"),
                                    ft.dropdown.Option("a hexadecimal")
                                ],
                                
                            )

    # Crear el campo de texto de entrada
    campo_texto_ingresar = ft.TextField(
        label="Ingrese un número",
        width=150,
    )

    # Crear el campo de texto de resultados
    campo_texto_resultados = ft.TextField(
        label="Resultado",
        width=150,
        disabled=True,
    )

    # Crear el botón de conversión
    boton_convertir = ft.ElevatedButton(
        text="Convertir",
        width=150,
        on_click=lambda e: evento_convertir(lista_convertir, lista_convertidos, campo_texto_ingresar, campo_texto_resultados, page)
    )

    # Agregar la interfaz a la página
    page.add(lista_convertidos,lista_convertir,campo_texto_ingresar,boton_convertir,campo_texto_resultados,)

