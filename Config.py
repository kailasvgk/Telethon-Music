import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28416584"))
    API_HASH = os.environ.get("API_HASH", "f224c57df76b4114a89ea332aa24c6db")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzQBu3a1G1k9NyykAvM19HpMeFEnO31RO_SY4Etid4gSpRs5KeUd53bVIgZO2MpI08t4FxCuv07JKwTzzokMOCSmZmogXQklD3QYNejR3hRtTRh1XVesv_HKR0lNJStSXfQf6SWrt9muVoDU_y5wQhzGB5NyjlpMk6PVSAvSolcitDFzw1oOJzhVN1AmgfdGHF8PsEsMmAHFcqayGX6wA_HTaTS3z06VCJ1RyqiXihdN5W37dm8Pr_m9Ek9E7kl9hX1HlQw-9HO3hOjFT6r04xempYZyhDrGvHvhiQx4yM4Ehd60rKYSc5OA1HcV-DOcVyEOm76BSYRc76rBrNK3m7OnK58=")
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
