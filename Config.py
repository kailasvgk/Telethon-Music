import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29693770"))
    API_HASH = os.environ.get("API_HASH", "e23545c738c0f214f88f4acaeaa8a8b8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBu4q9OU0eVdIsliXQjiHmzkfzqF0iiQulRZ_zsBNnMTeiICRC_EYYsIMona8mL_QjjG3g2Nq0EPshL25SASSzOiogrMLcMQd_2Y7bKvJaVIsNUzi3Nl1vrrQCLtLuCEnXe4kMoDpPNjxHEgC58L38TTTaTikrDmooxXlIQElAApyOEvQHHpSCpZJ4rFClpD_-Q18PG6tyL9Gq26z0Y3yZYVjNCmmXVPiBbKcIOFPxJbKXdXbthxkFHn9RQgS6A1qpeFiiPpcgmNMMo9zWRBZSjTvk4Nm7EmCoiz9hJYBr6zzyPqTqvBNXmFk-zV92BsxT62KUHbjYSHSDvnOV6eOogQc=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Pranav_support_chat") # Your Support
    CHANNEL = os.environ.get("OWNER", "Hell_federation_tg") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1749940054")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
