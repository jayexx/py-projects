#script to convert flac to mp3 using ffmpeg
import sys
import os

musiclist = os.listdir(os.getcwd())
for file in musiclist:
	name = os.path.splitext(file)[0]
	if file.endswith(".flac") and not os.path.isfile(name + '.mp3'):
			os.system('ffmpeg -i \"' + file + '\" -b:a 320k \"' + name + '.mp3\"')