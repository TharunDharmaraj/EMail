import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from docx import Document


# Login credentials for the email account you'll be sending the email from
username = 'tharundharmaraj@gmail.com'
password = 'higlwedycvdcllly'
# username = 'tharunyuvithar123@gmail.com'
# password = 'lcczmzbokcvgkugq'

recipients = []
with open("today.txt", "r") as file:
    curr = file.readline()
    while(curr):
        hash_pos = curr.find("#")
        name = curr[0:hash_pos]
        id = curr[hash_pos+1:len(curr)-1]
        this_list = [name,id]
        recipients.append(this_list)
        curr = file.readline()
        
        
# with open("emails_with_name.txt", "r") as file:
#     curr = file.readline()
#     while(curr):
#         hash_pos = curr.find("#")
#         name = curr[0:hash_pos]
#         id = curr[hash_pos+1:len(curr)-1]
#         this_list = [name, id]
#         recipients.append(this_list)
#         curr = file.readline()
# print(recipients,len(recipients))


# List of email addresses to send the email to
# recipients = [["yuvi", 'fiverryuvaraj@gmail.com'],]

for recipient in recipients:
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls(context=ssl.create_default_context())
        server.login(username, password)
        
        recipient_name = recipient[0]
        recipient_email = recipient[1]
        message = MIMEMultipart()
        # Add subject
        message["Subject"] = "Translated and dubbed video(VO) in multiple languages for channel expansion to wider audience."
        # Add sender
        message["From"] = username
        message["To"] = recipient_email
        # Create message
        html = '''
         <html>
  <head>
    <meta charset="utf-8" />
    <title>
      Translated and dubbed video in multiple languages for channel expansion to
      wider audience.
    </title>
  </head>
  <body
    style="
      background-color: #262729;
        border-radius: 16px;
        padding:25px 5px 15px;
        margin: 25px 5px 12px;
        box-shadow: 1px 1px 1.5px #000000, -1px -1px 2px #ffffff;
    "
  >
 
      <p
        style="
          color: white;
          font-size: 20px;
          font-weight: bold;
          text-align: center;
        "
      >
        Good Day {}
      </p>
      <p style="color: white; font-size: 16px">
      I love your content, so does everyone! and I think it is universal. 
      But only 16percent of the world's population can speak and understand English.
      What if I can translate and dub your youtube videos? 
      You can publish your videos in other languages, so everyone understands so well in different languages.
      Interesting.... Right.??? 
      <b>I have provided some of my works in the docx <u>attached below</u>. Please have a check on it.
      It also contains my contact details.</b>

      <p style="color: white; font-size: 16px">
        I can provide subtitles and AI-based auto-synced, translated and dubbed
        videos in these <strong>26 languages</strong> and other languages as well: Spanish,
        Hindi, Arabic, Russian, Portuguese, Italian, Indonesian, Japanese,
        Korean, German, Mandarin, Turkish, Tamil, French, Urdu, Dutch, Swedish,
        Telugu, Thai, Vietnamese, Bulgarian, Danish, Norwegian, Croatian, Greek,
        and Lithuanian are some of them.
      </p>
      <p style="color: white; font-size: 16px">
        If you want to include the background music, please send me a mp3 file
        of the background music alone(Without Voices).
      </p>
      <p style="color: white; font-size: 16px">
        <b>Pricing:</b>
One language -  2$ per minute of VO
Three languages - 1.5$ per minute of VO
Five Languages - 1.2$ per minute of VO
>5 Languages - <b>1$ per minute of VO</b>
For each language, I will be sending a video file dubbed into the respective language,
with translated captions and description for each. 
      </p>
      <p style="color: white; font-size: 16px">
        <b
          >If you want a <i>demo</i>, you just provide the link of your youtube
          video and I will provide you the dubbed version of the video with
          translated captions and Translated description.</b
        >
      </p>
      <p><u><b>I have provided some of my works in the docx. Please have a check on it.
      It also contains my contact details.</b></u></p>
      <p style="color: white; font-size: 16px">Thank You.</p>
      <p style="color: white; font-size: 16px">Regards,</p>
      <p style="color: white; font-size: 16px">Tharun.</p>
  </body>
</html>
        '''
        part1 = MIMEText(html.format(recipient_name), "html")
        message.attach(part1)
        # Open the docx file and read it
        with open("my_works_with_youtube_links.docx", "rb") as f:
            attach = MIMEText(f.read(), "base64", "utf-8")
            attach.add_header("Content-Disposition", "attachment",
                              filename="my_works_with_youtube_links.docx")
            message.attach(attach)
            
        
        server.sendmail(username, recipient_email, message.as_string())
        print(f"Email sent successfully to  {recipient_email}")
    except Exception as e:
        print(f"{recipient_email}!Unsuccessful{e}")
server.quit()
