# MATLAB

## Beats extraction

This part can be possible thanks to:
https://labrosa.ee.columbia.edu/projects/beattrack/

You can find all informations and functions on how extraction
beats from a music (.wav)

I've just done some scripts to automatize and record beats
into a text file for our game.

### Usage

You need matlab to use it!  
Just use this command in matlab console:

```
script_convert_music
```

If you want change the music to extract beats
just change:  

```
% Location of the music
music = 'musiques/colouring.wav';
% Where you want to put your text file
output_file = 'musiques/colouringBeats.txt';
```
