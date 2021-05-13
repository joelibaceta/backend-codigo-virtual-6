# Sesión 2 / 11 Mayo 2021

El objetivo de esta sesión fue explorar los tipos de colecciones que ofrece python y algunas estructuras de datos basicas como listas, tuplas y diccionarios. Se aprendio a crear funciones y trabajar con diferentes tipos de parametros de entrada.

# Contenido de la sesión

<br/>

## Colecciones

### Listas

La lista es un tipo de colección ordenada. Sería equivalente a lo que en otros lenguajes se conoce por arrays, o vectores.

Las listas pueden contener cualquier tipo de dato: números, cadenas, booleanos y también otras listas.


```
l = [22, True, “una lista”, [1, 2]]
```

Para acceder a un elemento de la lista podemos usar un inidica entre corchetes despues del identificador:

```
l[0]    # 22
l[1]    # True
```

Tambien es posible usar numeros negativos para obtener elementos de la lista en un orden inverso (de derecha a izquierda)

```
l[-1]    # Retorna el ultimo elemento, en este caso una lista [1, 2]
l[-2]    # Retorna el penultimo elemento, en este caso el texto "una lista"
```

Podemos extraer una porcion de lista si usamos el `slicing`, donde en lugar de numeros escribios dos numeros separados por dos puntos. 

```
l[0:2]  # Retornara un subgrupo de elementos desde el inicio 
        # hasta antes de la posicion 2
        # lo que nos devuelve [22, True]
```

Podemos omitir alguno de estos numeros lo que indicara a python que se usara por defecto el inicio o fin de la lista respecitvamente.

```
l[1:]  # Retorna todos los elementos desde el que posee el indice 1 
       # hasta antes de la ultima posicion.
       
l[:]   # Retorna todos los elementos desde el inicio hasta antes del ultimo
```


### Tuplas

Todo lo que hemos explicado sobre las listas se aplica también a las tuplas, a excepción de la forma de definirla, para lo que se utilizan paréntesis en lugar de corchetes.

```
t = (1, 2, True, “python”)
```

### Diccionarios

Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una clave y un valor.

```
d = {
      “Love Actually “: “Richard Curtis”,
      “Kill Bill”: “Tarantino”, 
      “Amélie”: “Jean-Pierre Jeunet”
    }
```

Para obtener un valor en especifico usamos la clave:

```
d[“Kill Bill”] = “Quentin Tarantino”
```

