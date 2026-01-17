from tkinter import *
from tkinter import messagebox
from pygame import mixer
import json
import random

mixer.init()

# --- DATA LOAD ---
try:
    with open('language_data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    messagebox.showerror(title='Error',message='File not found\nPlease make sure that the language file is in correct path.')
    
# --- UPDATED CYBER-DARK THEME ---
BG_MAIN = "#05070A"       # Pure Dark
CARD_BG = "#0B121E"       # Deep Navy Slate
ACCENT_BLUE = "#38BDF8"   # Electric Sky
ACCENT_PURPLE = "#A78BFA" # Soft Violet
ACCENT_PINK = "#FB7185"   # Rose Red
ACCENT_GREEN = "#34D399"  # Mint Green
TEXT_PRIMARY = "#F8FAFC"
TEXT_SECONDARY = "#64748B"

# Configuration
FLIP_DELAY = 5500 #Time it has to display primary Language word before switching.
TIMER_STEPS = 60

# Animation/State Variables
flip_stage = 0
is_flipping = False
flip_timer = None
timer_remaining = FLIP_DELAY

# --- FUNCTIONS ---

def update_progress_ui():
    progress_label.config(text=f"T O T A L   W O R D S :  {len(data)}")

def guessed_right():
    play_correct_button_sound()
    if len(data) > 0:
        del data[0]
    update_progress_ui()  #Change total words
    display_german()

def guessed_wrong():
    play_incorrect_button_sound()
    display_german()

def play_timer_sound():
    mixer.music.load('timer-5-sec.mp3')
    mixer.music.play(loops=1)

def play_correct_button_sound():
    mixer.music.load('correct.mp3')
    mixer.music.play(loops=1)

def play_incorrect_button_sound():
    mixer.music.load('incorrect.mp3')
    mixer.music.play(loops=1)

def update_timer_bar():
    global timer_remaining
    if not is_flipping and canvas.itemcget(text_id, 'text') == "G E R M A N":
        timer_remaining -= (FLIP_DELAY / TIMER_STEPS)
        percentage = max(0, timer_remaining / FLIP_DELAY)
        bar_width = 360 * percentage
        canvas.coords(timer_bar, 20, 15, 20 + bar_width, 15)
        
        color = ACCENT_BLUE if percentage > 0.3 else ACCENT_PINK
        canvas.itemconfig(timer_bar, fill=color)
        
        if timer_remaining > 0:
            window.after(int(FLIP_DELAY / TIMER_STEPS), update_timer_bar)

def animate_flip(to_back):
    global flip_stage, is_flipping, timer_remaining
    is_flipping = True
    canvas.itemconfig(timer_bar, state='hidden')
    
    if flip_stage < 6:
        scale = 1 - (flip_stage * 0.16)
        canvas.place(x=250 - (200 * scale), y=10)
        canvas.config(width=max(1, int(400 * scale)))
        flip_stage += 1
        window.after(15, lambda: animate_flip(to_back))
    
    elif flip_stage == 6:
        if to_back:
            try:
                english_word = data[0].get('english')
            except (IndexError, KeyError):
                english_word = "MASTERED"
            
            canvas.itemconfig(card_shape, outline=ACCENT_GREEN, width=3)
            canvas.itemconfig(text_id, text='T R A N S L A T I O N', fill=ACCENT_GREEN)
            canvas.itemconfig(word_id, text=english_word)
        else:
            random.shuffle(data)
            try:
                german_word = data[0].get('german')
            except (IndexError, KeyError):
                german_word = "DONE"
            
            canvas.itemconfig(card_shape, outline=ACCENT_PURPLE, width=2)
            canvas.itemconfig(text_id, text='G E R M A N', fill=TEXT_SECONDARY)
            canvas.itemconfig(word_id, text=german_word)
        
        flip_stage += 1
        window.after(15, lambda: animate_flip(to_back))
    
    elif flip_stage < 12:
        scale = 0.1 + ((flip_stage - 6) * 0.16)
        canvas.place(x=250 - (200 * scale), y=10)
        canvas.config(width=int(400 * scale))
        flip_stage += 1
        window.after(15, lambda: animate_flip(to_back))
    
    else:
        canvas.config(width=400)
        canvas.place(x=50, y=10)
        flip_stage = 0
        is_flipping = False
        
        if not to_back:
            timer_remaining = FLIP_DELAY
            canvas.itemconfig(timer_bar, state='normal')
            update_timer_bar()
        else:
            right_button.config(state=NORMAL)
            wrong_button.config(state=NORMAL)

def display_german():
    play_timer_sound()
    global flip_timer
    if flip_timer: 
        window.after_cancel(flip_timer)
    
    right_button.config(state=DISABLED)
    wrong_button.config(state=DISABLED)
    animate_flip(to_back=False)
    flip_timer = window.after(FLIP_DELAY, display_english)

def display_english():
    if not is_flipping:
        animate_flip(to_back=True)

# --- UI SETUP ---
window = Tk()
window.title('Flashify Pro')
window.geometry("500x640")
window.config(bg=BG_MAIN)
window.resizable(False, False)

# Header
title_frame = Frame(window, bg=BG_MAIN)
title_frame.pack(pady=(40, 10))
Label(title_frame, text="FLASH", font=('Impact', 28), bg=BG_MAIN, fg=TEXT_PRIMARY).grid(row=0, column=0)
Label(title_frame, text="IFY", font=('Impact', 28), bg=BG_MAIN, fg=ACCENT_BLUE).grid(row=0, column=1)

# Card Container
card_container = Frame(window, width=500, height=330, bg=BG_MAIN)
card_container.pack_propagate(False)
card_container.pack()

canvas = Canvas(card_container, width=400, height=300, bg=BG_MAIN, highlightthickness=0)
canvas.place(x=50, y=10)

# Card Graphics
card_shape = canvas.create_rectangle(5, 5, 395, 295, fill=CARD_BG, outline=ACCENT_PURPLE, width=2)
timer_bar = canvas.create_line(20, 15, 380, 15, fill=ACCENT_BLUE, width=4, capstyle=ROUND)
text_id = canvas.create_text(200, 70, text='G E R M A N', font=('Verdana', 9, 'bold'), fill=TEXT_SECONDARY)
word_id = canvas.create_text(200, 160, text="", font=('Verdana', 30, 'bold'), fill=TEXT_PRIMARY, width=340)

# Progress indicator
progress_label = Label(window, text="", font=('Consolas', 10), bg=BG_MAIN, fg=TEXT_SECONDARY)
progress_label.pack(pady=10)

# Buttons
btn_frame = Frame(window, bg=BG_MAIN)
btn_frame.pack(pady=20)

def create_btn(parent, icon, color, command):
    return Button(parent, text=icon, command=command, font=('Arial', 24, 'bold'),
                 fg=color, bg=BG_MAIN, activeforeground=BG_MAIN, activebackground=color,
                 bd=0, cursor='hand2', width=3)

wrong_button = create_btn(btn_frame, "✕", ACCENT_PINK, guessed_wrong)
wrong_button.grid(row=0, column=0, padx=30)

right_button = create_btn(btn_frame, "✓", ACCENT_GREEN, guessed_right)
right_button.grid(row=0, column=1, padx=30)

# Initial Start
update_progress_ui()
display_german()
window.mainloop()