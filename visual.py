from tkinter import *
from code import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as filedialog
from tkinter.messagebox import showerror, askyesno
from PIL import Image
from PIL import ImageTk
import webbrowser

#General configuration
color = 'white smoke'
width = 380

root = Tk()
root.title('Email Extrator')
root.geometry(f'380x175')
root.wm_iconbitmap('Images\logo.ico')
root.configure(background=color)

v = IntVar()
t = IntVar()
second_window_proof = 0

#Functions

def start(index=0):
    global height
    height = 175
    root.geometry(f'{width}x{height}')
    label.pack(pady=10)
    radio_button1.place(x=188, y=40)
    radio_button2.place(x=45, y=40)
    next_button.place(x=298, y=133)
    link.place_forget()
    input_entry.place(x=50, y=80)
    browse1.place(x=307, y=76)
    line.place(x=0, y=120)
    input_path = ""
    info_button.place(x=19, y=128)
    created_by.place(x=87, y=135)
    if index == 1:
        label2.pack_forget()
        line2.pack_forget()
        text.pack_forget()
        label3.pack_forget()
        radio_button_output_txt.place_forget()
        radio_button_output_csv.place_forget()
        radio_button_output_json.place_forget()
        radio_button_output_pdf.place_forget()
        radio_button_output_xlsx.place_forget()
        radio_button_output_docx.place_forget()
        output_entry.place_forget()
        browse2.place_forget()

def from_2nd_page():
    global second_window_proof
    second_window_proof = 1
    start(1)

def selection():
    if v.get() == 1:
        browse1.place_forget()
        link.place(x=40, y=79)
        input_entry.place(x=80, y=80)
    elif v.get() == 2:
        browse1.place(x=307, y=76)
        link.place_forget()
        input_entry.place(x=50, y=80)

def next(second_window_proof):
    if v.get() == 0:
        showerror(title = "Error", message = "No input file type selected")
    elif input_entry.get() == "":
        showerror(title = "Error", message = "Please insert an URL or select a file")
    elif v.get() == 1:
        if internet_conection(input_entry.get()) == False:
            showerror(title = "Error", message = "Make sure you have an active internet conection")
        else:
            internet_conection(input_entry.get())
            hide()
    elif v.get() == 2:
        if file_extension(input_path) == False:
            showerror(title = "Error", message = "Please insert a correct file format or an existing file")
        elif file_extension(input_path) == 'pdf':
            where_to_go(input_path, "pdf")
            hide()
        elif file_extension(input_path) == 'txt':
            where_to_go(input_path, "txt")
            hide()
        elif file_extension(input_path) == 'json':
            where_to_go(input_path, "json")
            hide()
            
def proof():
    next(second_window_proof)
      
def input():
    global input_path
    input_path = filedialog.askopenfilename(title = "Select a File", filetypes = (("Files", 
                                                        ".txt .pdf .json"), 
                                                       ("all files", 
                                                        "*.*")))
    input_entry.delete(0, 'end')  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'

def output_folder():
    global output_path
    output_path = filedialog.askdirectory(parent=root, initialdir = "/", title='Choose a folder')
    output_entry.delete(0, END)  # Remove current text in entry
    output_entry.insert(0, output_path)  # Insert the 'path'

def hide():
    if existence() == True:
        link.place_forget()
        browse1.place_forget()
        label.pack_forget()
        radio_button1.place_forget()
        radio_button2.place_forget()
        next_button.place_forget()
        input_entry.place_forget()
        label4.pack_forget()
        label5.pack_forget()
        second_return_button.pack_forget()
        info_button.place_forget()
        created_by.place_forget()
        second_window()

def hide_second_window():
    label2.pack_forget()
    line2.pack_forget()
    text.pack_forget()
    label3.pack_forget()
    radio_button_output_txt.place_forget()
    radio_button_output_csv.place_forget()
    radio_button_output_json.place_forget()
    radio_button_output_pdf.place_forget()
    radio_button_output_xlsx.place_forget()
    radio_button_output_docx.place_forget()
    output_entry.place_forget()
    browse2.place_forget()
    link.place_forget()
    output_entry.place_forget()
    return_button.place_forget()
    second_next_button.place_forget()
    link.place_forget()
    browse1.place_forget()
    label.pack_forget()
    radio_button1.place_forget()
    radio_button2.place_forget()
    next_button.place_forget()
    input_entry.place_forget()
    line.place_forget()
    label6.pack_forget()

