from openai import OpenAI
from config import DEEPSEEK_API_KEY
from tools import exchange_tool


client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)



tools = [

    {
        "type": "function",

        "function": {

            "name": "exchange_tool",

            "description":
            "计算两个货币之间的兑换金额",

            "parameters": {

                "type": "object",

                "properties": {

                    "from_currency": {
                        "type": "string",
                        "description":
                        "原始货币，例如USD"
                    },


                    "to_currency": {
                        "type": "string",
                        "description":
                        "目标货币，例如CNY"
                    },


                    "amount": {
                        "type": "number",
                        "description":
                        "金额"
                    }

                },


                "required": [
                    "from_currency",
                    "to_currency",
                    "amount"
                ]
            }
        }
    }
]

def run_agent(user_input):


    messages = [

        {
            "role": "system",
            "content":
            """
            你是一个汇率计算助手。
            如果用户需要汇率计算，
            请调用 exchange_tool。
            """
        },


        {
            "role": "user",
            "content": user_input
        }

    ]


    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=messages,

        tools=tools

    )


    message = response.choices[0].message


    # 判断AI是否想调用工具

    if message.tool_calls:


        tool_call = message.tool_calls[0]


        # 获取AI生成的参数
        import json

        args = json.loads(
            tool_call.function.arguments
        )


        # 真正执行工具
        result = exchange_tool(
            **args
        )


        return f"""
根据当前汇率：

{result['amount']} {result['from']}
≈ {result['result']:.2f} {result['to']}

当前汇率：
1 {result['from']}
≈ {result['rate']} {result['to']}
"""


    else:

        return message.content