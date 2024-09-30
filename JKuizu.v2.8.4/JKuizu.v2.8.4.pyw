import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
from PIL import ImageTk, Image
import os
import sys
import pickle
import random
import pandas as pd

current_question = 0
length = 0
theme = "minty"
data = [current_question, length, theme]


def load_quiz_data():
    global columnq
    global columna
    global current_question
    global length
    global theme
    print(current_question)
    #current_question = dataload.current_question
    #length = dataload.length
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Define the filename of your CSV file
    csv_filename = 'quiz_all_data.csv'
    print(length)
    # Construct the full path to the CSV file
    csv_file = os.path.join(current_directory, csv_filename)

    # Read data from the CSV file using pandas
    quiz_data = []
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file, encoding='utf-8')

    # Extract all words in the second column
    #choices_column = df.iloc[:, 1]
    choices_column = df.iloc[:, columna]
    #all_choices = [word.strip() for choices_row in choices_column for word in choices_row.split(',')]
    all_choices = [str(word).strip() for choices_row in choices_column for word in str(choices_row).split(',') if not (pd.isnull(word) or 'X' in str(word))]    # Remove duplicates and empty strings
    all_choices = list(filter(None, set(all_choices)))

    # Initialize a counter to keep track of rows processed since current_question
    rows_processed = 0

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Skip rows before current_question
        if index < current_question:
            continue
        # Extract English word (question) and its translation (correct answer)
        english_word = row[columnq]  # First column contains English word (question)

        if pd.isnull(english_word) or english_word == "X":
            # Increment the counter
            rows_processed += 1
        else:            
            correct_answer = row[columna]  # Second column contains translation (correct answer)

            # Make a copy of all_choices to avoid modifying the original list
            choices = all_choices.copy()

            # Remove the correct answer from choices if it exists
            if correct_answer in choices:
                choices.remove(correct_answer)

            # Select 3 random choices if there are more than 3
            other_choices = random.sample(choices, min(3, len(choices)))

            # Combine the correct answer and other choices
            all_choices = [correct_answer] + other_choices

            # Shuffle all choices
            random.shuffle(all_choices)

            # Append question, choices, and answer to quiz_data
            quiz_data.append({
                "question": english_word,
                "choices": all_choices,
                "answer": correct_answer
            })
            
            # Increment the counter
            rows_processed += 1
            # Check if the number of processed rows reaches the length
        
        if rows_processed >= length:
            random.shuffle(quiz_data)
            return quiz_data
            #current_question = 0
            break  # Exit the loop once length is reached
    print(quiz_data)
    



def set_question(chapter):
    global columnq
    global columna
    global current_question
    global length
    global theme
    global quiz_data
    # Determine the current question and length based on the chapter
    columnq = 0
    columna = 0
    current_question = 0
    length = 0
    if chapter == "Chapter 1":
        current_question = 0
        length = 55
        columnq = 0
        columna = 1
    elif chapter == "Chapter 2":
        current_question = 0  #if you want to define the exact question number, find the number and subtrackt 2
        length = 51
        columnq = 2
        columna = 3
    elif chapter == "Chapter 3":
        current_question = 0
        length = 56
        columnq = 4
        columna = 5
    elif chapter == "Chapter 4":
        current_question = 0
        length = 62
        columnq = 6
        columna = 7
    elif chapter == "Chapter 5":
        current_question = 0
        length = 52
        columnq = 8
        columna = 9        
    elif chapter == "Chapter 6":
        current_question = 0
        length = 47
        columnq = 10
        columna = 11
    elif chapter == "Chapter 7":
        current_question = 0
        length = 56
        columnq = 12
        columna = 13
    elif chapter == "Chapter 8":
        current_question = 0
        length = 58
        columnq = 14
        columna = 15 
    elif chapter == "Chapter 9":
        current_question = 0
        length = 55
        columnq = 16
        columna = 17     
    elif chapter == "Chapter 10":
        current_question = 0
        length = 59
        columnq = 18
        columna = 19 

    print("******************CHECK*******************")
    print(length)
    print(current_question)
    print("******************CHECK*******************")

    quiz_data = load_quiz_data()
    print(quiz_data)
    show_question_layout()



def initialize_style(chapter, button_background='#cccccc', button_foreground='#262626', button_padding=10, label_font=("Segoe", 28), label_weight="bold", label_background='#fffffe', button_font=("NotoSansJP", 28), button_weight="ultrabold"):
    
    global theme
    if chapter == "Chapter 1":
        theme = "minty"
        #create_back_button()
    elif chapter == "Chapter 2":
        theme = "litera"
        #create_back_button()
    elif chapter == "Chapter 3":
        theme = "journal"
        #create_back_button()
    elif chapter == "Chapter 4":
        theme = "united"
        #create_back_button()
    elif chapter == "Chapter 5":
        theme = "yeti"
        #create_back_button()
    elif chapter == "Chapter 6":
        theme = "morph"
        #create_back_button()
    elif chapter == "Chapter 7":
        theme = "lumen"
        #create_back_button()
    elif chapter == "Chapter 8":
        theme = "united"
        #create_back_button()
    elif chapter == "Chapter 9":
        theme = "minty"
        #create_back_button()    
    elif chapter == "Chapter 10":
        theme = "litera"
        #create_back_button() 

    style = Style(theme=theme)
    style.configure('TButton', background=button_background, foreground=button_foreground, padding=button_padding, font=button_font, weight=button_weight)
    style.configure("TLabel", font=label_font, weight=label_weight, background=label_background)
    
    return Style(theme=theme) 



# Function to display the question layout
def show_question_layout():
    global columnq
    global columna
    global quiz_data
    global current_question
    global length
    print(current_question)
    print("******************KOITA**************")
    # Hide the chapter selection layout
    for widget in chapter_layout_widgets:
        widget.pack_forget()
    # Show the question layout
    for widget in question_layout_widgets:
        widget.pack()
    
    show_question()


