import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24813673"))
    API_HASH = os.environ.get("API_HASH", "496899c0b06b321727f69559d98c95dd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5948256402:AAGEoPItFAByHyH700w6tOX_wB0dLKiNejM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu7Bj7CRuL-OdKs5u2oo8ZcDDgtC3yqpuKS2SF1XyveF_twk4HhWcdmJ2-HlIDD6I-llLIdlKh7k0qXbo5Ll6ge-MdqrMRN9zPPzOb86gXe5jH7m1tU22ED3u5cq_c_UGkOCxQX638FrAZe3OS5vi_J8KhfcxXSdZXaPr6zDvkcCt_A64q5A-m77iCHdcaQXOOF2RECCVp-t_K8jR9w-U3_07CE3hD2_Qv0P1Nbv1UubzO66kzlg-ov6eWHJLMegrtMeV66Z3EcSpBbTK71--rOTffvy3gSYu_UZrQCw8MJVHtCdWOGBatyVTz0r1XonoSLjjIIiTis3LDBg69seJj8w=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Darshana_music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Pranav_support_chat") # Your Support
    CHANNEL = os.environ.get("OWNER", "About_kailas") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6b4415d1980b51d78286e.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c9dbb1f7ff00665698e7d.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5794079559")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
