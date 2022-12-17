from tkinter import *
import smtplib
from email.message import EmailMessage
from tkinter import messagebox

def send_message():
    sender_email = "programlostest@gmail.com"
    sender_password = "kvvwlikjiivschom"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_password)

        recipient_email = recipient_address_input.get()
        email_body = emailBody.get('1.0', END)

        print("Login Successful")

        msg = EmailMessage()
        msg.set_content(email_body)
        msg["Subject"] = subject_entry.get()
        msg["From"] = sender_email
        msg["To"] = recipient_email.strip()

        answer = analyze_message()

        if answer: server.send_message(msg)

        print("Sent Mail Successful")

        subject_entry.delete(0, END)
        recipient_address_entry.delete(0, END)
        emailBody.delete('1.0', END)
    except:
        messagebox.showerror("Error", "Something went wrong :(")

def analyze_message():
    answer = messagebox.askyesno("Question","Do you like Python?")
    return answer

app = Tk()

app.geometry("500x500")

app.title("Email Sender")

app.configure(background="blue")

# LABELS
recipient_address_label = Label(text="Recipient Email")
subject_label = Label(text="Subject")
email_body_label = Label(text="Body")

# INPUTS
recipient_address_input = StringVar()
recipient_address_entry = Entry(
    textvariable=recipient_address_input, width="66")
subject_input = StringVar()
subject_entry = Entry(textvariable=subject_input, width="66")
emailBody = Text(app, height=5, width=50)

# BUTTONS
button = Button(app, text="Send Mail", bg="green",
                command=send_message, width="30", height="3")

# PLACING
recipient_address_label.grid(row=0, column=0)
recipient_address_entry.grid(row=0, column=1)
subject_label.grid(row=1, column=0)
subject_entry.grid(row=1, column=1)
email_body_label.grid(row=2, column=0)
emailBody.grid(row=2, column=1)
button.grid(row=3, column=1)

mainloop()
