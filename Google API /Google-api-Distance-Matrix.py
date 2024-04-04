# From Patrick Test stuff
import requests
import smtplib

# Stored google API key in txt file and open in read
api_file = open("***GOOGLE_API***", "r")
api_key = api_file.read()
api_file.close()

# enter start point
home = input("Enter a home address\n")

# enter destination
destination = input("Enter a destination\n")

url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get the response
r = requests.get(url + "origins=" + home + "&destinations=" + destination + "&key=" + api_key)

# return the tme as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

print("\nThe total travel time from home to destination is", time, round(seconds/60,2), "m.s")

# Check if the total travel time is more than 1 hour/60x60= 3600
"""
This is for the email to send if we hit a certain criteria,
We will use the SMTPLIB for this to send emails using python.
"""
if seconds > 3600:
    # These are the email constraints
    sender = "test@gmail.com"
    recipient = "test@gmail.com"
    subject = "News for you"
    message = "Hey, \n\nIts going to take me over 60 minutes to get there!!!."

    # format for the email
    email = "Subject: {}\n\n{}".format(subject, message)

    # Get my email
    password_file = open("***FILE_NAME***", "r")
    password = password_file.readline()
    password_file.close()

    # This creates an SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # Use tls for security
    s.starttls()

    # authenticate my login
    s.login(sender, password)

    # to send the email
    s.sendmail(sender, recipient, email)

    # finish the session
    s.quit()

    # message to confirm success
    print("\nYour message to", recipient, "was sent successfully")

else:
    print("Womp womp try again")
