import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import io

def generate_qr_code():
    website = website_entry.get()
    if not website:
        messagebox.showerror("Error", "Please enter a website URL")
        return
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(website)
    qr.make(fit=True)
    
    global qr_image  # Make it global so we can access it in the save function
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Resize the image to be larger
    qr_image = qr_image.resize((300, 300), Image.Resampling.LANCZOS)
    
    # Convert the image to a format tkinter can use
    img_tk = ImageTk.PhotoImage(qr_image)
    
    # Update the label with the new image
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    
    # Enable the save button
    save_button.config(state=tk.NORMAL)

def save_qr_code():
    if qr_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_image.save(file_path)
            messagebox.showinfo("Success", f"QR Code saved to {file_path}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x550")  # Increased height to accommodate larger QR code

# Create and pack the widgets
title_label = tk.Label(root, text="QR Code Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

website_frame = tk.Frame(root)
website_frame.pack(pady=10)

website_label = tk.Label(website_frame, text="Enter website URL:")
website_label.pack(side=tk.LEFT, padx=5)

website_entry = tk.Entry(website_frame, width=30)
website_entry.pack(side=tk.LEFT)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", command=save_qr_code, state=tk.DISABLED)
save_button.pack(pady=10)

# Global variable to store the QR code image
qr_image = None

root.mainloop()