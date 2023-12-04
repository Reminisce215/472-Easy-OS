import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import pyautogui
import pygame
import time
import os
import psutil
import pygetwindow as gw
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Global variable to track folder creation
is_folder_created = False
#watchdog observer checks whether a folder has been during runtime
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        global is_folder_created
        if event.is_directory:
            print(f"Directory created: {event.src_path}")
            is_folder_created = True

def start_watchdog_observer():
    path = os.path.join(os.path.expanduser('~'), 'Desktop')
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    return observer


#########################################################################################################################

#initialize pygame mixer
pygame.mixer.init()
###################AUDIO FUNCTIONS#################################################
# Global variable to track if the menu audio has been played
has_played_menu_audio = False
# Global variable for sound state
is_sound_on = True

# Function to play menu audio
def play_menu_audio():
    audio_file = 'menu_audio/menu_audio.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


# Function to play audio for Edge tutorial
def play_edge_audio(index):
    if is_sound_on:
        audio_files = ['edge_audio/edge_pt1.mp3', 'edge_audio/edge_pt2.mp3']
        if index < len(audio_files):
            pygame.mixer.music.load(audio_files[index])
            pygame.mixer.music.play()

# Function to play audio for file explorer tutorial
def play_file_explorer_audio(index):
    if is_sound_on:
        audio_files = ['file_explorer_audio/file_pt1.mp3', 'file_explorer_audio/file_pt2.mp3', 'file_explorer_audio/file_pt3.mp3', 'file_explorer_audio/file_pt4.mp3', 'file_explorer_audio/file_pt5.mp3']
        if index < len(audio_files):
            pygame.mixer.music.load(audio_files[index])
            pygame.mixer.music.play()

# Function to play audio for Edge tutorial
def play_folder_audio(index):
    if is_sound_on:
        audio_files = ['folder_audio/folder_pt1.mp3', 'folder_audio/folder_pt2.mp3', 'folder_audio/folder_pt3.mp3']
        if index < len(audio_files):
            pygame.mixer.music.load(audio_files[index])
            pygame.mixer.music.play()


# Function to play audio for file explorer tutorial
def play_mail_audio(index):
    if is_sound_on:
        audio_files = ['mail_audio/mail_pt1.mp3', 'mail_audio/mail_pt2.mp3', 'mail_audio/mail_pt3.mp3', 'mail_audio/mail_pt4.mp3', 'mail_audio/mail_pt5.mp3', 'mail_audio/mail_pt6.mp3']
        if index < len(audio_files):
            pygame.mixer.music.load(audio_files[index])
            pygame.mixer.music.play()

# Function to play audio for Task Manager tutorial
def play_task_audio(index):
    if is_sound_on:
        audio_files = ['task_manager_audio/task_pt1.mp3', 'task_manager_audio/task_pt2.mp3',
                       'task_manager_audio/task_pt3.mp3']  # Add more as needed
        if index < len(audio_files):
            pygame.mixer.music.load(audio_files[index])
            pygame.mixer.music.play()


#######################################################################################

# Function to create the main menu
def create_main_menu(root):
    global has_played_menu_audio
    if not has_played_menu_audio:
        play_menu_audio()  # Play menu audio only if it hasn't been played before
        has_played_menu_audio = True  # sets the flag to True after playing

    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Logo and Title
    logo = tk.Label(main_frame, text="Easy_OS", font=("Arial", 24))
    logo.pack(pady=20)

    # Tutorial Button
    tutorial_button = ttk.Button(main_frame, text="Tutorial", command=lambda: create_tutorial_page(root))
    tutorial_button.pack(pady=10)

    # Run Test Button
    run_test_button = ttk.Button(main_frame, text="Test Knowledge", command=lambda: create_test_knowledge_page(root))
    run_test_button.pack(pady=10)



def create_test_knowledge_page(root):
    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Title
    title = tk.Label(main_frame, text="Test Your Knowledge", font=("Arial", 16))
    title.pack(pady=10)

    # Test Knowledge Buttons
    test_buttons = {
        "Test Folder": lambda: test_folder(root),
        "Test Edge": lambda: test_edge(root),
        "Test File Explorer": lambda: test_file_explorer(root),
        "Test Mail": lambda: test_mail(root),
        "Test Task Manager": lambda: test_task_manager(root),
        "Main Menu": lambda: create_main_menu(root)
    }

    for text, command in test_buttons.items():
        button = ttk.Button(main_frame, text=text, command=command)
        button.pack(pady=5)




# Add two new functions to play the specific audio files
def play_folder_start_audio():
    audio_file = 'folder_test_audio/start_folder_test.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

def play_test_success_audio():
    audio_file = 'folder_test_audio/success.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


