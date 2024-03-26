import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()

window.title("Form")

#seached Google for this command for astetic
window.configure(bg="#333333")

label0 = tk.Label(window, text="*Not Requried*", bg="#333333", fg="pink")
label0.pack()

label9 = tk.Label(window, text="Please Fill out the Form", bg="#333333", fg="white")
label9.pack()

label_ = tk.Label(window, height=7, bg="#333333")
label_.pack()

label1 = tk.Label(window, text="Name:", bg="#333333", fg="white")
entry1 = tk.Entry(window, width=25)
label1.pack()
entry1.pack()

label2 = tk.Label(window, text="Adress Line 1:", bg="#333333", fg="white")
entry2 = tk.Entry(window, width=50)
label2.pack()
entry2.pack()

label3 = tk.Label(window, text="Adress Line 2:", bg="#333333", fg="pink")
entry3 = tk.Entry(window, width=50)
label3.pack()
entry3.pack()

label4 = tk.Label(window, text="City:", bg="#333333", fg="white")
entry4 = tk.Entry(window, width=20)
label4.pack()
entry4.pack()

label5 = tk.Label(window, text="State:", bg="#333333", fg="white")
entry5 = tk.Entry(window, width=20)
label5.pack()
entry5.pack()

label6 = tk.Label(window, text="Zip Code:", bg="#333333", fg="white")
entry6 = tk.Entry(window, width=20)
label6.pack()
entry6.pack()

label7 = tk.Label(window, text="Phone Number:", bg="#333333", fg="white")
entry7 = tk.Entry(window, width=50)
label7.pack()
entry7.pack()

label8 = tk.Label(window, text="Email Adress:", bg="#333333", fg="pink")
entry8 = tk.Entry(window, width=50)
label8.pack()
entry8.pack()

label10 = tk.Label(window, height=3, bg="#333333")
label10.pack()

button1 = tk.Button(window, text="Submit")
button1.pack()



window.mainloop()