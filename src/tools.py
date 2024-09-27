import os
from pathlib import Path
import time
from glob import glob
import tkinter as tk
from tkinter import ttk, END
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile
import pygame
import bsl
import numpy as np
import random
from bsl.triggers.software import SoftwareTrigger

def run_prompt_window():

    """
    for now hello
    """
    win = tk.Tk()
    bg_color = '#E0E0EE'
    win.title('ASMR'); win.configure(background=bg_color); win.geometry('1100x800')
    def get_values():
        global subject_id, session, welcome_page_duration, n_repetitions, resting_time, n_repetitions_train, sham_protocol, smr_protocol 
        subject_id = int(e0.get())
        session = int(e5.get())
        welcome_page_duration = int(e1.get())
        resting_time = int(e2.get())
        n_repetitions = int(e3.get())
        n_repetitions_train = int(e4.get())
        sham_protocol = sham_button.get()
        smr_protocol = smr_button.get()

        win.destroy()
    def estimate_exp_duration():
        welcome_page_duration = int(e1.get())
        resting_time = int(e2.get())
        n_repetitions = int(e3.get())
        tk.Label(win, text=f'Estimated duration of recording is {int((welcome_page_duration + 20 + resting_time + n_repetitions * (20 + resting_time)) / 60)} minutes',
                font=('Arial', 9, 'italic'), bg=bg_color, fg="black").place(relx = 0.58, rely = 0.41, anchor = 'sw')
        
        
    tk.Label(win, text='ASMR', font=('Arial', 22), bg=bg_color, fg="#3d6466").place(relx = 0.5, rely = 0.02, anchor = 'center')
    tk.Label(win, text='Welcome to ANT Sensorimotor Rhythm Study', font=('Arial', 12, 'italic', 'bold'), bg=bg_color, fg="#3d6466").place(relx = 0.5, rely = 0.06, anchor = 'center')
    tk.Label(win, text='Enter participant information...', font=('Arial', 10, 'italic', 'bold'), bg=bg_color, fg="#3d6466").place(relx = 0.2, rely = 0.14, anchor = 'center')
    tk.Label(win, text="Subject ID", font=('Arial', 9, 'italic'), bg=bg_color, fg="black").place(relx = 0.18, rely = 0.19, anchor = 'sw')
    tk.Label(win, text="Session number", font=('Arial', 9), bg=bg_color, fg="black").place(relx = 0.18, rely = 0.22, anchor = 'sw')
    tk.Label(win, text="Saving Directory", font=('Arial', 9), bg=bg_color, fg="black").place(relx = 0.18, rely = 0.25, anchor = 'sw')
    e0 = tk.Entry(win)
    e0.place(relx = 0.31, rely = 0.19, anchor = 'sw')
    e5 = tk.Entry(win)
    e5.place(relx = 0.31, rely = 0.22, anchor = 'sw')

    sham_button = tk.IntVar() 
    smr_button = tk.IntVar() 
    tk.Label(win, text="Protocol", font=('Arial', 9, 'italic'), bg=bg_color, fg="black").place(relx = 0.48, rely = 0.19, anchor = 'sw')
    tk.Checkbutton(win, text="Sham", font=('Arial', 9), bg=bg_color, fg="black", variable=sham_button).place(relx = 0.55, rely = 0.19, anchor = 'sw') 
    tk.Checkbutton(win, text="Smr", font=('Arial', 9), bg=bg_color, fg="black", variable=smr_button).place(relx = 0.55, rely = 0.22, anchor = 'sw') 

    def save():
        files = [('Python Files', '*.fif')]
        file = asksaveasfile(initialfile = f'epochs_subject_session.fif', filetypes = files, defaultextension = files)
        tk.Label(win, text=file, font=('Arial', 10, 'italic', 'bold'), bg=bg_color, fg="#3d6466").place(relx = 0.35, rely = 0.29, anchor = 'center')
    ttk.Button(win, text="Browse", command=lambda : save()).place(relx = 0.31, rely = 0.25, anchor = 'sw')
    tk.Label(win, text='Design your ASMR experiment...', font=('Arial', 10, 'italic', 'bold'), bg=bg_color, fg="#3d6466").place(relx = 0.2, rely = 0.29, anchor = 'center')
    tk.Label(win, text="Duration of welcome and end pages", font=('Arial', 9, 'italic'), bg=bg_color, fg="black").place(relx = 0.18, rely = 0.34, anchor = 'sw')
    tk.Label(win, text="Duration of resting time between trials", font=('Arial', 9), bg=bg_color, fg="black").place(relx = 0.18, rely = 0.37, anchor = 'sw')
    tk.Label(win, text="Number of experiment repetitions", font=('Arial', 9), bg=bg_color, fg="black").place(relx = 0.58, rely = 0.34, anchor = 'sw')
    tk.Label(win, text="Number of training repetitions", font=('Arial', 9), bg=bg_color, fg="black").place(relx = 0.58, rely = 0.37, anchor = 'sw')
    tk.Label(win, text="seconds", font=('Arial', 9, 'italic'), bg=bg_color, fg="black").place(relx = 0.46, rely = 0.37, anchor = 'sw')
    tk.Label(win, text="seconds", font=('Arial', 9, 'italic'), bg=bg_color, fg="black").place(relx = 0.46, rely = 0.34, anchor = 'sw')

    e1 = tk.Entry(win)
    e1.insert(END, '7') 
    e1.place(relx = 0.40, rely = 0.34, anchor = 'sw', width=60)
    e2 = tk.Entry(win)
    e2.insert(END, '5')
    e2.place(relx = 0.40, rely = 0.37, anchor = 'sw', width=60)
    e3 = tk.Entry(win)
    e3.insert(END, '75')
    e3.place(relx = 0.77, rely = 0.34, anchor = 'sw', width=60)
    e4 = tk.Entry(win)
    e4.insert(END, '5')
    e4.place(relx = 0.77, rely = 0.37, anchor = 'sw', width=60)
    ttk.Button(win, text="Set", command = estimate_exp_duration).place(relx = 0.87, rely = 0.37, anchor = 'sw', width=70, height=23)
    ttk.Button(win, text="Run the Experiment!", command = get_values).place(relx = 0.76, rely = 0.25, anchor = 'sw', height=85, width=160)

    logo = Image.open(Path.cwd() / "images" / "diagram.png")
    logo = logo.resize((800, 350))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, bg=bg_color)
    logo_label.place(relx = 0.5, rely = 0.64, anchor = 'center')
    logo_label.image = logo

    logo = Image.open(Path.cwd() / "images" / "SNSF_logo.png")
    logo = logo.resize((130, 95))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, bg=bg_color)
    logo_label.place(relx = 0.5, rely = 0.95, anchor = 'center')
    logo_label.image = logo

    logo = Image.open(Path.cwd() / "images" / "UZH_logo.png")
    logo = logo.resize((130, 125))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, bg=bg_color)
    logo_label.place(relx = 0.3, rely = 0.96, anchor = 'center')
    logo_label.image = logo

    logo = Image.open(Path.cwd() / "images" / "USZ_logo.png")
    logo = logo.resize((130, 25))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo, bg=bg_color)
    logo_label.place(relx = 0.7, rely = 0.96, anchor = 'center')
    logo_label.image = logo
    win.mainloop()