#Test Folder Functionality
def test_folder(root):
    global is_folder_created
    is_folder_created = False

    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Start the observer in a separate thread
    observer_thread = threading.Thread(target=start_watchdog_observer, daemon=True)
    observer_thread.start()

    def check_folder_creation():
        if is_folder_created:
            test_button.config(text="Good Job!", state="disabled")
            play_test_success_audio()
        else:
            root.after(1000, check_folder_creation)  # Check again after 1 second

    test_button = ttk.Button(main_frame, text="Test", command=lambda: [play_folder_start_audio(), check_folder_creation()])
    test_button.pack(pady=10)

    # Main Menu Button
    main_menu_button = ttk.Button(main_frame, text="Main Menu", command=lambda: create_main_menu(root))
    main_menu_button.pack(pady=10)



def play_edge_start_audio():
    audio_file = 'edge_test_audio/start_edge_test.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

#checks whether edge process is running
def is_edge_running():
    "Check if Edge process is running"
    for process in psutil.process_iter(['name']):
        if 'msedge' in process.info['name'].lower():
            return True
    return False

#test edge functionality
def test_edge(root):
    def check_edge_running():
        if is_edge_running():
            test_button.config(text="Good Job!", state="disabled")
            play_test_success_audio()
        else:
            root.after(1000, check_edge_running)  # Check again after 1 second

    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Test Button
    test_button = ttk.Button(main_frame, text="Test", command=lambda: [play_edge_start_audio(),check_edge_running()])
    test_button.pack(pady=10)

    # Main Menu Button
    main_menu_button = ttk.Button(main_frame, text="Main Menu", command=lambda: create_main_menu(root))
    main_menu_button.pack(pady=10)



def play_file_explore_start_audio():
    audio_file = 'file_explorer_test_audio/start_file_explorer_test.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
# Function to check if File Explorer is open
def is_file_explorer_open():
    explorer_titles = ["Quick access", "Home", "Documents", "Downloads", "Pictures", "Desktop"]
    for win in gw.getAllWindows():
        if any(title in win.title for title in explorer_titles):
            return True
    return False

# Test File Explorer
# Functionality
def test_file_explorer(root):
    def check_file_explorer_open():
        if is_file_explorer_open():
            test_button.config(text="Good Job!", state="disabled")
            play_test_success_audio()
        else:
            root.after(1000, check_file_explorer_open)  # Check again after 1 second

    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Test Button
    test_button = ttk.Button(main_frame, text="Test", command=lambda: [play_file_explore_start_audio(),check_file_explorer_open()])
    test_button.pack(pady=10)

    # Main Menu Button
    main_menu_button = ttk.Button(main_frame, text="Main Menu", command=lambda: create_main_menu(root))
    main_menu_button.pack(pady=10)
# Function to check if Mail is open
def is_mail_app_open():
    mail_app_titles = ["Mail"]
    for win in gw.getAllWindows():
        if any(title in win.title for title in mail_app_titles):
            return True
    return False

def play_mail_test_start_audio():
    audio_file = 'mail_test_audio/start_mail_test.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

def play_mail_test_login_confirm_audio():
    audio_file = 'mail_test_audio/mail_confirm.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()


# Test Mail Functionality
def test_mail(root):
    def check_mail_app_open():
        if is_mail_app_open():
            test_button.config(text="Confirm that you have logged in", command=confirm_login)
            play_mail_test_login_confirm_audio()
        else:
            root.after(1000, check_mail_app_open)  # Check again after 1 second

    def confirm_login():
        test_button.config(text="Good Job!", state="disabled")
        play_test_success_audio()

    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Test Button
    test_button = ttk.Button(main_frame, text="Test",
                             command=lambda: [play_mail_test_start_audio(), check_mail_app_open()])
    test_button.pack(pady=10)

    # Main Menu Button
    main_menu_button = ttk.Button(main_frame, text="Main Menu", command=lambda: create_main_menu(root))
    main_menu_button.pack(pady=10)




def play_task_manager_start_audio():
    audio_file = 'task_manager_test_audio/start_task_manager_test.mp3'
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
# Function to check if Task Manager is open
def is_task_manager_open():
    task_manager_titles = ["Task Manager"]
    for win in gw.getAllWindows():
        if any(title in win.title for title in task_manager_titles):
            return True
    return False

# Test Task Manager Functionality
def test_task_manager(root):
    def check_task_manager_open():
        if is_task_manager_open():
            test_button.config(text="Good Job!", state="disabled")
            play_test_success_audio()
        else:
            root.after(1000, check_task_manager_open)  # Check again after 1 second

    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Test Button
    test_button = ttk.Button(main_frame, text="Test",
                             command=lambda: [play_task_manager_start_audio(), check_task_manager_open()])
    test_button.pack(pady=10)

    # Main Menu Button
    main_menu_button = ttk.Button(main_frame, text="Main Menu", command=lambda: create_main_menu(root))
    main_menu_button.pack(pady=10)

