from pygame import mixer

mixer.init() #Start the mixer

mixer.music.load('d:\pythontutorials\chapter 1\songs\Daddy Yankee + Katy Perry feat. Snow - Con Calma Remix (Video con Letra Oficial).mp3') #load the song
mixer.music.set_volume(0.7) #set the volume
mixer.music.play() #play the mixer

while True:
    print("Press 'p' to pause 'r' to resume")
    print("press 'e' to exit the program")
    query = input(">>> ")

    if query == 'p':
        mixer.music.pause() #to pause the music
    elif query =='r':
        mixer.music.unpause() #to resume music
    elif query == 'e':
        mixer.music.stop() #stop the mixer
        break