def show_question():
    global current_question
    global length
    global quiz_data
    
    print(current_question)
    print("******************KOITA**************")
    #lambda: set_question(chapter)
    print("Current Question:", current_question)  # Add this line to check the value
    print("Length:", length)
    print(current_question)
    print(length)
    #current_question += 1
    print(current_question)
    #print(quiz_data[current_question])
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])
    choices = question["choices"]
    #print(choices)
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")
        choice_btns[i].pack(pady=10)
    feedback_label.config(text="(◔_◔) Q:"+ str(current_question + 1), foreground="black",wraplength=10000)
    next_btn.config(state="disabled")
    


# Function to check the selected answer and provide feedback
def check_answer(choice):
    global current_question
    global length
    global quiz_data
    print("********************")
    print(quiz_data)
    #current_question += 1
    question  = quiz_data[current_question]
    
    selected_choice = choice_btns[choice].cget("text")
    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{} ".format(score, length))
        feedback_label.config(text="Correct!", foreground="green",wraplength=10000)
    else:
        score_label.config(text="Score: {}/{} ".format(score, length))
        feedback_label.config(text="Incorrect!", foreground="red",wraplength=10000)
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")


# Function to move to the next question
def next_question():
    global current_question
    global length
    global quiz_data
    current_question += 1
    #if current_question < length:
    if current_question < length:
        
        show_question()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, length))
        root.destroy()



# Create the main window
root = tk.Tk()
root.iconbitmap("tori.ico")
root.title("JKuizu")

width = 852
height = 908
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

style = Style(theme="minty")
style = initialize_style(theme)
style.configure('TButton', background='#cccccc', foreground='#262626', padding=8)
style.configure("TLabel", font=("Segoe", 24), weight="bold", background='#fffffe')
style.configure("TButton", font=("NotoSansJP", 22), weight="ultrabold")

# Load and display the background image
script_dir_main = os.path.dirname(os.path.abspath(sys.argv[0]))
#navigate one folder inside
script_dir = os.path.join(script_dir_main, "gazoo")


imlist = ["1ffpic.jpg","2ffpic.jpg","3ffpic.jpg","4ffpic.jpg","dtotoro.jpg","ctotoro.jpg","atotoro.jpg","btotoro.jpg","etotoro.jpg","ftotoro.jpg","gtotoro.jpg","htotoro.jpg","itotoro.jpg","jtotoro.jpg","ktotoro.jpg"]
random.shuffle(imlist)
image_name = random.choice(imlist)
image_path = os.path.join(script_dir, image_name)
pil_image = Image.open(image_path)
pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
pil_image = pil_image.convert("RGBA")  # Ensure image has an alpha channel
background_image = ImageTk.PhotoImage(pil_image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Calculate the x-coordinate to place the buttons
#x_coordinate = root.winfo_reqwidth() // 2 + 60  # 60 pixels to the right of the center

# Create the level selection layout
genki_layout_widget = []
genki_buttons = [
    ("Genki 1", lambda: set_genki("Genki 1")),
    ("Genki 2", lambda: set_genki("Genki 2"))
]
#print(00000000000000000)
for genki, func in genki_buttons:
    button = ttk.Button(root, text=genki, command=func)
    button.pack(pady=15)
    genki_layout_widget.append(button)

# Create the chapter selection layout
chapter_layout_widgets = []


def set_genki(genki):
    for widget in genki_layout_widget:
        widget.destroy()  # Destroy all widgets in the layout
    if genki == "Genki 1":
        # Create the chapter selection layout
        chapter_buttons = [
            ("Chapter 1", lambda: [initialize_style("Chapter 1"), set_question("Chapter 1")]),
            ("Chapter 2", lambda: [initialize_style("Chapter 2"), set_question("Chapter 2")]),
            ("Chapter 3", lambda: [initialize_style("Chapter 3"), set_question("Chapter 3")]),
            ("Chapter 4", lambda: [initialize_style("Chapter 4"), set_question("Chapter 4")]),
            ("Chapter 5", lambda: [initialize_style("Chapter 5"), set_question("Chapter 5")]),
            ("Chapter 6", lambda: [initialize_style("Chapter 6"), set_question("Chapter 6")]),
            ("Chapter 7", lambda: [initialize_style("Chapter 7"), set_question("Chapter 7")]),
            ("Chapter 8", lambda: [initialize_style("Chapter 8"), set_question("Chapter 8")]),
            ("Chapter 9", lambda: [initialize_style("Chapter 9"), set_question("Chapter 9")]),
            ("Chapter 10", lambda: [initialize_style("Chapter 10"), set_question("Chapter 10")])
        ]

        for chapter, func in chapter_buttons:
            button = ttk.Button(root, text=chapter, command=func)
            button.pack(pady=10)
            chapter_layout_widgets.append(button)

    else:
        restart_button = ttk.Button(root, text="This place is off limits you dumbo!", command=restart_program)
        restart_button.pack(pady=15)





def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
# Create a label as a placeholder for the restart button icon

# Create the question layout widgets
question_layout_widgets = []
#print(111111111111111111111)
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=1000,
    padding=10
)
question_layout_widgets.append(qs_label)


choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i),
    )
    choice_btns.append(button)
    question_layout_widgets.append(button)
    #choice_btns[i].pack(pady=5)


feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
question_layout_widgets.append(feedback_label)



score = 0
score_label = ttk.Label(
    root,
    text="Ready?",
    anchor="center",
    padding=10
)
question_layout_widgets.append(score_label)


next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
question_layout_widgets.append(next_btn)

root.mainloop()
