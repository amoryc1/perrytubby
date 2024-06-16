import pygame
import random
import os
import tkinter as tk
from subprocess import run
from sys import exit

print("[LOADING]   loaded modules")

# ------------------------------------------------------------- #

show_answers                = False             # Show answers in question screen
prefix_path                 = ""                # _internal/    if using auto_py_to_exe
volume_mult                 = 1                 # Volume percent (1 - 100%, 0 - 0%, 0.5 = 50%)
base_volume                 = 0.75

load_into_game_list         = False             # Show game list that would only be visible after the konami code

size                        = (960, 540)        # Screen width x height
screen_title                = "The Perrytubby"  # Title of the window

# ------------------------------------------------------------- #

pygame.init() # Main Pygame module
pygame.mixer.init() # music

print("[LOADING]   pygame initialized")

# ------------------------------------------------------------- #

menu_music                  = prefix_path + "assets/music/title.ogg"
question_music              = prefix_path + "assets/music/question.ogg"
scream_sfx                  = prefix_path + "assets/music/scream.ogg"
fail_music                  = prefix_path + "assets/music/dead.ogg"
gameselect_music            = prefix_path + "assets/music/gameselect.ogg"

pygame.mixer.music.load(menu_music)
base_volume = 0.75
pygame.mixer.music.play(-1)

print("[LOADING]   assets/music/ loaded")

# ------------------------------------------------------------- #

splashfile = open(prefix_path + "assets/txt/splash.txt", "r")
splashes = []
for x in splashfile:
    splashes.append(x[:-1])
splashchoice = random.choice(splashes)

with open(prefix_path + 'assets/txt/hiscore.txt') as file:
    hiscore = int(file.read())
file.close()

lossfile = open(prefix_path + "assets/txt/threats.txt", "r")
loss_response = []
win_response = ["beans"]
for x in lossfile:
    loss_response.append(x)
    
print("[LOADING]   assets/txt/ loaded")

# ------------------------------------------------------------- #

screen                      = pygame.display.set_mode(size)
pygame.display.set_caption("The Perrytubby")
pygame.display.set_icon(pygame.image.load(prefix_path + 'assets/images/icon.ico'))

# ------------------------------------------------------------- #

BLACK = (0, 0, 0)
GREY = (100, 100, 100)
WHITE = (255, 255, 255)

# ------------------------------------------------------------- #

bg                          = pygame.image.load(prefix_path + 'assets/images/bg.jpg')
matoos_fail                 = pygame.image.load(prefix_path + 'assets/images/gameover.jpg')
questions_bg                = pygame.image.load(prefix_path + 'assets/images/questions.jpeg')
uparrow                     = pygame.image.load(prefix_path + 'assets/images/up.png')
downarrow                   = pygame.image.load(prefix_path + 'assets/images/down.png')
leftarrow                   = pygame.image.load(prefix_path + 'assets/images/left.png')
rightarrow                  = pygame.image.load(prefix_path + 'assets/images/right.png')
agamepad                    = pygame.image.load(prefix_path + 'assets/images/a.png')
bgamepad                    = pygame.image.load(prefix_path + 'assets/images/b.png')

print("[LOADING]   assets/images/ loaded")

# ------------------------------------------------------------- #

title_font                  = pygame.font.Font(prefix_path + 'assets/Unifontexmono.ttf', 28)
font                        = pygame.font.Font(prefix_path + 'assets/Unifontexmono.ttf', 22)
small_font                  = pygame.font.Font(prefix_path + 'assets/Unifontexmono.ttf', 14)

print("[LOADING]   assets/Unifontexmono.ttf loaded")

# ------------------------------------------------------------- #

