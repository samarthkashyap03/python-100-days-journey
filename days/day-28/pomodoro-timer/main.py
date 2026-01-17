from tkinter import *
from pygame import mixer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE_PATH='tomato.png'
REPS=0
TIMER=None    

#------------------------------PLAY SOUND---------------------------------#
def play_sound():
    mixer.init()
    mixer.music.load('race-start-beeps-125125.mp3')
    mixer.music.play(loops=2)
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    REPS=0
    label.config(text='TIMER')
    canvas.itemconfig(timer_text,text=f"00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def set_timer():
    global REPS
    REPS+=1
    play_sound()
    if REPS%8==0:
        label.config(text='BREAK')
        countdown(LONG_BREAK_MIN*60)
    elif REPS%2==0:
        label.config(text='BREAK')
        countdown(SHORT_BREAK_MIN*60)
    else:
        label.config(text='TIMER')
        countdown(WORK_MIN*60)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):        
    count_mins=count//60
    count_secs=count%60
    if count_secs<10:
        count_secs=f"0{count_secs}"
    if count_mins<10:
        count_mins=f"0{count_mins}"
    canvas.itemconfig(timer_text,text=f"{count_mins}:{count_secs}")
    if count>0:
        global TIMER
        TIMER=window.after(1000,countdown,count-1)
    else:
        play_sound()
        checkmark.config(text="✓"*(REPS//2))
        set_timer()
# ----------------------------UI------------------------------- #
window=Tk()
window.title("Pomodoro Timer")
window.config(padx=80,pady=40,background=YELLOW)

#Label text for Timer
label=Label(fg=GREEN,text='TIMER',font=(FONT_NAME,30,'bold'),highlightthickness=0,bg=YELLOW,pady=20)
label.pack(side='top')

#Create canvas
canvas=Canvas(width=200,height=215,background=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file=IMAGE_PATH)
canvas.create_image(100,100,image=tomato_image)
timer_text=canvas.create_text(100,125,text='00:00',font=(FONT_NAME,40,'bold'))
canvas.pack()

#Create a start button
start_button=Button(text='START',font=(FONT_NAME,10,'bold'),fg=RED,command=set_timer)
start_button.pack(side='left')

#Create a Reset button
reset_button=Button(text='RESET',font=(FONT_NAME,10,'bold'),fg=RED,command=reset_timer)
reset_button.pack(side='right')

#Checkmark Label
checkmark=Label(text="✓",fg=GREEN,pady=10,font=(FONT_NAME,20,'bold'))
checkmark.pack(side='bottom')

window.mainloop()