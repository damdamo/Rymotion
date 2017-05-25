function [] = convertWav2Beat(musique, nameOutput)
% Allow to take a music in the .wav format and 
% return a text file with each line correspond to 
% a beat in a certain time

    % Add path to use detection beats
    addpath('./detectionBeats');
    
    filename = musique;
    [y, Fs] = wavread(filename);
    sonFreq = y(:,1);

    % Function beats return a list with timer of each beat
    b = beat(sonFreq,Fs);

    % We open the file to write
    fid = fopen(nameOutput, 'w');

    % We write into the file
    for i = b
        fprintf(fid, '%f\n', i);
    end

    fclose('all');
    
    disp('Finish!')
end

