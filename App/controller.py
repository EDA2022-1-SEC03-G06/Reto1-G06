"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de álbumes

def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control

# Funciones para la carga de datos

def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    album = loadAlbums(catalog)
    artists = loadArtists(catalog)
    songs = loadSongs(catalog)
    sortBooks(catalog)
    return album, artists, songs

def loadAlbums(catalog):
    """
    Carga los albumes del archivo.  Por cada album se toma su artista 
    principal y se crea en la lista de artistas, a dicho artista y una
    referencia al album que se esta procesando.
    """
    albumsfile = cf.data_dir + 'Datos/spotify-albums-utf8-small.csv'
    input_file = csv.DictReader(open(albumsfile, encoding='utf-8'))
    for album in input_file:
        model.addAlbum(catalog, album)
    return model.albumSize(catalog)

def loadArtists(catalog):
    """
    Carga los artistas del archivo y los agrega a la lista de artistas
    """
    artistFile = cf.data_dir + 'Datos/spotify-artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistFile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    return model.artistSize(catalog)

def loadSongs(catalog):
    """
    """
    songFile = cf.data_dir + 'Datos/spotify-tracks-utf8-small.csv'
    input_file = csv.DictReader(open(songFile, encoding='utf-8'))
    for song in input_file:
        model.addSong(catalog, song)
    return model.songSize(catalog)

# Funciones de ordenamiento

def sortAlbums(catalog):
    """
    Ordena los libros por average_rating
    """
    model.sortAlbums(catalog)

# Funciones de consulta sobre el catálogo

def getAlbumssByAuthor(control, authorname):
    """
    Retrona los albumes de un artista
    """
    author = model.getAlbumssByAuthor(control['model'], authorname)
    return author


def getBestAlbums(control, number):
    """
    Retorna los mejores albumes
    """
    bestAlbums = model.getBestAlbums(control['model'], number)
    return bestAlbums
