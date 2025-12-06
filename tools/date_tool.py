from langchain.tools import tool
from datetime import datetime


@tool
def get_current_date() -> str:
    """Returns the current date."""
    return datetime.now().strftime("%Y-%m-%d")
