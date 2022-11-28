import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28416584"))
    API_HASH = os.environ.get("API_HASH", "f224c57df76b4114a89ea332aa24c6db")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu5KkSBO6U3RNHDhP3NGozIgwy5jIfr5tBuw1sv95E7kiRlJtB_NbemdecSqICcrv9ak5gALbt6CjtQJH-wTihvAqVokPpQVgl8JXsLIp0l9ESR_8RafFrknHYr0DCd9QDm-QooQG9bSDmizwCbEF2VpTyvusHketHW_EOAMEjs75J9ZwLmV3-fWW7o3IFYB8-YsEEojg1cDprQY6AXTDCkvgUKI29ls8pQkK6HwJg_etR9TiniUrtKVjs73XlIqh9uuZM_61G6zSaUR21fpr2RIgHHgozeAC-57HC3vQYu6MXi2Fy_DLOBojEyFeHok0aHgDMuZ7DvHkCfHopJjlz3Y=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Darshana_music_Support") # Your Support
    CHANNEL = os.environ.get("OWNER", "About_kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5775058591")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
