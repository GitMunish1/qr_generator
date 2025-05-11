import qrcode
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if data.strip() == "":
        messagebox.showwarning("Input Error", "Please enter some text or URL.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("temp_qr.png")

    # Display the image in the GUI
    qr_img = Image.open("temp_qr.png")
    qr_img = qr_img.resize((200, 200))
    qr_img = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img  # Keep a reference

# Function to save the QR code
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        qr = qrcode.make(entry.get())
        qr.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully.")

# Set up GUI
root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

Label(root, text="Enter Text or URL:", font=("Arial", 14)).pack(pady=10)

entry = Entry(root, font=("Arial", 12), width=35)
entry.pack(pady=5)

Button(root, text="Generate QR Code", font=("Arial", 12), command=generate_qr).pack(pady=10)

qr_label = Label(root)
qr_label.pack(pady=20)

Button(root, text="Save QR Code", font=("Arial", 12), command=save_qr).pack(pady=10)

root.mainloop()
