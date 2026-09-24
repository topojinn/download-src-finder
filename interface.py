import customtkinter as ctk
from download_src import finalsource as srcUrl

root = ctk.CTk()
root.title("download source finder")
root.geometry("800x600")
root.iconbitmap()

label_entry = ctk.CTkLabel(root, text="the source path is {src}")
label_entry.pack(pady=(20, 5))

root.mainloop()
