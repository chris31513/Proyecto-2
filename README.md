# Proyecto-2
Versión:<br />
    python 3.6.5<br />
    <br />
    
  Uso:<br />
    $ make GUI <br />
   <br />
   Para cargar las canciones, hay un botón en el menú "Refresh" que se llama "Mine".<br />
   <br />
   Para buscar una canción, en la barre de búsqueda se escribe:<br />
    Song: song_name<br />
   <br />
   Para buscar un artista, en la barra de búsqueda se escribe:<br />
    Artist: artist_name<br />
   <br />
   Para buscar un álbum, en la barra de búsqueda se escribe:<br />
    Album: album_name<br />
   <br />
   Para limpiar la búsqueda (regresar a la lista de todas las canciones), en el menú "Refresh", está el botón "Search"<br />
   <br />
   Análogamente, para editar una canción, álbum o artista, en la ventana de editar (que se abre presionando el botón "Edit" del menú "Edit tags"), se pone:<br />
    Song: new_song_name<br />
    Album: new_album_name<br />
    Artist: new_artist_name<br />
   <br />
   Sólo se edita la canción que esté seleccionada.<br />
   <br />
   Para reproducir una canción, la seleccionas y, en el menú "Player", hay un botón que se llama "Play". Es análogo para pausar y parar la canción.<br />
   <br />
  Dependencias: <br />
    python-vlc para la versión de python usada, se puede instalar de la siguiente manera: <br />
     $ python3.6 -m pip install python-vlc<br />
    <br />
    vlc, debes instalarlo con tu paqueteria, en distribuciones basadas en Debian se instala así:<br />
     $ sudo apt install vlc<br />
    <br />
    mutagen para la versión de python usada, se puede instalar de la siguiente manera:<br />
     $ python3.6 -m pip install mutagen<br />
    <br />
    PyGObject, es un modulo que permite la interacción entre GTK y python, debería estar instalado. En el caso contrario, hay muchas maneras instalarlo para cada distribución<br />
    <br />
  Recomendaciones:<br />
    Es demasiado recomendable que se ejectue el comando despues de usar la app:<br />
      $ make clean<br />
      <br />
  Errores conocidos:<br />
    -Puede que la música no deje de reproducirse al cerrar la ventana si está escuchando una canción y edita los tags, por lo que se recomienda que pares la canción antes de editar, ó antes de salir.<br />
