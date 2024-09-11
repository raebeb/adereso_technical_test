![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  

# Prueba Técnica Adereso

Este repositorio contiene una propuesta de solución al desafío técnico presentado por Adereso, donde se requiere procesar un archivo JSONL que contiene la documentación de Adereso. El objetivo es fragmentar dicha documentación según lo solicitado.

## Índice
1. [Comenzando 🚀](#comenzando-)
   - [Pre-requisitos 📋](#pre-requisitos-)
2. [Instalación 🔧](#instalación-)
   - [Clonar el repositorio](#1-clonar-el-repositorio)
   - [Instalar Python y PIP](#2-descarga-e-instala-python)
   - [Instalar dependencias](#instalar-librerías-necesarias)
3. [Ejecución](#ejecución-)
   - [Variables de entorno](#variables-de-entorno)
   - [Generación de fragmentos](#generación-de-fragmentos)
   - [Pruebas](#pruebas-)
4. [Trabajos futuros](#trabajos-futuros-y-posibles-mejoras)

## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

-   Python 3.12

---

## Instalación 🔧

### 1. Clonar el repositorio
```
git clone git@github.com:raebeb/adereso_technical_test.git
```
ó
```
git clone https://github.com/raebeb/adereso_technical_test.git
```  
>En caso de no tener git instalado (y no tener la intención ni la necesidad de hacerlo) se puede descargar el repositorio como ZIP
  

![image](https://github.com/user-attachments/assets/d6a29527-7bbe-48cc-89f7-2ac43ea9fa37)


### 2. Descarga e instala Python 

(En caso de tener instalado python, pip y algun entorno virtual, saltar al [siguiente paso](#ejecución-))

Sigue las instrucciones de https://www.python.org/downloads/

### 3. Instalar PIP

En este sitio están detalladas las instrucciones para descargar e instalar pip según tu sistema operativo https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/


---  

## Ejecución 💻

### Instalar librerías necesarias  
En la raíz del proyecto, ejecuta el siguiente comando: 
```pip install -r requirements.txt```
> en caso de que el comando anterior falle probar con ```pip3 install -r requirements.txt```

Una vez que se hayan instalado todas las dependencias podemos seguir con el siguiente paso  

### Variables de entorno
En el archivo ```.env```, debes establecer el valor de la API key de OpenAI. De lo contrario, el programa no podrá ejecutarse correctamente  
![image](https://github.com/user-attachments/assets/f717c3d3-ff1b-4b28-af33-e6b3d61d47e4)

### Generación de fragmentos
Una vez que hayas instalado las dependencias, puedes ejecutar el siguiente comando en la raíz del proyecto:
```
python main.py
```

o

```
python3 main.py
```
Durante la ejecución, se mostrará una barra de progreso. Al finalizar, el archivo JSONL resultante se guardará en la carpeta ```output```
![image](https://github.com/user-attachments/assets/6b379d30-2220-4c55-8191-aee9931ae467)




### Pruebas 🧪
Para ejecutar los tests unitarios, ejecuta el siguiente comando en la terminal en la raíz del proyecto:

```
pytest tests
```



***
## Construido con 🛠️
* [Python 3.12](https://www.python.org) - Lenguaje de programación


## ⌨️ con ❤️ por [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) 👩‍💻

```
          ／＞　 フ
         | 　_　_| 
       ／` ミ＿xノ 
      /　　　　 |
     /　 ヽ　　 ﾉ
    │　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_  ヽ_)__)
＼二)
```

## Trabajos futuros y posibles mejoras:
- [ ] Implementar **PDM** o **Poetry** para gestionar las dependencias de forma más eficiente y moderna.
- [ ] Utilizar **difflib** o un algoritmo más robusto para mejorar la búsqueda y detección de fragmentos relacionados.
- [x] Generar dinámicamente los prompts según el contexto mediante una nueva llamada a la API de GPT, evitando así modificar manualmente el diccionario de prompts y previniendo un crecimiento innecesario del mismo.
- [ ] Ampliar la cobertura de pruebas unitarias para asegurar la detección precisa de fragmentos relacionados y mejorar la robustez del código.
- [x] Optimizar el procesamiento de archivos grandes mediante paralelización o procesamiento por lotes para mejorar el rendimiento y reducir el tiempo de ejecución.
- [ ] Agregar soporte para nuevos formatos de entrada/salida (CSV, XML) para ampliar la flexibilidad del procesamiento.

