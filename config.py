import os

from dotenv import load_dotenv


# 加载.env
load_dotenv()


# 读取API Key
DEEPSEEK_API_KEY = os.getenv(
    "DEEPSEEK_API_KEY"
)


# 检查一下
if not DEEPSEEK_API_KEY:
    raise ValueError(
        "没有找到DEEPSEEK_API_KEY，请检查.env文件"
    )