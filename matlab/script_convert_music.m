% Script to convert a music wav into beats text
% Thanks to: https://labrosa.ee.columbia.edu/projects/beattrack/

% Variables

music = 'musiques/colouring.wav';
output_file = 'musiques/colouringBeats.txt';

% Call the function convert wav 2 beats
% Care the music must be to the wav format!

convertWav2Beat(music, output_file)