def hide_third_window():
    label5.pack_forget()
    label6.pack_forget()
    label7.pack_forget()
    label8.pack_forget()
    label9.pack_forget()
    label10.place_forget()
    label11.place_forget()
    label12.place_forget()
    gmail_button.place_forget()
    stackoverflow_button.place_forget()
    github_button.place_forget()
    paypal_button.place_forget()
    line.place_forget()
    second_return_button.place_forget()
    open_file_button.place_forget()
    finish_button.place_forget()
    second_window()

def existence():
    if second_window_proof == 0:
        if emails_existence(emails_found) == False:
            showerror(title = "Error", message = "No emails were found.")
        else:
            return True
    elif second_window_proof == 1:
        if emails_existence(where_to_go(input_path, "txt", second_window_proof)) == False:
            showerror(title = "Error", message = "No emails were found.")
        else:
            return True

def second_window():
    global height, label2, line2, text, email_category_copy, output_path
    height = 410
    root.geometry(f'{width}x{height}')
    label2 = Label(root,
        text=amount_of_emails_found(category(where_to_go(input_path, "txt", 1), 1)),
        justify = CENTER,
        padx = 0, background=color)
    label2.pack(pady=10)
    text = ScrolledText(root, width=20, height=10, background=color)
    text.pack(fill='both', expand=True)
    email_category_copy = category(where_to_go(input_path, "txt", 1)).copy()
    email_domains(email_category_copy)
    label3.pack(pady=10)
    line2.pack(pady=65)
    radio_button_output_txt.place(x=50, y=273)
    radio_button_output_csv.place(x=145, y=273)
    radio_button_output_json.place(x=240, y=273)
    radio_button_output_pdf.place(x=50, y=300)
    radio_button_output_xlsx.place(x=145, y=300)
    radio_button_output_docx.place(x=240, y=300)
    output_entry.place(x=50, y=333)
    browse2.place(x=307, y=329)
    output_path = os.getcwd()
    if second_window_proof == 1:
        output_entry.delete(0, END)  #Remove current text in entry
    output_entry.insert(0, output_path)
    return_button.place(x=10, y=375)
    second_next_button.place(x=218, y=375)

def third_window():
    global height
    height = 375
    root.geometry(f'{width}x{height}')
    hide_second_window()
    label5.pack(pady=5)
    label6.pack(pady=5)
    label7.pack(pady=(0, 5))
    label8.pack(pady=(0,2))
    label9.pack(pady=5)
    label10.place(x=90, y=200)
    label11.place(x=280, y=200)
    label12.place(x=167, y=260)
    gmail_button.place(x=15, y=220)
    stackoverflow_button.place(x=60, y=220)
    github_button.place(x=235, y=220)
    paypal_button.place(x=125, y=280)
    line.place(x=0, y=330)
    second_return_button.place(x=10, y=341)
    open_file_button.place(x=132, y=341)
    finish_button.place(x=255, y=341)

def email_domains(email_category):
    for emails_domains in email_category.keys():
        email_category[emails_domains] = IntVar()
        # create Checkbutton for filename and keep on list
        cb = Checkbutton(text, text=emails_domains, variable=email_category[emails_domains], bg=color, anchor='w')
        text.window_create('end', window=cb, padx=(140))
        text.insert('end', '\n')
        text.config(state=DISABLED)

def filter_selection():
    selection = []
    email_category_to_filter = category(where_to_go(input_path, "txt", 1))
    for key, value in email_category_copy.items():
        if email_category_copy["All"].get() > 0:
            selection = email_category_to_filter["All"]
            break
        elif value.get() > 0:
            if len(email_category_to_filter[key]) > 1:
                for email in email_category_to_filter[key]:
                    selection.append("".join(email))
            else:
                selection.append("".join(email_category_to_filter[key]))
    return selection

