import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22593868"))
    API_HASH = os.environ.get("API_HASH", "88e4304cc7a5dfc2f54763e9ee21a9ac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzgBu7hW8PrSXRFQMVNm0iYaLVn0VavGsWq2EK7LSR156JsMQPc4tupyiRMUfqOHFFyJUHPemIJrhw2rE1tfYQTKNl7idwU9xaT_v8cO5dpG4TWx9fw7CmvLxYHvbbYA5lELie_951iBVQgqRROJa80aKfiMjcYhXn8Kd_EctwbaFJzL3Id3T95BT7dSP-BN2xgdJ--zsrKqyQf0FYN0NQBBbwYpstFFQpRi2BdPa7O37eSIBvdongSBgZof6i1GAbNCUIb1GM9C0PhDex2B8cVo4s9L6hP5x-i3L0kpcLMtg69dNPcuLur5iZ2RrEmt3HTJP7sFKmoE7V0Ikq68MJj-VjI=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Darshana_music_Support") # Your Support
    CHANNEL = os.environ.get("OWNER", "About_kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5794211496")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
