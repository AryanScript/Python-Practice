# This is coding for making a healthy programmer work

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if(a==stopper):
            mixer.music.stop()
            break

def log_now(msg):
    with open("health.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

init_water=time()
init_eye=time()
init_exercise=time()
water_t=60
eye_t=80
exercise_t=45456
while True:
    if(init_water-time()<water_t):
        print("time for water drink")
        musiconloop("water.mp3","water done")
        init_water=time()
        log_now("drinking water at")

    if(init_eye-time()<eye_t):
        print("time for water drink")
        musiconloop("eye.mp3","break done")
        init_eye=time()
        log_now("break at")
        
    if(init_exercise-time()<exercise_t):
        print("time for water drink")
        musiconloop("exercise.mp3","exercise done")
        init_exercise=time()
        log_now("exercise at")
