import os
import warnings
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import pdfkit
import tkinter as tk
from tkinter import filedialog, messagebox

# 忽略警告
warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", FutureWarning)

def epub_to_text(epub_path, txt_output_path):
    book = epub.read_epub(epub_path)
    text = ""
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            text += soup.get_text() + '\n\n'
    
    with open(txt_output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f'Text extracted to {txt_output_path}')

def epub_to_html(epub_path, html_output_path):
    book = epub.read_epub(epub_path)
    html_content = "<html><head><meta charset='utf-8'></head><body>"
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            html_content += f"<div>{soup.prettify()}</div><br>"
    
    html_content += "</body></html>"
    
    with open(html_output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'HTML generated at {html_output_path}')

def epub_to_pdf(epub_path, pdf_output_path, html_output_path):
    epub_to_html(epub_path, html_output_path)
    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    options = {'encoding': 'UTF-8', 'enable-local-file-access': ''}
    pdfkit.from_file(html_output_path, pdf_output_path, configuration=config, options=options)
    
    print(f'PDF generated at {pdf_output_path}')

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub")])
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, folder_path)

def convert_files():
    epub_file = entry_file.get()
    output_folder = entry_output.get()
    
    if not epub_file or not output_folder:
        messagebox.showerror("Error", "請選擇EPUB檔案和輸出資料夾")
        return
    
    base_name = os.path.splitext(os.path.basename(epub_file))[0]
    output_folder = os.path.join(output_folder, base_name)
    os.makedirs(output_folder, exist_ok=True)
    
    txt_file = os.path.join(output_folder, f"{base_name}.txt")
    html_file = os.path.join(output_folder, f"{base_name}.html")
    pdf_file = os.path.join(output_folder, f"{base_name}.pdf")
    
    epub_to_text(epub_file, txt_file)
    epub_to_pdf(epub_file, pdf_file, html_file)
    
    messagebox.showinfo("完成", "轉換完成！")

# GUI 設計
root = tk.Tk()
root.title("EPUB 轉換器")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="選擇 EPUB 檔案:").grid(row=0, column=0, sticky="w")
entry_file = tk.Entry(frame, width=50)
entry_file.grid(row=0, column=1)
tk.Button(frame, text="瀏覽", command=select_file).grid(row=0, column=2)

tk.Label(frame, text="選擇輸出資料夾:").grid(row=1, column=0, sticky="w")
entry_output = tk.Entry(frame, width=50)
entry_output.grid(row=1, column=1)
tk.Button(frame, text="瀏覽", command=select_output_folder).grid(row=1, column=2)

tk.Button(root, text="開始轉換", command=convert_files).pack(pady=10)

root.mainloop()
