import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# Function to create the main menu
def create_main_menu(root):
    # Clear current content
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
    run_test_button = ttk.Button(main_frame, text="Run Test")
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

    def update_image(delta):
        nonlocal current_image_index
        current_image_index[0] += delta
        current_image_index[0] = max(0, min(current_image_index[0], len(image_paths) - 1))
        # Open the image using PIL
        pil_image = Image.open(image_paths[current_image_index[0]])

        # Resize the image to a fixed size (e.g., 300x300)
        pil_image = pil_image.resize((1400, 950), Image.Resampling.LANCZOS)

        # Convert the PIL image to a Tkinter-compatible image
        tk_image = ImageTk.PhotoImage(pil_image)

        image_label.config(image=tk_image)
        image_label.image = tk_image  # Keep a reference to prevent garba

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

    sound_off_button = ttk.Button(nav_frame, text="Sound Off")  # No command attached
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

# Initialize main menu
create_main_menu(root)

# Start the application
root.mainloop()


'''
import tkinter as tk
from tkinter import ttk

# Function to create the main menu
def create_main_menu(root):
    # Clear current content
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
    run_test_button = ttk.Button(main_frame, text="Run Test")
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

# Function to create a feature page with image traversal
def create_feature_page(root, feature_name, image_paths):
    current_image_index = [0]  # Using a list to allow modification in nested function

    def update_image(delta):
        nonlocal current_image_index
        current_image_index[0] += delta
        current_image_index[0] = max(0, min(current_image_index[0], len(image_paths) - 1))
        image = tk.PhotoImage(file=image_paths[current_image_index[0]])
        image_label.config(image=image)
        image_label.image = image  # Keep a reference

    # Clear current content
    for widget in root.winfo_children():
        widget.destroy()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Title
    title = tk.Label(main_frame, text=feature_name, font=("Arial", 16))
    title.pack(pady=10)

    # Image Label
    image_label = tk.Label(main_frame)
    image_label.pack(pady=10)

    # Feature Page Buttons
    next_button = ttk.Button(main_frame, text="Next", command=lambda: update_image(1))
    next_button.pack(pady=5)

    previous_button = ttk.Button(main_frame, text="Previous", command=lambda: update_image(-1))
    previous_button.pack(pady=5)

    sound_off_button = ttk.Button(main_frame, text="Sound Off")
    sound_off_button.pack(pady=5)

    main_menu_button = ttk.Button(main_frame, text="Main Menu", command=lambda: create_main_menu(root))
    main_menu_button.pack(pady=20)

    # Initially display the first image
    if image_paths:
        update_image(0)

# Initialize Tkinter root
root = tk.Tk()
root.title("Easy_OS Interface")
v
# Initialize main menu
create_main_menu(root)

# Start the application
root.mainloop()

'''

