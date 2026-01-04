import requests

import selectorlib
# Imports the requests and the selectorlib library

"INSERT INTO events VALUES ('Feng Suave', 'Minimalia City', '5.5.2089')"
"SELECT*FROM data WHERE date='6.5.2088'"

URL = "https://programmer100.pythonanywhere.com/tours/" # Stores the url in a variable named URL.

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
def scrape(url):# defines the function.
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)# gets the URL.
    source = response.text # Shows the page source.
    return source # returns the page source.

def extract(source):# defines another function.
    """Extract the data.txt from the source page"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml") # extracts the data.txt from extract.yaml.
    value = extractor.extract(source)["tours"] # extract the tours part from the source
    return value # returns the tours.

def send_email(mail_to_send): #defines the send_email function.
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = "farazyamaan@gmail.com"
    receiver_email = "farazyamaan@gmail.com"
    password = "kdnm tspb anwa zahg"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Upcoming tours."

    msg.attach(MIMEText(mail_to_send, "plain"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def store(extracted):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt", "r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__": # runs the program when the script is executed only in main.py.
    scraped = scrape(url=URL) # scrapes the page source.
    extracted = extract(scraped) # extracts tours from the URL.
    print(extracted) # prints tours. # stores extracted in data.txt.
    content = read(extracted)
    if extracted != "No upcoming tours": # says if extracted has No upcoming tours,
        if not extracted in content: # and says that if extracted not in data.txt, then sends the mail
            store(extracted)
            send_email(mail_to_send=extracted) # the last line of code that resembles my hardwork for 4 continous days.