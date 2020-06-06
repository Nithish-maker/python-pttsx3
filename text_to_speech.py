import pyttsx3
from mybio import *
friend = pyttsx3.init() # object creation

""" RATE"""
rate = friend.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
friend.setProperty('rate', 90)     # setting up new voice rate


"""VOLUME"""
volume = friend.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
friend.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = friend.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
friend.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
friend.say(about0("hi rakesh kumar"))
# in friend.say('My current speaking rate is ' + str(rate))
friend.runAndWait()
friend.stop()