import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28451931"))
    API_HASH = os.environ.get("API_HASH", "c43d7aabe7c43ee9759485ca6665a723")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AQAOMTQ5LjE1NC4xNzUuNTMBu8Fb5CvNWT4kw/ibtMJMlcdNQxOXhDF/Vusrfu6eRfXCr/aIQ00cjO+fmKfkBGcQrUlgwA1sfdIblTazUBmr/d3mRANF+zifreQKIGOxyV901JWYHqunD2GxS/50Npva4wZF1wNSv8cmS0R4F3F+2thv0q0CDyzxZYVzfO1Lj5oOE6lapWHUc+dmwwqa2ZV+JNKU0skQhYu2akFnQaYQmkIFMSywBkeTGIwCLIpyde9g/62hueTqGl4YyfcARtJIFG3N9McbDypTdk5C4fb84kjDkaXLZunli82IIsT2XMZTeK4NzmBd3QYjnUiNPgkkIusXTlCqotHkkfOcPxtsXBM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Darshana_music_Support") # Your Support
    CHANNEL = os.environ.get("OWNER", "About_kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5449969295")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
