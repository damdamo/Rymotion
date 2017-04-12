# Rymotion

## Projet IHM (Interactions Homme Machine)

#### Bases git  

-  Cloner le projet
-  Ajouter un nouveau fichier au projet
-  Commit ses changements
-  Push ses changements sur github:

```bash
# Télécharger le projet
git clone https://github.com/damdamo/Rymotion.git
# Ajouter un fichier au projet git
git add nomDuFichier
# Commit ses changements
git commit nomDuFichier
# Push ses changements
git push
```

#### Raccourci Vim pour les commentaires du commit (avec git bash):
```bash
#Save
:w
#Quit
:q
#Save and Quit
:wq
#Mode insertion
i
#Quitter le mode insertion
escape
```


## Gestion du son

#### Installation Pygame

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

## Comment récupérer les beats d'une musique

Deux méthodes testées jusqu'à maintenant:  

-  Utilisation de aubio avec la fonction aubiotrack (cependant résultat très décevant après tests):  
[Lien pour la doc aubio](https://github.com/aubio/aubio)
-  Utilisation de matlab avec une librairie qui donne des résultats bien plus convaincants:  
[Lien pour la librairie matlab](http://labrosa.ee.columbia.edu/projects/coversongs/)

Nous avons une étape de pré-processing où nous transformons un fichier ".wav" en un fichier texte qui nous retourne pour chaque ligne un temps en seconde où nous avons un beat de la musique.

Une fois que nous récupérons le fichier "beats.txt" un script python lance la musique et un bruit sur chaque beat des temps données dans "beats.txt". Nous vérifions ainsi l'efficacité du système.

Les musiques étant trop lourdes elles ne sont pas disponible directement sous github pour l'instant. Le fichier "beats.txt" est plus donné à titre indicatif pour voir à quoi celui-ci ressemble.
