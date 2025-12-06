from custom_agents.basic_agent import create_basic_agent
from tools.date_tool import get_current_date
from tools.calc_tool import calculate_expression
from tools.email_tool import send_email

agent = create_basic_agent()

TOOLS = {
    "get_current_date": get_current_date,
    "calculate_expression": calculate_expression,
    "send_email": send_email,
}

response = agent.invoke(
    "Send an email to svetoslavov.dev@gmail.com and say HI"
)

tool_messages = []

if response.tool_calls:
    for call in response.tool_calls:
        tool_name = call["name"]
        call_id = call["id"]
        args = call["args"]

        tool = TOOLS[tool_name]

        # Always pass args directly
        result = tool.invoke(args)

        tool_msg = {
            "role": "tool",
            "tool_call_id": call_id,
            "content": result
        }

        tool_messages.append(tool_msg)

    final = agent.invoke([response, *tool_messages])
    print("FINAL ANSWER:", final.content)

else:
    print("FINAL ANSWER IS:", response.content)
