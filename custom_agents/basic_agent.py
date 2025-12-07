import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from tools.excel_tool import excel_column_remover, excel_column_add
from tools.calc_tool import calculate_expression
from tools.date_tool import get_current_date
from tools.email_tool import send_email


load_dotenv()
tools = [get_current_date, calculate_expression, send_email, excel_column_remover, excel_column_add]


def create_basic_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    llm_with_tools = llm.bind_tools(tools)

    return llm_with_tools
