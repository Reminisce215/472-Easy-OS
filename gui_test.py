import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import pyautogui
import pygame


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
    run_test_button = ttk.Button(main_frame, text="Test Run")
    run_test_button.pack(pady=10)

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
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.1
        offset_y = new_height * 0.1

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_edge_pt2():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.15
        offset_y = new_height * 0.3

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_file_explorer_pt1():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.1
        offset_y = new_height * 0.1

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_file_explorer_pt2():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.5
        offset_y = new_height * 0.28

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_file_explorer_pt3():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.5
        offset_y = new_height * 0.3

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_file_explorer_pt4():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.42
        offset_y = new_height * 0.33

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)


    def mouse_file_explorer_pt5():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.26
        offset_y = new_height * 0.34

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_create_folder_pt1():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.2
        offset_y = new_height * 0.08

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)


    def mouse_create_folder_pt2():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.105
        offset_y = new_height * 0.08

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_create_folder_pt3():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.2
        offset_y = new_height * 0.09

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_mail_app_pt1():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.1
        offset_y = new_height * 0.1

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_mail_app_pt2():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.05
        offset_y = new_height * 0.02

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_mail_app_pt3():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.25
        offset_y = new_height * 0.05

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_mail_app_pt4():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.08
        offset_y = new_height * 0.18

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_mail_app_pt5():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.11
        offset_y = new_height * 0.082

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_mail_app_pt6():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.4
        offset_y = new_height * 0.2

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_task_manager_pt1():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.1
        offset_y = new_height * 0.1

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x - offset_x
        target_y = center_y + offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)


    def mouse_task_manager_pt2():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.015
        offset_y = new_height * 0.1111

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

    def mouse_task_manager_pt3():
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the aspect ratio of the original image
        original_width, original_height = 1400, 950  # Original dimensions of the image
        aspect_ratio = original_width / original_height

        # Calculate new dimensions of the image based on screen size
        new_width = screen_width
        new_height = int(new_width / aspect_ratio)

        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)

        # Calculate the top left corner of the image (considering letterboxing)
        image_x = (screen_width - new_width) // 2
        image_y = (screen_height - new_height) // 2

        # Calculate the center of the image
        center_x = image_x + new_width // 2
        center_y = image_y + new_height // 2

        # Calculate 10% of the image's width and height
        offset_x = new_width * 0.07
        offset_y = new_height * 0.11

        # Adjust the position to be 10% down and 10% left of the center
        target_x = center_x + offset_x
        target_y = center_y - offset_y

        # Move the mouse to the adjusted position
        pyautogui.moveTo(target_x, target_y, duration=1)

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
        image_label.image = tk_image  # Keep a reference to prevent garbage collection

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
root.attributes('-fullscreen', True)

# Initialize main menu
create_main_menu(root)

# Start the application
root.mainloop()

