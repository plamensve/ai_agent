from custom_agents.basic_agent import create_basic_agent
from tools.date_tool import get_current_date
from tools.calc_tool import calculate_expression
from tools.email_tool import send_email
from tools.excel_tool import excel_column_remover, excel_column_add

agent = create_basic_agent()

TOOLS = {
    "get_current_date": get_current_date,
    "calculate_expression": calculate_expression,
    "send_email": send_email,
    'excel_column_remover': excel_column_remover,
    'excel_column_add': excel_column_add
}


message = "Add column 'name'"

response = agent.invoke(message)

tool_messages = []

if response.tool_calls:
    for call in response.tool_calls:
        tool_name = call["name"]
        call_id = call["id"]
        args = call["args"]

        tool = TOOLS[tool_name]

        # Always pass args directly
        result = tool(**args)

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
