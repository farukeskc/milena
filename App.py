from tkinter import *
import smtplib
from email.message import EmailMessage
from tkinter import messagebox
import re
import traceback
import logging

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def quit_server():
    server.quit()
    print("Server Closed")

def isValid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def send_message():
    defaultSenderEmail = "programlostest@gmail.com"
    defaultSenderPassword = "kvvwlikjiivschom"

    inputSenderAddressText = inputSenderAddress.get('1.0', END).strip()
    inputSenderPasswordText = entrySenderPassword.get().strip()

    try:
        global server
        server = smtplib.SMTP(smtpHostOption.get(), 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(inputSenderAddressText, inputSenderPasswordText)

        emailRecipient = inputRecipientAddress.get().strip()
        emailBody = inputEmailBody.get('1.0', END)

        msg = EmailMessage()
        msg.set_content(emailBody)
        msg["Subject"] = entrySubject.get()
        msg["From"] = inputSenderAddressText
        msg["To"] = emailRecipient
        msg["Cc"] = inputCC.get('1.0', END).strip().split(",")
        msg["Bcc"] = inputBCC.get('1.0', END).strip().split(",")

        if isValid(emailRecipient):
            answer = messagebox.askyesno("Question", "Do you like Python?")
            if answer:
                server.send_message(msg)
        else:
            raise Exception("Invalid recipient email")

        print("Sent Mail Successful")

        entrySubject.delete(0, END)
        entryRecipientAddress.delete(0, END)
        inputEmailBody.delete('1.0', END)
        inputCC.delete('1.0', END)
        inputBCC.delete('1.0', END)
    except Exception as e:
        messagebox.showerror("Error", "Something went wrong :(")
        logging.error(traceback.format_exc())

################################# UI #################################


app = Tk()

app.geometry("700x700")
app.minsize(700, 700)
app.maxsize(700, 700)

app.title("Email Sender")

app.configure(background="gray")

# LABELS
lblRecipientAddress = Label(text="Recipient Email:",
                            background="gray", fg="white", font=("Arial", 16))
lblSubject = Label(text="Subject:", background="gray",
                   fg="white", font=("Arial", 16))
lblEmailBody = Label(text="Body:", background="gray",
                     fg="white", font=("Arial", 16))
lblCC = Label(text="CC:", background="gray",
              fg="white", font=("Arial", 16))
lblBCC = Label(text="BCC:", background="gray",
               fg="white", font=("Arial", 16))
lblSenderAddress = Label(text="Sender Email:",
                         background="gray", fg="white", font=("Arial", 16))
lblSenderPassword = Label(text="Sender Password:",
                          background="gray", fg="white", font=("Arial", 16))

# INPUTS
inputSenderAddress = Text(app, height=1, width=50)
inputSenderPassword = StringVar()
inputCC = Text(app, height=1, width=50)
inputBCC = Text(app, height=1, width=50)
inputEmailBody = Text(app, height=5, width=50)
inputRecipientAddress = StringVar()
inputSubject = StringVar()
entrySenderPassword = Entry(textvariable=inputSenderPassword, width="66", show="*")
entryRecipientAddress = Entry(
    textvariable=inputRecipientAddress, width="66")
entrySubject = Entry(textvariable=inputSubject, width="66")

# Radio
smtpHostOption = StringVar(app, "smtp.gmail.com")
radioGmail = Radiobutton(app, text="Gmail (SMTP Host)", variable=smtpHostOption,
                         value="smtp.gmail.com", font=("Arial", 16))
radioOutlook = Radiobutton(app, text="Outlook (SMTP Host UNAVAILABLE)", variable=smtpHostOption,
                           value="smtp-mail.outlook.com", font=("Arial", 16))

# BUTTONS
buttonSend = Button(app, text="Send Mail", bg="green",
                command=send_message, width="30", height="3", fg="white", font=("Arial", 16))
buttonQuit = Button(app, text="Quit Server", bg="red",
                command=quit_server, width="15", height="3", fg="white", font=("Arial", 16))

# PLACING
widgetsLabel = [lblSenderAddress, lblSenderPassword,
                lblRecipientAddress, lblCC, lblBCC, lblSubject, lblEmailBody]
widgetsInput = [inputSenderAddress, entrySenderPassword,
                entryRecipientAddress, inputCC, inputBCC, entrySubject, inputEmailBody]


def place(labels, inputs):
    for i in range(1, len(labels) + 1):
        labels[i-1].grid(sticky="EN", row=i, column=0,
                         pady=(10, 10), padx=(20, 10))
        inputs[i-1].grid(row=i, column=1, pady=(10, 10))
    buttonSend.grid(row=len(labels) + 1, column=1)
    buttonQuit.grid(row=len(labels) + 1, column=0)


radioGmail.grid(sticky="EN", row=0, column=0,
                       pady=(10, 10), padx=(20, 10))
radioOutlook.grid(sticky="EN", row=0, column=1,
                  pady=(10, 10), padx=(20, 10))

place(widgetsLabel, widgetsInput)

mainloop()
