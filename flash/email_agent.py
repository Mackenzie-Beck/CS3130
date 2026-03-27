import os
import smtplib
import imaplib
from email.message import EmailMessage
import mimetypes
import validators
import email


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')




def menu():
    print("Do you want to send or fetch an email?")
    print("1 for send \n2 for fetch")
    option = input()
    if option == str(1):
        send_email()
    elif option == str(2):
        fetch_email()


def send_email():

    msg = EmailMessage()
    email_address = input("Enter recipients email address\n")
    while not validators.is_valid_email(email_address):
        email_address = input("Invalid email address, please enter valid email address: ")
    msg['To'] = email_address 


    CC_emails = []
    flag = True
    while flag:
        cc = input("Enter email address you would like to CC (Press enter if you do not want to CC): ")
        if cc == '':
            break
        while not validators.is_valid_email(cc):
            cc = input("Invalid email address, please enter valid email address: ")
        CC_emails.append(cc)
        exit = input("Would you like to CC another address? (Y/N) \n")
        if exit.lower() == 'y':
            continue
        elif exit.lower() == 'n':
            flag = False
        
    msg['CC'] = ', '.join(CC_emails)

    subject = input("Enter the emails subject line: ")
    msg['Subject'] = subject


    msg_content = input("Enter the message content:\n")
    msg.set_content(msg_content)

    is_attach = input("Will you attach a file? (Y/N)\n")
    

    if is_attach.lower() == 'y':
        attachment_file = input("Enter the name of the file you wish to attach: ")
        mime_type, _ = mimetypes.guess_type(attachment_file)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_file, 'rb') as ap:
            msg.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                                    filename=os.path.basename(attachment_file))



    elif is_attach.lower() == 'n':
        pass



    with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def fetch_email():
    
    # create an IMAP4_SSL class instance/object
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # # Listing the Folders in the mailbox
    # for i in imap.list()[1]:
    #     l = i.decode().split(' "/" ')
    #     print(l[0] + " = " + l[1])

    imap.select('inbox')
    sterm = input("Enter address you would like to search for: ")
    while not validators.is_valid_email(sterm):
        sterm = input("Not a valid email address, please enter a valid email address")
    status, messages = imap.search(None,'FROM', sterm)
    for num in messages[0].split():
        _, msg = imap.fetch(num, "(RFC822)")
        message = email.message_from_bytes(msg[0][1])
        #print(message)
        # print the message details
        subject = message['Subject']
        if subject is None:
            subject_line = '(no subject)'
        else:
            from email.header import decode_header, make_header
            subject_line = str(make_header(decode_header(subject)))
        #print(num[id])
        print("Subject:", subject_line)
        print("From:", message["From"])
        print("Date:", message["Date"])
        print("Contents:")
        for m in message.walk():
            if m.get_content_type() == "text/plain":
                print(m.as_string())

    delete = input("\nWould you like to delete the messages? (Y/N)\n")

    if delete.lower() == 'y':
        # Delete messages
        for num in messages[0].split():
            imap.store(num,'+FLAGS','\\Deleted')
        imap.expunge()
    if delete.lower() == 'n':
        exit()

if __name__ == "__main__":
    menu()