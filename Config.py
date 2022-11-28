import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25548385"))
    API_HASH = os.environ.get("API_HASH", "5e45310a94f9348f87858269b0b67005")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AQAOMTQ5LjE1NC4xNzUuNTMBu0UFixUgobmyxRdC8YacKHQIqJSGcKZHqptVdoHQJ45aPMk25sDm+ZYMzjcT6Q1usS15iY2z0AcNc39w42NSbCtOHfVNuS/t52gDwn1y6OMJ86LuS7rvXMYjztV4LKq2iwEdLZ0JuZLb4N+a6SpxkPv1ZWNFJXsfnRiWN68j36zBnpEBHcnyM7PtT4R1wlc4I/BZuO6qL2e3iHtTOPCiRgFro5EJs+lEYR35/BedRUF2oB2WODdGS/yWKTcE+WNk3FlYekABDrGa8m6aL+sElWuCwZu+n8vTtLT6AcWAB8zkZi3i4t/g57lrt21KRlAeDtnFihzY4DFFZyK9sNB28NQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Darshana_music_Support") # Your Support
    CHANNEL = os.environ.get("OWNER", "About_kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5439771489")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