def run_instruction_phase():
    """
    fill here too
    """
    x = 2150; y = 0
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()
    width, height = 1920, 1200
    twisting_hands_img = pygame.image.load(Path.cwd() / "images" / "instruction_image.png")
    n_repetition_train = 0
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    space_interval = pygame.transform.scale(pygame.image.load(Path.cwd() / "images" / "black_screen.jpg"), (width, height))
    cat_solo_img = pygame.image.load(Path.cwd() / "images" / "cat" / "Idle (1).png").convert()
    while n_repetition_train <= n_repetitions_train:
        wait_time = 5
        screen.blit(space_interval, (0, 0))
        if n_repetition_train == 0:
            font1 = pygame.font.SysFont('Arial', 28, italic=False) # need to adjust the values
            font2 = pygame.font.SysFont('Arial', 21, italic=True) # need to adjust the values
            img1 = font2.render('Please put your hands on the table', True, 'white') 
            img2 = font2.render('Imagine twisting your right hand, whenever you see the below photo (just imagine)', True, 'white')
            img3 = font1.render('Welcome to Instruction phase of ASMR experiment', True, 'white') 
            screen.blit(img1, (width/2 - 180, height/2 - 250))
            screen.blit(img2, (width/2 - 390, height/2 - 200))
            screen.blit(img3, (width/2 - 320, height/2 - 400))
            wait_time = 10
        screen.blit(twisting_hands_img, (width/2 - 175, height/2 - 150))
        pygame.display.update()
        time.sleep(wait_time)
        screen.blit(space_interval, (0, 0))
        pygame.display.update()
        time.sleep(5)
        n_repetition_train += 1
    pygame.quit()

    return cat_solo_img

