import tkinter
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler


win = tkinter.Tk()
win.title("FTIR Analysis Based on Key Words")


frame = tkinter.Frame(win, width=300)
frame.pack()

first_frame = tkinter.LabelFrame(frame, width=300)
first_frame.grid(row=0, column=0, padx=20, pady=10, sticky="news")

label1 = tkinter.Label(first_frame, text="Please Select a Part :  From Part 1 to Part 25 ")
label1.grid(row=1, padx=5, pady=3, sticky='w')
label1_entry = tkinter.Entry(first_frame, width= 10)
label1_entry.grid(row=2, padx=5, pady=3)

def printinp():
    label_new = tkinter.Label(first_frame, text=label1_entry.get())
    label_new.grid(row=1, column=2)

button1 = tkinter.Button(first_frame, text="Execute", command = printinp)
button1.grid(row=2, column=2, padx=50, pady=5)

def _quit():
    win.quit()
    win.destroy()

button2 = tkinter.Button(first_frame, text="End", command=_quit)
button2.grid(row=2, column=3, padx=50, pady=5)


second_frame = tkinter.LabelFrame(frame)
second_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

def FTIR():
    df = pd.read_csv('data.csv')
    data = df[df['Part Name'] == label1_entry.get()]
    counts = data.value_counts()
    label_new = tkinter.Label(second_frame, text=counts.values.sum())
    label_new.grid(row=0, column=1, sticky='E')

buttonFTIR = tkinter.Button(second_frame, text="Total FTIRs Found", command=FTIR)
buttonFTIR.grid(row=0, padx=5, pady=3, sticky='W')

def FA():
    df = pd.read_csv('data.csv')
    data = df[df['Part Name'] == label1_entry.get()]
    label_new = tkinter.Label(second_frame, text=round(data['FAULT_MONTHS'].mean()))
    label_new.grid(row=1, column=1, sticky='E')

buttonFA = tkinter.Button(second_frame, text="Average Fault Months", command=FA)
buttonFA.grid(row=1, padx=5, pady=3, sticky='W')


third_frame = tkinter.LabelFrame(frame)
third_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

forth_frame = tkinter.LabelFrame(frame)
forth_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

def pmwt():
    fig = Figure(figsize=(7, 4), dpi=100)
    df = pd.read_csv('data.csv')
    data = df[df['Part Name'] == label1_entry.get()]
    plt = fig.add_subplot(111)
    counts = data["PROCESSING_MONTH"].value_counts()
    plt.bar(counts.index, counts.values)
    plt.set_title("Processing Month Wise Trend")
    plt.set_xlabel("Processing Month and Year")
    plt.set_ylabel("Count")
    canvas = FigureCanvasTkAgg(fig, master=forth_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, forth_frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)

button3 = tkinter.Button(third_frame, text="Processing Month Wise Trend", command = pmwt)
button3.grid(row=0, column=1, padx=10, pady=5)

def fmwt():
    fig = Figure(figsize=(5, 4), dpi=100)
    df = pd.read_csv('data.csv')
    data = df[df['Part Name'] == label1_entry.get()]
    plt = fig.add_subplot(111)
    counts = data["FCOK_MONTH"].value_counts()
    plt.bar(counts.index, counts.values)
    plt.set_title("FCOK Month Wise Trend")
    plt.set_xlabel("FCOK Month and Year")
    plt.set_ylabel("Count")
    canvas = FigureCanvasTkAgg(fig, master=forth_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, forth_frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)

button4 = tkinter.Button(third_frame, text="FCOK Month Wise Trend", command = fmwt)
button4.grid(row=0, column=2, padx=10, pady=5)

def mwh():
    fig = Figure(figsize=(5, 4), dpi=100)
    df = pd.read_csv('data.csv')
    data = df[df['Part Name'] == label1_entry.get()]
    plt = fig.add_subplot(111)
    plt.hist(x="ODOMETER", data=data)
    plt.set_title("Mileage wise History")
    plt.set_xlabel("Mileage")
    plt.set_ylabel("Count")
    canvas = FigureCanvasTkAgg(fig, master=forth_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, forth_frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)

button5 = tkinter.Button(third_frame, text="Mileage Wise Histogram", command = mwh)
button5.grid(row=0, column=3, padx=10, pady=5)

def mudt ():
    fig = Figure(figsize=(5, 4), dpi=100)
    df = pd.read_csv('data.csv')
    data = df[df['Part Name'] == label1_entry.get()]
    plt = fig.add_subplot(111)
    plt.scatter(x="ODOMETER", y = "USAGE_MONTHS", data=data)
    plt.set_title("Mileage vs Usage Days Trend")
    plt.set_xlabel("Mileage")
    plt.set_ylabel("Usage in Months")
    canvas = FigureCanvasTkAgg(fig, master=forth_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, forth_frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)

button6 = tkinter.Button(third_frame, text="Mileage vs Usage Days Trend", command=mudt)
button6.grid(row=1, column=1, padx=10, pady=5)

def mnwt():
    fig = Figure(figsize=(5, 4), dpi=100)
    df = pd.read_csv('data.csv')
    data = df[df['Part Name'] == label1_entry.get()]
    plt = fig.add_subplot(111)
    counts = data["Model"].value_counts()
    plt.bar(counts.index, counts.values)
    plt.set_title("Model Wise History")
    plt.set_xlabel("Model")
    plt.set_ylabel("Count")
    canvas = FigureCanvasTkAgg(fig, master=forth_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, forth_frame)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)

button7 = tkinter.Button(third_frame, text="Model Name Wise Trend", command=mnwt)
button7.grid(row=1, column=2, padx=10, pady=5)

def clean():
    for widget in forth_frame.winfo_children():
        widget.destroy()

button7 = tkinter.Button(third_frame, text="Clear Graph", command=clean)
button7.grid(row=1, column=3, padx=10, pady=5)


win.mainloop()