def last_stage():
    selection = filter_selection()
    if selection == []:
        showerror(title = "Error", message = "Please select which domains you'd like to export")
    elif t.get() == 0:
        showerror(title = "Error", message = "Please select an output file format")
    elif t.get() == 3:
        output_file(selection, 3, output_path, ".txt")
        third_window()
    elif t.get() == 4:
        output_file(selection, 4, output_path, ".csv")
        third_window()
    elif t.get() == 5:
        output_file(selection, 5, output_path, ".json")
        third_window()
    elif t.get() == 6:
        output_file(selection, 6, output_path, ".pdf")
        third_window()
    elif t.get() == 7:
        output_file(selection, 7, output_path, ".xlsx")
        third_window()
    elif t.get() == 8:
        output_file(selection, 8, output_path, ".docx")
        third_window()
    else:
        showerror(title = "Error", message = "An error have been encountered, Please restart the program")

def created_file_location():
    try:
        os.startfile(output_file_location(output_path))
    except:
        if askyesno(title="No such program to open file", message="It seems that there's no program define to open this type of file. Would you like to open the container folder instead?"):
            os.startfile(output_file_location(output_path, 1))

def open_gmail():
    webbrowser.open("mailto:?to=newswebstar@gmail.com", new=1)

def open_github_page():
    webbrowser.open("https://github.com/henfrydls/email-extrator", new=1)

def open_stack_page():
    webbrowser.open("https://stackoverflow.com/users/14391986/henfry-de-los-santos", new=1)

def open_paypal_page():
    webbrowser.open("http://paypal.me/henfrydls", new=1)

def finish():
    root.destroy()

def information():
    information_window = Toplevel()
    information_window.title('Information')
    information_window.configure(background=color)
    information_window.geometry('380x275')

    label7 = Label(information_window,
            text="""Hope this program helped you.
    Please take a minute and read the documentation.
    If you have any questions or suggestion,
    Please feel free to contact me.
    All links are provided down below.""",
            justify = CENTER,
            padx = 0, background=color).pack(pady=(5, 5))

    label8 = Label(information_window,
            text='¡Break a leg!', font=('Helvetica', 10, 'bold'),
            justify = CENTER,
            padx = 0, background=color).pack(pady=(0,2))

    label9 = Label(information_window,
            text="Created by Henfry De Los Santos", font=('Helvetica', 8, 'bold'),
            justify = CENTER,
            padx = 0, background=color).pack(pady=5)

    label10 = Label(information_window,
            text="Contact me:",
            justify = CENTER,
            padx = 0, background=color).place(x=90, y=145)

    label11 = Label(information_window,
            text="Project:",
            justify = CENTER,
            padx = 0, background=color).place(x=280, y=145)

    label12 = Label(information_window,
            text="Donate:",
            justify = CENTER,
            padx = 0, background=color).place(x=167, y=205) 

    gmail_button = Button(information_window,image=photo_img_gmail, command = open_gmail)
    stackoverflow_button = Button(information_window,image=photo_img_stack, command = open_stack_page)
    github_button = Button(information_window,image=photo_img_github, command = open_github_page)
    paypal_button = Button(information_window,image=photo_img_paypal, command = open_paypal_page)

    gmail_button.place(x=15, y=165)
    stackoverflow_button.place(x=60, y=165)
    github_button.place(x=235, y=165)
    paypal_button.place(x=125, y=225)
    information_window.resizable(False, False) 
    information_window.mainloop()

#Some variables definitions

line = Frame(root, height=1, width=400, bg="grey80", relief='groove')
line2 = Frame(root, height=1, width=400, bg=color, relief='groove')

label = Label(root,
        text="""Choose an input file type:""",
        justify = CENTER,
        padx = 20, background=color)

label3 = Label(root,
    text="In which format would you like to save the data?",
    justify = CENTER,
    padx = 20, background=color)

label4 = Label(root,
    text="In which format would you like to save the data?",
    justify = CENTER,
    padx = 20, background=color)

label5 = Label(root,
        text="Your file have been successfully created",
        justify = CENTER,
        padx = 0, background=color)

label6 = Label(root,
        text='- Click "Open File" to open it -',
        justify = CENTER,
        padx = 0, background=color)

label7 = Label(root,
        text="""Hope this program helped you.
Please take a minute and read the documentation.
If you have any questions or suggestion,
Please feel free to contact me.
All links are provided down below.""",
        justify = CENTER,
        padx = 0, background=color)

label8 = Label(root,
        text='¡Break a leg!', font=('Helvetica', 10, 'bold'),
        justify = CENTER,
        padx = 0, background=color)

label9 = Label(root,
        text="Created by Henfry De Los Santos", font=('Helvetica', 8, 'bold'),
        justify = CENTER,
        padx = 0, background=color)

