import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28416584"))
    API_HASH = os.environ.get("API_HASH", "f224c57df76b4114a89ea332aa24c6db")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu3S7CyTwDqqvmUcKF1JtXjwD6BaTt_G7GTpeBSuNmWYAe53UOafub8GTRK9_H9_TrwQgTbgmfaCfx60ySztPElbTTjb0xeP_lWlNX7okeeO2akIDSk22vqsUgJXJ69WhpWPePSS_OCXl1obSPeBJI5jVF_4T9zANtXX1pxcQbch-0aoUql0Xwdz_fQk5Bb2y4VVWQg6TYNR7e7J5Rc9rttbbFjLyIBc3jFqoXKf5VpL-uImR1p785hoAVcYbV9zLJ2uP7daxU2NJdCZXOr9OZAvP6Yk1bPy6qengA8-At5-FUoUljea54hZnob8W7QO5jBiuq5xal41rqADeMMLLRzg=")
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
