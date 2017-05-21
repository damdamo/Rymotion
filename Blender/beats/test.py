f=open('beats.txt', 'r')
beats=f.readlines()
beats=[l.strip('\n') for l in beats]
# beats = list(map(float, beats)) 
beats = [ '%.0f' % elem for elem in beats ]
beats = list(map(float, beats)) 

if 235 in beats:
	print('yes')
else:
	print('no')