import smtplib
import webbrowser
if __name__ == "__main__":
    while True:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587 
        smtp_username = str(input("Pleas enter a username: "))
        smtp_password = str(input("Pleas enter your app password: \nEnter '1' to obtain your app password.\n"))
        receiver = input("Enter receiver's gmail:")
        message = input("Enter a message\n")

        if smtp_password == '1':
            webbrowser.open('https://myaccount.google.com/apppasswords')
            continue

        connect = smtplib.SMTP(smtp_server, smtp_port)

        connect.ehlo()

        connect.starttls()

        connect.login(smtp_username, smtp_password)

        connect.sendmail(
            from_addr= smtp_username,
            to_addrs=receiver,
            msg=message
        )
        connect.quit()
        break