start_button_text           = font.render("Start", True, (255, 255, 255))
start_button                = start_button_text.get_rect(center=(size[0] // 2, size[1] // 2))

keypad1_text                = title_font.render("1", True, (0, 0, 0)) # 1
keypad1_button              = keypad1_text.get_rect(center=((size[0] // 2)-48, (size[1] // 2)-60))
keypad2_text                = title_font.render("2", True, (0, 0, 0)) # 2
keypad2_button              = keypad2_text.get_rect(center=((size[0] // 2), (size[1] // 2)-60))
keypad3_text                = title_font.render("3", True, (0, 0, 0)) # 3
keypad3_button              = keypad3_text.get_rect(center=((size[0] // 2)+48, (size[1] // 2)-60))
keypad4_text                = title_font.render("4", True, (0, 0, 0)) # 4
keypad4_button              = keypad4_text.get_rect(center=((size[0] // 2)-48, (size[1] // 2)))
keypad5_text                = title_font.render("5", True, (0, 0, 0)) # 5
keypad5_button              = keypad5_text.get_rect(center=((size[0] // 2), (size[1] // 2)))
keypad6_text                = title_font.render("6", True, (0, 0, 0)) # 6
keypad6_button              = keypad6_text.get_rect(center=((size[0] // 2)+48, (size[1] // 2)))
keypad7_text                = title_font.render("7", True, (0, 0, 0)) # 7
keypad7_button              = keypad7_text.get_rect(center=((size[0] // 2)-48, (size[1] // 2)+60))
keypad8_text                = title_font.render("8", True, (0, 0, 0)) # 8
keypad8_button              = keypad8_text.get_rect(center=((size[0] // 2), (size[1] // 2)+60))
keypad9_text                = title_font.render("9", True, (0, 0, 0)) # 9
keypad9_button              = keypad9_text.get_rect(center=((size[0] // 2)+48, (size[1] // 2)+60))
keypad0_text                = title_font.render("0", True, (0, 0, 0)) # 0
keypad0_button              = keypad0_text.get_rect(center=((size[0] // 2), (size[1] // 2)+120))

keypadback_text             = title_font.render("<", True, (0, 0, 0)) # Backspace
keypadback_button           = keypadback_text.get_rect(center=((size[0] // 2)-48, (size[1] // 2)+120))
keypadeq_text               = title_font.render("=", True, (0, 0, 0)) # Equals
keypadeq_button             = keypadback_text.get_rect(center=((size[0] // 2)+96, (size[1] // 2)+120))
keypadde_text               = title_font.render(".", True, (0, 0, 0)) # Decimals
keypadde_button             = keypadback_text.get_rect(center=((size[0] // 2)+48, (size[1] // 2)+120))

setting_showanswers_text    = small_font.render("Show Answers", True, (255, 255, 255)) # show_answers
setting_showanswers_button  = setting_showanswers_text.get_rect(center=((size[0] // 2), (size[1]-64)))

slider_rect = pygame.Rect(size[0] - 220, size[1] - 60, 200, 10)
handle_rect = pygame.Rect(size[0] - 40, size[1] - 75, 20, 30)

print("[LOADING]   buttons loaded")

# ------------------------------------------------------------- #

alpha_surface = pygame.Surface(size, pygame.SRCALPHA)    # 0 - solid, 255 - invisible
alpha_surface_animation = pygame.Surface(size, pygame.SRCALPHA)    # 0 - solid, 255 - invisible

# ------------------------------------------------------------- #

question = 0
lives = 3
answer = 0 # Corrent answer
p_answer = "" # What did the use type
symbolList = ["+", "-", "/", "*"]
equation = ""

# ------------------------------------------------------------- #

def draw_slider(screen, slider_rect, handle_rect):
    pygame.draw.rect(screen, GREY, slider_rect)
    pygame.draw.rect(screen, BLACK, handle_rect)
    
def gamelist():
    global game_launched
    # Open up a game
    def open_game():
        selected_index = listbox.curselection()[0]
        print(f"[TKINTER]   Opening {items[selected_index]}")
        
        root.destroy()
        pygame.quit()
        
        exe_dir = file[selected_index]
        os.chdir(exe_dir)
        print(f"[TKINTER]   exe: {exe_dir + 'main.exe'}")
        run("main.exe")
        
        exit()



    # Create the main window
    root = tk.Tk()
    root.title("Open a game")

    # Create a frame to hold the listbox and scrollbar
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Create a Listbox widget
    listbox = tk.Listbox(frame, selectmode=tk.SINGLE, height=6)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Create a Scrollbar widget
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Link the scrollbar to the listbox
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Add items to the listbox
    items = []
    file = []
    
    files = os.listdir(prefix_path + "games/")
    for x in files:
        if os.path.isfile(os.path.join(prefix_path + "games/" + x, "main.exe")):
            print(f"[TKINTER]   {os.path.join(prefix_path + 'games/' + x, 'main.exe')} exists!")

            items.append(os.path.basename(x))
            file.append(os.path.abspath(prefix_path + "games/" + x))
        else:
            print(f"[TKINTER]   {os.path.join(prefix_path + 'games/' + x, 'main.exe')} does not exist!")
    
    for item in items:
        listbox.insert(tk.END, item)

    # Create a button to change the selected value to "b"
    button = tk.Button(root, text="Open", command=open_game)
    button.pack(pady=10)

    # Run the application
    root.mainloop()

konami = [82,82,81,81,80,79,80,79,5,4] # Input konami code on the main menu and play DOOM
konamiimages = ["uparrow","uparrow","downarrow","downarrow","leftarrow","rightarrow","leftarrow","rightarrow","bgamepad","agamepad"]
konamistep = 0

# ------------------------------------------------------------- #

def figure_out_answer():
    global lives, equation
    if len(p_answer) != 0:
        if not p_answer == ".":
            if float(p_answer) == float(answer):
                pygame.display.set_caption(random.choice(win_response))
            else:
                lives -= 1
                pygame.display.set_caption(random.choice(loss_response))
            equation = ""
        else:
            print("[WARNING]   p_answer can not equal '.'")
    else:
        print("[WARNING]   p_answer has a length of 0.")

def add_to_answer(x):
    global p_answer
    p_answer += str(x)

# ------------------------------------------------------------- #

running = True
game_started = False # start math game
failed = False
game_launched = False
dragging = False

clock = pygame.time.Clock()

print("[LOADING]   complete!")

if load_into_game_list:
    running = False
    gamelist()
while running:
    if game_launched:
        running = False
    
    pygame.mixer.music.set_volume(base_volume * volume_mult)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: # Konami Code
            if game_started: # Inside a game
                if event.key == pygame.K_0:
                    add_to_answer(0)
                elif event.key == pygame.K_1:
                    add_to_answer(1)
                elif event.key == pygame.K_2:
                    add_to_answer(2)
                elif event.key == pygame.K_3:
                    add_to_answer(3)
                elif event.key == pygame.K_4:
                    add_to_answer(4)
                elif event.key == pygame.K_5:
                    add_to_answer(5)
                elif event.key == pygame.K_6:
                    add_to_answer(6)
                elif event.key == pygame.K_7:
                    add_to_answer(7)
                elif event.key == pygame.K_8:
                    add_to_answer(8)
                elif event.key == pygame.K_9:
                    add_to_answer(9)
                elif event.key == pygame.K_PERIOD:
                    if "." not in p_answer:
                        add_to_answer(".")
                elif (event.key == pygame.K_EQUALS or event.key == pygame.K_RETURN) and lives > 0:
                    figure_out_answer()
                elif event.key == pygame.K_BACKSPACE:
                    if len(p_answer) > 0:
                        p_answer = p_answer[:len(p_answer)-1]
                    
            if not konamistep == 10:
                if (event.scancode == konami[konamistep]) and (not game_started):
                    konamistep += 1
                    if konamistep == 10:
                        # BG
                        screen.fill((0, 0, 0))
                        screen.blit(matoos_fail, (0, 0))
                        pygame.display.flip()
                        # Music
                        pygame.mixer.music.load(gameselect_music)
                        base_volume = 1.25
                        pygame.mixer.music.play(-1)
                        pygame.display.set_caption(f"Game select.")
                        
                        gamelist()
                else:
                    konamistep = 0
                    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos) and not konamistep == 10: # Start the game
                if not game_started:
                    pygame.mixer.music.load(question_music)
                    pygame.mixer.music.play(-1)
                    base_volume = 0.5
                    game_started = True
            
            if handle_rect.collidepoint(event.pos):
                dragging = True
                
            # Settings
            if setting_showanswers_button.collidepoint(event.pos): # show_answers
                show_answers = not show_answers
            # Keypad
            if keypadback_button.collidepoint(event.pos): # keypad minus
                if len(p_answer) > 0:
                    p_answer = p_answer[:len(p_answer)-1]
            if keypadeq_button.collidepoint(event.pos) and lives > 0: # keypad equal
                figure_out_answer()
                
            if keypad0_button.collidepoint(event.pos): # keypad 0
                add_to_answer(0)
            if keypad1_button.collidepoint(event.pos): # keypad 1
                add_to_answer(1)
            if keypad2_button.collidepoint(event.pos): # keypad 2
                add_to_answer(2)
            if keypad3_button.collidepoint(event.pos): # keypad 3
                add_to_answer(3)
            if keypad4_button.collidepoint(event.pos): # keypad 4
                add_to_answer(4)
            if keypad5_button.collidepoint(event.pos): # keypad 5
                add_to_answer(5)
            if keypad6_button.collidepoint(event.pos): # keypad 6
                add_to_answer(6)
            if keypad7_button.collidepoint(event.pos): # keypad 7
                add_to_answer(7)
            if keypad8_button.collidepoint(event.pos): # keypad 8
                add_to_answer(8)
            if keypad9_button.collidepoint(event.pos): # keypad 9
                add_to_answer(9)
            if keypadde_button.collidepoint(event.pos): # keypad decimal
                if "." not in p_answer:
                    add_to_answer(".")

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                handle_rect.x = max(slider_rect.x, min(event.pos[0] - handle_rect.width // 2, slider_rect.x + slider_rect.width - handle_rect.width))
                volume_mult = (handle_rect.x - slider_rect.x) / (slider_rect.width - handle_rect.width)
    
    
    
    
    screen.fill(WHITE) # Fill over screen
   

    # Show before game
    if not game_started:
        # images
        screen.blit(bg, (0, 0)) # Draw background imag
        alpha_surface.fill((0, 0, 0, 155)) # Make image darker
        screen.blit(alpha_surface, (0, 0))
        # text
        screen.blit(title_font.render("Perrytubby's Class", True, (255, 255, 255)), (size[0] // 2 - (56 * (18/4)), 20))
        screen.blit(small_font.render(splashchoice, True, (255, 255, 255)), (size[0] // 2 - (28 * (len(splashchoice)/4)), 65))
        screen.blit(font.render(f"Hiscore: {hiscore}", True, (255, 255, 255)), (5, size[1]-32))
        # button
        pygame.draw.rect(screen, (20, 120, 20), start_button.inflate(20, 10))
        screen.blit(start_button_text, start_button)
        
        if show_answers:
            pygame.draw.rect(screen, (20, 120, 20), setting_showanswers_button.inflate(0, 0))
        else:
            pygame.draw.rect(screen, (120, 20, 20), setting_showanswers_button.inflate(0, 0))
        screen.blit(setting_showanswers_text, setting_showanswers_button)
        # Konami Code
        for i in range(10):
            if konamistep > i:
                exec(f"screen.blit({konamiimages[i]}, (6 + 32*i, 6))")
    
    # You Die
    elif lives == 0: # fail_music, scream_sfx
        screen.blit(matoos_fail, (0, 0)) # matos imag
        if not failed: # Only run code once for sounds
            failed = True
            pygame.display.set_caption(f"I'm in your walls... (Score {question-3})")
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(scream_sfx), maxtime=2000)
            pygame.mixer.music.load(fail_music)
            base_volume = 1.25
            pygame.mixer.music.play(-1)
            
            if question-3 > hiscore and not show_answers:
                with open(prefix_path + 'assets/hiscore.txt', "w") as file:
                    file.write(str(question-3))
                file.close()
    
    # animation finishd
    else:
            
        # Generate equation
        if equation == "":
            p_answer = ""
            question += 1
            num1 = 0
            num2 = 0
            symbol = random.choice(symbolList)
            if symbol == "+" or symbol == "-":
                num1 = random.randrange(1000+question)+1
                num2 = random.randrange(1000+question)+1
                if symbol == "-" and num2 > num1:
                    num1, num2 = num2, num1
            elif symbol == "*":
                num1 = random.randrange(11+question)+1
                num2 = random.randrange(11+question)+1
            elif symbol == "/":
                num1 = random.randrange(15+question)+1
                num2 = random.randrange(15+question)+1
                if num2 > num1:
                    num1, num2 = num2, num1
            equation = f"{num1} {symbol} {num2}"
            exec(f"answer = round({equation}, 1)")
            
        # Images
        screen.blit(questions_bg, (0, 0)) # Draw background imag
        screen.blit(alpha_surface, (0, 0)) # Make image darker
        
        # Add text
        if show_answers:
            screen.blit(font.render(f"Question {question}:   {equation} [{answer}]", True, (255, 255, 255)), (20, 20))
        else:
            screen.blit(font.render(f"Question {question}:   {equation}", True, (255, 255, 255)), (20, 20))
        screen.blit(font.render(f"Lives: {lives}/3", True, (255, 255, 255)), (20, size[1]-36))
        screen.blit(font.render(f"{p_answer}", True, (255, 255, 255)), ((size[0] // 2)-104, (size[1] // 2)-132))
        
        # Buttons
        # Keypad
        for i in range(10):
            exec(f"pygame.draw.rect(screen, (200, 200, 200), keypad{i}_button.inflate(0, 0))")
            exec(f"screen.blit(keypad{i}_text, keypad{i}_button)")
        pygame.draw.rect(screen, (200, 200, 200), keypadback_button.inflate(0, 0))
        screen.blit(keypadback_text, keypadback_button)
        pygame.draw.rect(screen, (200, 200, 200), keypadeq_button.inflate(0, 0))
        screen.blit(keypadeq_text, keypadeq_button)
        pygame.draw.rect(screen, (200, 200, 200), keypadde_button.inflate(0, 0))
        screen.blit(keypadde_text, keypadde_button)
            
        
    
    # Volume
    draw_slider(screen, slider_rect, handle_rect)
    screen.blit(small_font.render(f"Volume: {int(volume_mult*100)}%", True, WHITE), (size[0] - 220, size[1] - 30))

    # Update the display
    pygame.display.flip()
    clock.tick(60) # Frame rate


# Quit Pygame
pygame.quit()
exit()