# Function to create the tutorial page
def create_tutorial_page(root):
    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Title
    title = tk.Label(main_frame, text="OS Tutorials", font=("Arial", 16))
    title.pack(pady=10)

    # Tutorial Buttons with image paths
    tutorial_buttons = {
        "Create Folder": lambda: create_feature_page(root, "Create Folder",
                                                     ["folder_images/pt1.png", "folder_images/pt2.png",
                                                      "folder_images/pt3.png"]),
        "Edge": lambda: create_feature_page(root, "Edge", ["edge_images/pt1.png", "edge_images/pt2.png"]),
        "File Explorer": lambda: create_feature_page(root, "File Explorer",
                                                     ["file_explorer_images/pt1.png", "file_explorer_images/pt2.png",
                                                      "file_explorer_images/pt3.png", "file_explorer_images/pt4.png",
                                                      "file_explorer_images/pt5.png"]),
        "Mail App": lambda: create_feature_page(root, "Mail App",
                                                ["mail_images/pt1.png", "mail_images/pt2.png", "mail_images/pt3.png",
                                                 "mail_images/pt4.png", "mail_images/pt5.png", "mail_images/pt6.png"]),
        "Task Manager": lambda: create_feature_page(root, "Task Manager",
                                                    ["task_manager_images/pt1.png", "task_manager_images/pt2.png",
                                                     "task_manager_images/pt3.png"]),
        "Main Menu": lambda: create_main_menu(root)
    }

    for text, command in tutorial_buttons.items():
        button = ttk.Button(main_frame, text=text, command=command)
        button.pack(pady=5)

