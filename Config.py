import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24011262"))
    API_HASH = os.environ.get("API_HASH", "8fa5e5c8ba714201850d753e34402eb9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzwBu26vAQdMAlypZ-1M7_4PP-u365kcd29IOOo4LIWQV8VPocYcslFlhCySnuMzKLB4gLhRVUK8FpDST0IPJw--1zCd5AH7SAXZNljsK6AnfM0CfnOHgOz9lhBN1hZP5a-qUD08MzP_0g7AubGOhtqywTkS-Co0EqBBRoFLRg2xbArvYxl0I6H3OyMmwGMTtsz-03htz-hmzy9BD1QJa4L12iP9xloZax9r3ZaAM5yLw8hTZDGfCsltAcxHbIYixAUzWw7CiFPS2nizNpETzIA1-pqEeCeZ3u18OMYjRaWRxCzskA37o07JoJkKx_CSuffcEt6qZh4QeyynQfo1ViqE3y0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Darshana_music_Support") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "About_kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5669457850")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