label10 = Label(root,
        text="Contact me:",
        justify = CENTER,
        padx = 0, background=color)

label11 = Label(root,
        text="Project:",
        justify = CENTER,
        padx = 0, background=color)

label12 = Label(root,
        text="Donate:",
        justify = CENTER,
        padx = 0, background=color)

created_by = Label(root,
        text="Created by Henfry De Los Santos", font=('Helvetica', 9, 'bold'),
        justify = CENTER,
        padx = 0, background=color)

radio_button1 = Radiobutton(root, text="Public web page", padx = 20, 
        variable=v, background=color, 
        value=1, command = selection)

radio_button2 =Radiobutton(root, text="File (txt, pdf, json)", padx = 20, 
        variable=v, background=color, 
        value=2, command = selection)

radio_button_output_txt = Radiobutton(root, text="txt", padx = 20, 
        variable=t, background=color, 
        value=3, command = selection)

radio_button_output_csv =Radiobutton(root, text="csv", padx = 20, 
        variable=t, background=color, 
        value=4, command = selection)

radio_button_output_json = Radiobutton(root, text="json", padx = 20, 
        variable=t, background=color, 
        value=5, command = selection)

radio_button_output_pdf =Radiobutton(root, text="pdf", padx = 20, 
        variable=t, background=color, 
        value=6, command = selection)

radio_button_output_xlsx = Radiobutton(root, text="xlsx", padx = 20, 
        variable=t, background=color, 
        value=7, command = selection)

radio_button_output_docx =Radiobutton(root, text="docx", padx = 20, 
        variable=t, background=color, 
        value=8, command = selection)

next_button = Button(root, text ="Next", activebackground="black",
activeforeground="white", bd=2, width=8,
justify = CENTER, command = proof)

return_button = Button(root, text ="Return", activebackground="black",
    activeforeground="white", bd=2, width=20, command=from_2nd_page)

second_next_button = Button(root, text ="Next", activebackground="black",
    activeforeground="white", bd=2, width=20, command=last_stage)

second_return_button = Button(root, text ="Return", activebackground="black",
    activeforeground="white", bd=2, width=15, command=hide_third_window)

open_file_button = Button(root, text ="Open File", activebackground="black",
    activeforeground="white", bd=2, width=15, command=created_file_location)

finish_button = Button(root, text ="Finish", activebackground="black",
    activeforeground="white", bd=2, width=15, command=finish)


link = Label(root, text="""URL:""", padx = 10, background=color)
input_entry = Entry(root, text="", width=40)
browse1 = Button(root, text="Browser", width=7, command=input)
output_entry = Entry(root, text="", width=40)
browse2 = Button(root, text="Browser", width=7, command=output_folder)
image_size = {'Gmail':(35,30), "Stackoverflow":(150,30), "Github":(125,30),
    "Paypal":(124,30), "Info":(33, 33)}
img_gmail = Image.open("images\gmail.png")
img_stack = Image.open("images\stack.png")
img_github = Image.open("images\github.png")
img_paypal = Image.open("images\paypal.png")
img_info = Image.open("images\info.png")
img_gmail = img_gmail.resize(image_size["Gmail"], Image.ANTIALIAS)
img_stack = img_stack.resize(image_size["Stackoverflow"], Image.ANTIALIAS)
img_github = img_github.resize(image_size["Github"], Image.ANTIALIAS)
img_paypal = img_paypal.resize(image_size["Paypal"], Image.ANTIALIAS)
img_info = img_info.resize(image_size["Info"], Image.ANTIALIAS)
photo_img_gmail =  ImageTk.PhotoImage(img_gmail)
photo_img_stack =  ImageTk.PhotoImage(img_stack)
photo_img_github =  ImageTk.PhotoImage(img_github)
photo_img_paypal =  ImageTk.PhotoImage(img_paypal)
photo_img_info =  ImageTk.PhotoImage(img_info)
gmail_button = Button(root,image=photo_img_gmail, command = open_gmail)
stackoverflow_button = Button(root,image=photo_img_stack, command = open_stack_page)
github_button = Button(root,image=photo_img_github, command = open_github_page)
paypal_button = Button(root,image=photo_img_paypal, command = open_paypal_page)
info_button = Button(root,image=photo_img_info, command=information)

if __name__ == '__main__':
    start()

root.resizable(False, False) 
root.mainloop() 