def stream_eeg_data():
    """
    fill in
    """

    fname = f'subject_{subject_id}_session_{session}'
    stream_name = "BrainVision RDA" 
    record_dir = Path(Path.cwd() / "raw_data").expanduser()
    recorder= bsl.StreamRecorder(record_dir=record_dir, fname=fname, stream_name=stream_name, fif_subdir=False, verbose=False)
    recorder.start()
    trigger = SoftwareTrigger(recorder)
    receiver = bsl.StreamReceiver(bufsize=2, winsize=1, stream_name=stream_name) # LSL stream name ('RDA 127.0.0.1:51244')
    winsize_in_samples = receiver.streams[stream_name].sample_rate * receiver.winsize
    fft_window = np.hanning(winsize_in_samples)
    sample_spacing = 1./receiver.streams[stream_name].sample_rate
    frequencies = np.fft.rfftfreq(n=int(winsize_in_samples), d=sample_spacing) 
    smr_band = np.where(np.logical_and(8<=frequencies, frequencies<=15))[0] # check the values
    
    return recorder, receiver, stream_name, trigger, fft_window, smr_band
    

def run_experiment(recorder, receiver, stream_name, trigger, fft_window, smr_band, cat_solo_img):
    """
    fill in
    """

    x = 2150; y = 0
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()
    width, height = 1920, 1200
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    class Cat:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.list = [pygame.image.load(f).convert_alpha() for f in glob(str(Path.cwd() / "images" / "cat" / "Walk*.png"))[1:]]
            self.list_kill = [pygame.transform.scale(pygame.image.load(f).convert_alpha(), (0, 0)) for f in glob(str(Path.cwd() / "images" / "cat" / "Walk*.png"))[1:]] # added this line
            self.list_idle = [pygame.image.load(f).convert_alpha() for f in glob(str(Path.cwd() / "images" / "cat" / "Idle*.png"))[1:]]
            self.counter = 0
            self.image = self.list[0]
            self.prov = ""
            self.state = ""
        
        def update(self):
            self.counter += .1 # control speed of the images loop
            if self.counter >= len(self.list):
                self.counter = 0
            if self.state == "alive_right":    
                self.image = self.list[int(self.counter)]
                self.prov = self.state
            if self.state == "alive_left":    
                self.image = pygame.transform.flip(self.list[int(self.counter)], True, False)
                self.prov = self.state    
            if self.state == "alive_nomove":
                self.image = self.list_idle[int(self.counter)]
                self.prov = self.state
            if self.state == "kill_nomove":
                self.image = self.list_kill[int(self.counter)]
                self.prov = self.state
            if self.state == "alive_nomove":
                if self.counter >= len(self.list_idle):
                    self.counter = 0
                if self.prov == "alive_right":
                    self.image = self.list_idle[int(self.counter)]
                if self.prov == "alive_left":
                    self.image = pygame.transform.flip(self.list_idle[int(self.counter)], True, False)

            screen.blit(self.image, (self.x, self.y))

    width, height = 1920, 1200
    cat_init_x, cat_init_y = 900, 477
    cat = Cat(cat_init_x, cat_init_y)
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    space_restings_photos = [pygame.transform.scale(pygame.image.load(Path.cwd() / "images" / "resting_photos" / f'resting_screen_{i}.jpg'), (width, height)) for i in range(1, 31)]
    space = pygame.transform.scale(pygame.image.load(Path.cwd() / "images" / 'background.jpeg'), (width, height))
    space_interval = pygame.transform.scale(pygame.image.load(Path.cwd() / "images" / "black_screen.jpg"), (width, height))
    space_ask_for_exp_start = pygame.transform.scale(pygame.image.load(Path.cwd() / "images" / "grey_screen.jpg"), (width, height))

    if sham_protocol:
        blocks_set = ["fake", "rest"] 
    if smr_protocol:
        blocks_set = ["smr", "rest"]
    
    clock = pygame.time.Clock()
    phase_timer = bsl.utils.Timer()  # timer used within a phase to count the duration
    n_repetition = 0
    winsize_in_samples = receiver.streams[stream_name].sample_rate * receiver.winsize

    ## Welcome Page
    tic = phase_timer.sec()
    while phase_timer.sec() <= tic + welcome_page_duration:
        screen.blit(space_interval, (0, 0))
        font1 = pygame.font.SysFont('Arial', 28, italic=False) # need to adjust the values
        font2 = pygame.font.SysFont('Arial', 18, italic=True) # need to adjust the values
        font3 = pygame.font.SysFont('Arial', 15, italic=False) # need to adjust the values
        img1 = font1.render('Welcome to ANT Sensori Motor Rhythm (ASMR) Study', True, 'white')
        img3 = font2.render('Imagine moving the cat to the right, whenever you see it. (just imagine)', True, 'white')
        img5 = font2.render('Please focus on the black cross whenever you see it (no moving imagination)', True, 'white')
        img4 = font3.render(f'The experiment will start in {int(welcome_page_duration - phase_timer.sec())} seconds ...', True, 'white')
        screen.blit(img1, (width/2 - 350, height/2 - 370))
        screen.blit(cat_solo_img, (width/2 - 45, height/2 + 40))
        screen.blit(img3, (width/2 - 300, height/2 - 170))
        screen.blit(img4, (width/2 - 145, height/2 + 300))
        screen.blit(img5, (width/2 - 325, height/2 - 120))
        cat.state = "kill_nomove"
        cat.update()
        pygame.display.update()


    ## Going in to the loop of recording duration

    while welcome_page_duration < phase_timer.sec() and n_repetition < n_repetitions:
        for block in blocks_set:
            if block == 'rest':  # resting part intra blocks around 5 seconds... doing nothing (show a black window)
                cat.state = "kill_nomove"
                screen.blit(space_interval, (0, 0))
                cat.update() 
                pygame.display.update() 
                pygame.time.wait(int((resting_time - 1 + (random.random() * 2)) * 1000)) # random values around resting_time (user adjustable)
        
            if block == 'smr':
                miu_powers_rest = []
                trigger.signal(1) 
                init_time = phase_timer.sec()
                print(winsize_in_samples)
                while phase_timer.sec() <= init_time + 10: # smr first 10 seconds (resting part) 
                    receiver.acquire()
                    raw, samples = receiver.get_window(return_raw=True)
                    # print(samples.shape)
                    if samples.shape[0] != winsize_in_samples: 
                        continue
                    data = raw.pick(picks=['C3']).get_data() # .set_eeg_reference(ref_channels='average', projection=False)
                    data = np.multiply(data, fft_window)
                    
                    fftval = np.abs(np.fft.rfft(data, axis=1) / data.shape[-1])
                    miu_powers_rest.append(np.average(np.square(fftval[:, smr_band]), axis=1)[0]) # - np.average(np.square(fftval[:, smr_band]), axis=1)[0]))
                    screen.blit(space, (0, 0))
                    cat.state = "kill_nomove"
                    cat.update()
                    pygame.draw.line(screen, color='black', start_pos=(width/2, height/2 - 50), end_pos=(width/2, height/2 + 50), width=5) # maybe I need to change it because of full screen
                    pygame.draw.line(screen, color='black', start_pos=(width/2 - 50, height/2), end_pos=(width/2 + 50, height/2), width=5)
                    pygame.display.update()
                    
                # thr = np.mean(miu_powers_rest, axis=0) + (np.max(miu_powers_rest, axis=0) - np.mean(miu_powers_rest, axis=0)) / 0.6745
                thr = np.mean(miu_powers_rest, axis=0) * 0.8 # changed to 80 percent
                trigger.signal(2)
                cat.x = cat_init_x  # initiate cat position
                cat.y = cat_init_y
                while phase_timer.sec() <= init_time + 20: # smr second 10 seconds (imagery part)
                    
                    receiver.acquire()
                    raw, samples = receiver.get_window(return_raw=True)
                    if samples.shape[0] != winsize_in_samples: 
                        continue
                    data = raw.pick(picks=['C3']).get_data() # .set_eeg_reference(ref_channels='average', projection=False)
                    data = np.multiply(data, fft_window)
                    fftval = np.abs(np.fft.rfft(data, axis=1) / data.shape[-1])
                    miu_power_imag = np.average(np.square(fftval[:, smr_band]), axis=1)[0] # - np.average(np.square(fftval[:, smr_band]), axis=1)[0])
                    if miu_power_imag <= thr: # ERD
                        cat.state = "alive_right"
                        cat.x += 5 
                    if miu_power_imag > thr:
                        cat.state = "alive_nomove"
                        
                    
                    screen.blit(space, (0, 0))
                    cat.update()
                    pygame.display.update()
            
            if block == 'fake':
                trigger.signal(3)
                init_time = phase_timer.sec()
                while phase_timer.sec() <= init_time + 10: # duration of fake rest block  
                    
                    screen.blit(space, (0, 0))
                    cat.state = "kill_nomove"
                    cat.update()
                    pygame.draw.line(screen, color='black', start_pos=(width/2, height/2 - 50), end_pos=(width/2, height/2 + 50), width=5) # maybe I need to change it because of full screen
                    pygame.draw.line(screen, color='black', start_pos=(width/2 - 50, height/2), end_pos=(width/2 + 50, height/2), width=5)
                    pygame.display.update()
                
                trigger.signal(4)
                cat.x = cat_init_x  # initiate cat position
                cat.y = cat_init_y
                while phase_timer.sec() <= init_time + 20: # duration of fake block 
                    signals_right = [random.randint(0,15) for _ in range(random.randint(50,300))]
                    signals_left = [random.randint(-15,0) for _ in range(random.randint(50,300))]
                    signals_right.extend(signals_left)
                    for signal in signals_right:
                        if signal >= 0:
                            cat.state = "alive_right"
                            cat.x += 1
                        if signal < 0:
                            cat.state = "alive_nomove" 
                            
                        screen.blit(space, (0, 0))
                        cat.update()
                        pygame.display.update()
                    
            clock.tick(10) # control the speed of the cat

        
        ## One minute break every 15 minutes 
        if n_repetition % 15 == 0 and n_repetition != 0: 
            space_restings = random.choices(space_restings_photos, k=6) # 5 photos randomly selected
            for space_resting in space_restings: 
                screen.blit(space_resting, (0, 0))
                cat.state = "kill_nomove"
                cat.update()
                pygame.display.update()
                time.sleep(10) 

        
        ## Training phase
        if n_repetition == 0: 
            screen.blit(space_ask_for_exp_start, (0, 0))
            font1 = pygame.font.SysFont('Arial', 24, italic=False)
            font2 = pygame.font.SysFont('Arial', 20, italic=True)
            font3 = pygame.font.SysFont('Arial', 15, italic=False)
            img1 = font1.render('You passed the training phase, do you want to continue?', True, 'white')
            img2 = font2.render('If yes, press space button to start the experiment', True, 'white')
            img3 = font2.render('If no, press R button to repeat the training phase', True, 'white')  
            img4 = font3.render('Please consider that you should NOT imagine moving the cat to any direction while you see the cross in the screen', True, 'white')  
            screen.blit(img1, (width/2 - 310, height/2 - 400))
            screen.blit(img2, (width/2 - 230, height/2 - 250))
            screen.blit(img3, (width/2 - 230, height/2 - 200))
            screen.blit(img4, (width/2 - 380, height/2 + 300))
            cat.state = "kill_nomove"
            cat.update()
            pygame.display.update()
            pygame.event.clear()
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            running = False
                            trigger.signal(10)
                        elif event.key == pygame.K_r:
                            running = False
                            n_repetition -= 1
        n_repetition += 1 


    # end page (It could be modified with better picture) 
    init_time = phase_timer.sec()
    while  phase_timer.sec() <= init_time + 10:
        screen.blit(space_interval, (0, 0))
        img3 = font1.render('Thanks for your participation', True, 'white')
        screen.blit(img3, (width/2 - 165, height/2 - 150)) # need to adjust the values
        cat.state = "kill_nomove"
        cat.update()
        pygame.display.update()

    trigger.close()
    recorder.stop()
    pygame.quit()


