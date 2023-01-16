import smtplib,ssl
from email.mime.text import MIMEText

# Login credentials for the email account you'll be sending the email from
# username = 'tharundharmaraj@gmail.com'
# password = 'higlwedycvdcllly'
username = 'tharunyuvithar123@gmail.com'
password = 'lcczmzbokcvgkugq'

# recipients = []
# with open("emails_with_name.txt", "r") as file:
#     curr = file.readline()
#     while(curr):
#         hash_pos = curr.find("#")
#         name = curr[0:hash_pos]
#         id = curr[hash_pos+1:len(curr)-1]
#         this_list = [name,id]
#         recipients.append(this_list)
#         curr = file.readline()
        
        
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
recipients = [["tharun", 'tharundharmaraj@gmail.com']]
#               ["Jared", "jared@jokullmedia.com"]]
            #   ,["Yuvi","tharunyuvithar123@gmail.com"]]
            #   ,'thirumalai@student.tce.edu', 'tharunyuvithar123@gmail.com']

# Connect to the server and send the email
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls(context=ssl.create_default_context())

server.login(username, password)

for recipient in recipients:
    try:
        recipient_name = recipient[0]
        recipient_email = recipient[1]
        # Create message
        message = MIMEText("""\
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
        border-radius: 13px;
        padding:25px 5px;
        margin: 25px 5px 25px 10px;
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
        Good Day {}!!!
      </p>
      <p style="color: white; font-size: 13px">
        I love your content, so does everyone! and I think it is universal. But only 16% of the
        world's population can speak and understand English. What if I can translate and
        dub your youtube videos. You can publish your videos in other languages, so everyone understands so well means in different languages.Interesting Right.
        Here are some examples:
      </p>
      <p style="color: white; font-size: 13px"><b>Client 1:</b></p>
      <p style="color: white; font-size: 13px">
        Original video:
        <a
          href="https://www.youtube.com/watch?v=NvsnvslVgUk"
          style="color: #0000ff; font-size: 13px"
          >Top-10-English</a
        >
      </p>
      <p style="color: white; font-size: 13px">
        Dubbed video:
        <a
          href="https://www.youtube.com/watch?v=2jgKJ5up5eo&feature=youtu.be"
          style="color: #0000ff; font-size: 13px"
          >Translated to hindi with hindi captions</a
        >
      </p>
      <p style="color: white; font-size: 13px"><b>Client 2:</b></p>
      <p style="color: white; font-size: 13px">
        Original video:
        <a
          href="https://www.youtube.com/watch?v=d8Qp18dNBqc"
          style="color: #0000ff; font-size: 13px"
          >English-Short video</a
        >
      </p>
      <p style="color: white; font-size: 13px">
        Dubbed video:
        <a
          href="https://www.youtube.com/shorts/9HupGGiObr4"
          style="color: #0000ff; font-size: 13px"
          >Dubbed and Translated to spanish with spanish subtitles</a
        >
      </p>
      <p style="color: white; font-size: 13px">
        Dubbed videos are uploaded to my channel for easy access.The video also
        has the translated captions also for the file.
        You need to just have one language video and we can translate it to N languages.
      </p>
      <p style="color: white; font-size: 13px">
        I can provide subtitles and AI-based auto-synced, translated and dubbed
        videos in these <strong>26 languages</strong> and other languages as well: Spanish,
        Hindi, Arabic, Russian, Portuguese, Italian, Indonesian, Japanese,
        Korean, German, Mandarin, Turkish, Tamil, French, Urdu, Dutch, Swedish,
        Telugu, Thai, Vietnamese, Bulgarian, Danish, Norwegian, Croatian, Greek,
        and Lithuanian are some of them.
      </p>
      <p style="color: white; font-size: 13px">
        If you want to include the background music, please send me a mp3 file
        of the background music alone(Without Voices).
      </p>
      <p style="color: white; font-size: 13px">
        <b>Pricing:</b>
      </p>
     <p  style="color: white; font-size: 13px">
     I can provide translation and AI voice-over of your 5 minute video for</p>
      <p style="color: white; font-size: 13px">$10 -> 1 language(1 video file for one language)</p>
      <p style="color: white; font-size: 13px">$20 -> 3 languages(3 video files for three languages)</p>
    <p style="color: white; font-size: 13px"> <b> $30 -> 5 languages(5 video files for five languages)</b></p>
    <p style="color: white; font-size: 13px">  And I also do custom orders with multiple languages for custom video duration based on your wish.
      (More the  languages,less the cost).</p>
      <p style="color: white; font-size: 13px">
        <b
          >If you want a <i>demo</i>, you just provide the link of your youtube
          video and I will provide you the dubbed version of the video with
          translated captions and Translated description.</b
        >
      </p>
      <p style="color: white; font-size: 13px">Thank You.</p>
      <p style="color: white; font-size: 13px">Regards,</p>
      <p style="color: white; font-size: 13px">Tharun.</p>
    <p style="text-align: center;color: white;">Contact Support</p>
    <div
      style="
       display: flex; flex-wrap: wrap;justify-content: center;
      "
    >
      <a
        href="https://twitter.com/DharmarajTharun"
        target="_blank"
        border-radius="5px"
      >
        <img
          src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-twitter-square2-512.png"
          alt="Twitter Icon"
          width="40"
          height="40"
          style="flex: 1; margin-right: 10px; border-radius:50%;margin-bottom:15px"
        />
      </a>
      <a href="https://t.me/+919489473688" target="_blank">
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQB9kQwhpeVc_Zsg0wK47GDWgoD3yi9aiENg&usqp=CAU"
          alt="Telegram Icon"
          width="40"
          height="40"
         
          style="flex: 1; margin-right: 10px; border-radius:50%;margin-bottom:15px"
          ;
        />
      </a>
      <a href="https://wa.me/+919489473688" target="_blank" border-radius="5px">
        <img
          src="https://pbs.twimg.com/profile_images/1318652224638124032/wrpp2Nl4_400x400.png"
          alt="WhatsApp Icon"
          width="40"
          height="40"
          style="flex: 1; margin-right: 10px; border-radius:50%;margin-bottom:15px"

        />
      </a>
      <a
        href="mailto:tharundharmaraj@gmail.com"
        target="_blank"
        border-radius="5px"
      >
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYOYrIg9QH40a3-R7YOBaDr0k7ai6R0yzniw&usqp=CAU"
          alt="Email Icon"
          width="40"
          style="flex: 1; margin-right: 10px; border-radius:50%;margin-bottom:15px"
          height="40"
        />
      </a>
      <a href="https://discordapp.com/users/tharun#3355" target="_blank"
        ><img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTn2LEOuCJY3YbXz4sUEOjBHb9bb0sYAAbAHA&usqp=CAU"
          alt="Discord Icon"
          width="40"
          height="40"
style="flex: 1; margin-right: 10px; border-radius:50%;margin-bottom:15px"

      /></a>
      <a
        href="https://www.linkedin.com/in/tharun-dharmaraj-004888223"
        target="_blank"
        ><img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSW1GkfjNpv6I2RNkgssOCcm7uhGcCWlhwd-A&usqp=CAU"
          alt="LinkedIn Icon"
          width="40"
          style="flex: 1; margin-right: 0px; border-radius:50%;margin-bottom:15px"
          height="40"
      /></a>
    </div>
  </body>
</html>
    """.format(recipient_name), "html")
        # Add subject
        message["Subject"] = "Translated and dubbed video in multiple languages for channel expansion to wider audience."
        # Add sender
        message["From"] = username
        message["To"] = recipient_email
        server.sendmail(username, recipient_email, message.as_string())
        print(f"Email sent successfully to  {recipient_email}")
    except Exception as e:
        print(f"{recipient_email}!Unsuccessful{e}")
server.quit()
