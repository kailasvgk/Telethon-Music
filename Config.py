import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28416584"))
    API_HASH = os.environ.get("API_HASH", "f224c57df76b4114a89ea332aa24c6db")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBu4Ny4HaReyjdmtjwoItvGjuMSXiscM2x2EC9t0QCxHP0ln4aRZjBL8HosBgFJkxs6O3V8OLqcAoDjKX0QgLorVu6ugovKCEBtTvqZlDlG5w_5DuAojro_UW-2xw9h00u6LrPqjhXJ1xL0vR2LXMDYlLH7K2j8Had99GigE8Iu8cSezGK2V_t6PmAU-qHipFRz6Lh8Sfm_vk5S4PtWQDEgXnwRN5xqP8kzMilXdLwwNY2oFLp_iSlSDLUFxi8qcIl4LeRXqKsmSi6IqD5otBVCVbDPN6ANI5zYBUAB6l7Qg4T6XY1vLcsLujVZJxIS6n_mA_Zl6ydn6VUHf6UaCOzhcQ=")
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
