# Rymotion

## Projet IHM (Interactions Homme Machine)

### Usage (Only linux)

Go to the folder Blender and open "blender"

Before to start Blender (in the folder Blender and not in the root), you have to
start the python script (openface/openface.py) like this
(You have to be in the folder Blender, even for the python script!)

```bash
# You can choose your config, but think about to adapt it
# if necessarily
python3 openface/openface.py config/config_blender.yml
```

You're running the script to record emotions. The blender game will
read in the file "openface/informations_extract/emotion.txt" the value
which is written by "openface/openface.py".

Now you just have to start the game. You have to put your mouse on the window
game and press "p".

### What do you need?

#### Openface

I redirect you on this url to install Openface:  
https://github.com/TadasBaltrusaitis/OpenFace/wiki  
When you have finished the above step, think to modify
the file config to give the full path of openface.

#### Blender

You can download it to:  
https://www.blender.org/download/

#### Pygame

Installation Pygame: (needed to use the camera)

```bash
# Dépendances permettant de compiler un module pour python3 + mercurial pour cloner le repo
sudo apt-get install mercurial python3-dev build-essential
# SDL
sudo apt-get install libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev
# FFMPEG et autres
sudo apt-get install libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libsmpeg-dev
mkdir dev
cd dev
# Récupération des sources
hg clone https://bitbucket.org/pygame/pygame
# Compilation et installation
cd pygame
python3 setup.py build
sudo python3 setup.py install
```

[Lien où trouver ce script](https://openclassrooms.com/forum/sujet/pygame-pour-python-3-3-sous-ubuntu-12-10)


## More informations

#### Comment récupérer les beats d'une musique

Deux méthodes testées jusqu'à maintenant:  

-  Utilisation de aubio avec la fonction aubiotrack (cependant résultat très décevant après tests):  
[Lien pour la doc aubio](https://github.com/aubio/aubio)
-  Utilisation de matlab avec une librairie qui donne des résultats bien plus convaincants:  
[Lien pour la librairie matlab](http://labrosa.ee.columbia.edu/projects/coversongs/)

Nous avons une étape de pré-processing où nous transformons un fichier ".wav" en un fichier texte qui nous retourne pour chaque ligne un temps en seconde où nous avons un beat de la musique.  
Pour plus de détails rendez-vous dans le dossier "matlab" qui gère toute cette partie avec un readme dédié.
