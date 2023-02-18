import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2

class PDFProtector:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Protector")
        
        # Add label for selecting file
        self.file_label = tk.Label(master, text="Select PDF file")
        self.file_label.pack()
        
        # Add button for browsing files
        self.file_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.file_button.pack()
        
        # Add label for entering output file name
        self.output_label = tk.Label(master, text="Enter output file name")
        self.output_label.pack()
        
        # Add entry widget for output file name
        self.output_entry = tk.Entry(master)
        self.output_entry.pack()
        
        # Add label for entering password
        self.password_label = tk.Label(master, text="Enter password")
        self.password_label.pack()
        
        # Add entry widget for password
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()
        
        # Add protect button
        self.protect_button = tk.Button(master, text="Protect", command=self.protect)
        self.protect_button.pack()
    
    def browse_file(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("PDF files", "*.pdf"), ("all files", "*.*")))
        
    def protect(self):
        # Get values from entry widgets
        output_file = self.output_entry.get()
        password = self.password_entry.get()
        
        # Check if all required fields are filled
        if not all([self.filename, output_file, password]):
            messagebox.showerror("Error", "Please fill in all required fields")
            return
        
        # Read PDF file
        pdf_reader = PyPDF2.PdfFileReader(self.filename)
        
        # Encrypt PDF
        pdf_reader.encrypt(password)
        
        # Create output PDF file
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(0))
        
        with open(output_file, 'wb') as f:
            pdf_writer.write(f)
        
        messagebox.showinfo("Success", "PDF file protected successfully")

if __name__ == '__main__':
    root = tk.Tk()
    app = PDFProtector(root)
    root.mainloop()
