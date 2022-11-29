import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28416584"))
    API_HASH = os.environ.get("API_HASH", "f224c57df76b4114a89ea332aa24c6db")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBu8bDkUvtXWCf9J_0q-7SZ2kN3T3IFyWpyXzwcaAYaJJ6j9ZDgnOoSz0RYTXDG8heeA3yHbt2TdJbNg6AbsyZYTIxcEx7tvcI72heZt7ZIQE9tshz45K2yzvzHXmn4AR-yiNa1u25BgGM8yysr5rt7Zg36_1x-enFe-K30peA1TIV7X0_EN1D6j_45l04COfkRH5JXt-bP_RswaicfJq1T_-33vuSm7OsDUk9ZbiIvQ2ZtwTwouS8dvD6T5eGgp9_9UGmz07EE5ccf7mfq1p3T9DylXTa1FyjhcX0jt5GfUMLPRZ3S_2xKylNWFkOGVc2hIBzcCV4t_4-5UN_4Oj8IVU=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Pranav_support_chat") # Your Support
    CHANNEL = os.environ.get("OWNER", "About_kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5775058591")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
