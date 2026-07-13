from agent import run_agent



print("汇率助手启动")
print("输入 exit 退出")



while True:

    user_input = input(
        "\n你:"
    )


    if user_input == "exit":
        break


    answer = run_agent(
        user_input
    )


    print(
        "\nAI:",
        answer
    )

# 输出回答
print(
    response.choices[0].message.content
)