# Function to create the feature page with image traversal
def create_feature_page(root, feature_name, image_paths):
    current_image_index = [0]  # Use a list to allow modification in nested function

    #############   MOUSE FUNCTIONS     ####################
    def mouse_edge_pt1():
        try:
            #slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("edge_feature/edge1_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_edge_pt2():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("edge_feature/edge2_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_file_explorer_pt1():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("file_explorer_feature/file_explorer1_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_file_explorer_pt2():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("file_explorer_feature/file_explorer2_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()


    def mouse_file_explorer_pt3():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("file_explorer_feature/file_explorer3_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_file_explorer_pt4():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("file_explorer_feature/file_explorer4_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()



    def mouse_file_explorer_pt5():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("file_explorer_feature/file_explorer5_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_create_folder_pt1():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("folder_feature/folder1_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()



    def mouse_create_folder_pt2():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("folder_feature/folder2_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_create_folder_pt3():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("folder_feature/folder3_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_mail_app_pt1():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("mail_feature/mail1_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()


    def mouse_mail_app_pt2():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("mail_feature/mail2_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    def mouse_mail_app_pt3():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("mail_feature/mail3_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()


    def mouse_mail_app_pt4():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("mail_feature/mail4_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()
    def mouse_mail_app_pt5():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("mail_feature/mail5_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()


    def mouse_mail_app_pt6():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("mail_feature/mail6_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()


    def mouse_task_manager_pt1():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("task_manager_feature/task1_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()



    def mouse_task_manager_pt2():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("task_manager_feature/task2_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()
    def mouse_task_manager_pt3():
        try:
            # slight delay to ensure that screenshot loads before location function
            time.sleep(0.10)
            coordinates = pyautogui.locateCenterOnScreen("task_manager_feature/task3_feature.png")
            if coordinates is not None:
                pyautogui.moveTo(coordinates)
            else:
                print("Image not found on the screen.")
        except Exception as e:
            print(f"Error occurred: {e}")
            import traceback
            traceback.print_exc()

    #############################################################################


    def update_image(delta):
        nonlocal current_image_index
        current_image_index[0] += delta
        current_image_index[0] = max(0, min(current_image_index[0], len(image_paths) - 1))

        # Open the image using PIL
        pil_image = Image.open(image_paths[current_image_index[0]])

        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the new size maintaining the aspect ratio
        img_width, img_height = pil_image.size
        aspect_ratio = img_width / img_height
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Resize the image
        pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Convert the PIL image to a Tkinter-compatible image
        tk_image = ImageTk.PhotoImage(pil_image)

        image_label.config(image=tk_image)
        image_label.image = tk_image

        #UPDATE IMAGE FOR EACH MOUSE FUNCTION#############################
        # Start the mouse movement in a separate thread to avoid blocking the GUI
        if feature_name == "Edge":
            if current_image_index[0] == 0:  # First image in Edge tutorial
                play_edge_audio(current_image_index[0])
                threading.Thread(target=mouse_edge_pt1).start()
            elif current_image_index[0] == 1:  # Second image in Edge tutorial
                play_edge_audio(current_image_index[0])
                threading.Thread(target=mouse_edge_pt2).start()

        if feature_name == "File Explorer":
            if current_image_index[0] == 0:  # First image in File Explorer tutorial
                play_file_explorer_audio(current_image_index[0])
                threading.Thread(target=mouse_file_explorer_pt1).start()
            elif current_image_index[0] == 1:  # Second image
                play_file_explorer_audio(current_image_index[0])
                threading.Thread(target=mouse_file_explorer_pt2).start()
            elif current_image_index[0] == 2:  # Third image
                play_file_explorer_audio(current_image_index[0])
                threading.Thread(target=mouse_file_explorer_pt3).start()
            elif current_image_index[0] == 3:  # Fourth image
                play_file_explorer_audio(current_image_index[0])
                threading.Thread(target=mouse_file_explorer_pt4).start()
            elif current_image_index[0] == 4:  # Fifth image
                play_file_explorer_audio(current_image_index[0])
                threading.Thread(target=mouse_file_explorer_pt5).start()


        if feature_name == "Create Folder":
            if current_image_index[0] == 0:  # First image in File Explorer tutorial
                play_folder_audio(current_image_index[0])
                threading.Thread(target=mouse_create_folder_pt1).start()
            elif current_image_index[0] == 1:  # Second image
                play_folder_audio(current_image_index[0])
                threading.Thread(target=mouse_create_folder_pt2).start()
            elif current_image_index[0] == 2:  # Third image
                play_folder_audio(current_image_index[0])
                threading.Thread(target=mouse_create_folder_pt3).start()



        if feature_name == "Mail App":
            if current_image_index[0] == 0:  # First image in File Explorer tutorial
                play_mail_audio(current_image_index[0])
                threading.Thread(target=mouse_mail_app_pt1).start()
            elif current_image_index[0] == 1:  # Second image
                play_mail_audio(current_image_index[0])
                threading.Thread(target=mouse_mail_app_pt2).start()
            elif current_image_index[0] == 2:  # Third image
                play_mail_audio(current_image_index[0])
                threading.Thread(target=mouse_mail_app_pt3).start()
            elif current_image_index[0] == 3:  # Fourth image
                play_mail_audio(current_image_index[0])
                threading.Thread(target=mouse_mail_app_pt4).start()
            elif current_image_index[0] == 4:  # Fifth image
                play_mail_audio(current_image_index[0])
                threading.Thread(target=mouse_mail_app_pt5).start()
            elif current_image_index[0] == 5:  # Sixth image
                play_mail_audio(current_image_index[0])
                threading.Thread(target=mouse_mail_app_pt6).start()


        if feature_name == "Task Manager":
            if current_image_index[0] == 0:  # First image in Task Manager tutorial
                play_task_audio(current_image_index[0])
                threading.Thread(target=mouse_task_manager_pt1).start()
            elif current_image_index[0] == 1:  # Second image
                play_task_audio(current_image_index[0])
                threading.Thread(target=mouse_task_manager_pt2).start()
            elif current_image_index[0] == 2:  # Third image
                play_task_audio(current_image_index[0])
                threading.Thread(target=mouse_task_manager_pt3).start()
        ###################################################################

    def toggle_sound():
        global is_sound_on
        is_sound_on = not is_sound_on
        sound_off_button.config(text="Sound On" if is_sound_on else "Sound Off")
        if not is_sound_on:
            pygame.mixer.music.stop()  # Stop playing any ongoing audio

    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Title
    title = tk.Label(main_frame, text=feature_name, font=("Arial", 16))
    title.pack(pady=10)

    # Navigation Frame
    nav_frame = tk.Frame(main_frame)
    nav_frame.pack(pady=10)

    # Feature Page Buttons
    previous_button = ttk.Button(nav_frame, text="Previous", command=lambda: update_image(-1))
    previous_button.grid(row=0, column=0, padx=5)

    next_button = ttk.Button(nav_frame, text="Next", command=lambda: update_image(1))
    next_button.grid(row=0, column=1, padx=5)

    sound_off_button = ttk.Button(nav_frame, text="Sound On/Off", command=toggle_sound)  # No command attached
    sound_off_button.grid(row=0, column=2, padx=5)

    main_menu_button = ttk.Button(nav_frame, text="Main Menu", command=lambda: create_main_menu(root))
    main_menu_button.grid(row=0, column=3, padx=5)

    # Image Label
    image_label = tk.Label(main_frame)
    image_label.pack(pady=10)

    # Initially display the first image
    if image_paths:
        update_image(0)

# Initialize Tkinter root
root = tk.Tk()
root.title("Easy_OS Interface")

# Set the window to full screen
#root.attributes('-fullscreen', True)

# Initialize main menu
create_main_menu(root)

# Start the application
root.mainloop()

