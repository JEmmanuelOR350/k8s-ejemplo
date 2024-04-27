import tkinter as tk
from datetime import date, timedelta
import random
from fastapi import FastAPI

app = FastAPI()

class identidad():
    nombre_completo = str("")
    edad = int(0)
    nid = int()
    fecha_de_nacimiento = str()


def descargar_assets():
    nombres = "Hugo Mateo Martín Lucas Leo Daniel Alejandro Manuel Pablo Álvaro Adrián Enzo Mario Diego David Oliver Marcos Thiago Marco Álex Javier Izan Bruno Miguel Antonio Gonzalo Liam Gael Marc Carlos Juan Ángel Dylan Nicolás José Sergio Gabriel Luca Jorge Darío Íker Samuel Eric Adam Héctor Francisco Rodrigo Jesús Erik Amir Jaime Ian Rubén Aarón Iván Pau Víctor Guillermo Luis Mohamed Pedro Julen Unai Rafael Santiago Saúl Alberto Noah Aitor Joel Nil Jan Pol Raúl Matías Martí Fernando Andrés Rayan Alonso Ismael Asier Biel Ander Aleix Axel Alan Ignacio Fabio Neizan Jon Teo Isaac Arnau Luka Max Imran Youssef Anas Elías"
    apellidos = "Hernández García Martínez López González Pérez Rodríguez Sánchez Ramírez Cruz Gómez Flores Morales Vázquez Jiménez Reyes Díaz Torres Gutiérrez Ruiz Mendoza Aguilar Méndez Moreno Ortíz Juárez Castillo Álvarez Romero Ramos Rivera Chávez De_la_Cruz Domínguez Guzmán Velázquez Santiago Herrera Castro Vargas Medina Rojas Muñóz Luna Contreras Bautista Salazar Ortega Guerrero Estrada"
    #Descodificar el contenido
    lista_nombres = nombres.split()
    lista_apellidos = apellidos.split()
    return lista_nombres,lista_apellidos

def generar_id_random():
    n_id = random.randint(1,1000)
    return n_id

def edad_random():
    return random.randint(18,45)

def fecha_random(edad):
    hoy = date.today()
    margen_anyo = int(hoy.year) - edad
    fin = date(margen_anyo,int(hoy.month),int(hoy.day))
    inicio = fin - timedelta(days=365)
    fecha = inicio + (fin - inicio) * random.random()
    fecha = str(fecha)
    return fecha

def generar_nombre():
    lista_nombres,lista_apellidos = descargar_assets()

    # Generar el nombre
    nombre_completo = random.choice(lista_nombres)
    if((random.randint(1,100) <= 20)):
        nombre_completo = nombre_completo +" "+ str(random.choice(lista_nombres))
    nombre_completo = nombre_completo +" "+ random.choice(lista_apellidos)
    nombre_completo = nombre_completo +" "+ random.choice(lista_apellidos)
    nombre_completo = nombre_completo.replace("_"," ")
    return nombre_completo

def generar_identidad():
    id_tmpr = identidad()
    id_tmpr.nid = generar_id_random()
    id_tmpr.nombre_completo = generar_nombre()
    id_tmpr.edad = edad_random()
    id_tmpr.fecha_de_nacimiento = fecha_random(id_tmpr.edad)
    return id_tmpr

@app.get("/")
def read_root():
    try:
        id_contenedor = generar_identidad()
        generar_identidad()
        return f"Mi nombre es {id_contenedor.nombre_completo}, tengo {id_contenedor.edad} años, naci el {id_contenedor.fecha_de_nacimiento}. Mi ID es {id_contenedor.nid}."
    except Exception as e:
        return "Ocurrio el error:", e.args