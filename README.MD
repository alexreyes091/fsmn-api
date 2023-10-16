# FSMN API

## Requisitos

---

- Python 3.x
- pip (administrador de paquetes de Python)
- virtualenv (opcional para entornos virtuales)

## Dependencias

---

- La lista de dependencias se encuentra en  'requirements.txt'

## Puesta en marcha

---

##### 1. Clonar el repositorio.

```bash
> git clone https://github.com/alexreyes091/fsmn-api.git
```

##### 2. Navegar al directorio del proyecto y crear una instancia de la base de datos en docker.

```bash
> docker compose up -d
```

##### 3. Instalar Dependencias

- (Si utiliza virtualenv, asegurece de que su entorno este activo.)

```bash
> pip install -r requirements.txt
```

##### 4.  Ejecutar el main.py

```bash
> python main.py
```


## Detalles de Uso

---
Tras iniciar el servidor podra ingresar a la siguiente URL.

```bash
http://127.0.0.1:8000/docs
```

