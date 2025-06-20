from utils.text_formatter import format_text
from runners.local_model_runner import run_local
import textwrap


def execute_testcase(model_name, tc_prompt) -> str:
    """Manages the execution of test cases.
    Returns:
        str: The response from the model
    """

    model_output = run_local(model_name, tc_prompt)
    if not model_output:
        print("No response generated.")
        return "NO RESPONSE!!"
    response = format_text(model_output, width=80)

    return response
