from langchain.tools import tool


@tool
def calculate_expression(expression: str) -> str:
    """
    Evaluate mathematical expression
    :param expression:
    :return: str
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Error {e}"
