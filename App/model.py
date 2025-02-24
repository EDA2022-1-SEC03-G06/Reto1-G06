﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'albums': None,
               'artists': None,
               'songs': None,}

    catalog['albums'] = lt.newList('ARRAY_LIST')
    catalog['artists'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareartists)
    catalog['songs'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparesongs)

    return catalog


# Funciones para agregar informacion al catalogo

def addAlbum(catalog, album):
    # Se adiciona el album a la lista de albumes
    lt.addLast(catalog['albums'], album)
    # Se obtienen los artistas del album
    artists = album['artists'].split(",")
    # Cada artista, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for artist in artists:
        addAlbumArtist(catalog, artist.strip(), album)
    return catalog


def addTrack():

    "Adiciona una canción a la lista de canciones"
    track = newtrack(Track['Track_name'],Track['Track_id'])
    lt.addLast(catalog['songs'],track)

    return catalog






# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento