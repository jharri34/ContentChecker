import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import io
import opennsfw2 as n2

# Define allowed file types (lowercase only)
ALLOWED_FILE_TYPES = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff']

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Upload an image or content file",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")]
    )
    if not file_path:
        return

    # Normalize the file extension to lowercase
    file_extension = file_path.split('.')[-1].lower()
    if file_extension not in ALLOWED_FILE_TYPES:
        messagebox.showerror("Error", f"Unsupported file type: {file_extension}")
        return

    try:
        # Open and display the image
        with open(file_path, "rb") as f:
            image_data = f.read()
        image = Image.open(io.BytesIO(image_data))
        image.thumbnail((300, 300))  # Resize for display
        img_tk = ImageTk.PhotoImage(image)

        # Update the image label
        image_label.config(image=img_tk)
        image_label.image = img_tk

        # Predict NSFW probability
        nsfw_probability = n2.predict_image(image)
        progress_bar["value"] = nsfw_probability * 100
        progress_label.config(text=f"NSFW Probability: {nsfw_probability:.2f}")

    except Exception as e:
        messagebox.showerror("Error", f"Error processing image: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Content Checker")

# Create and place widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

title_label = tk.Label(frame, text="Content Checker", font=("Arial", 16))
title_label.pack(pady=10)

upload_button = tk.Button(frame, text="Upload Image", command=upload_file)
upload_button.pack(pady=5)

image_label = tk.Label(frame)
image_label.pack(pady=10)

progress_label = tk.Label(frame, text="NSFW Probability: N/A", font=("Arial", 12))
progress_label.pack(pady=5)

progress_bar = Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()


if __name__ == '__main__':
    root.mainloop()  # run the app