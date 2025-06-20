# Placeholder for text formatter
import textwrap


def format_text(txt: str, width: int = 80) -> str:
    """
    Strips out leading and trailing whitespace and
    Formats the input text to a specified width, wrapping lines as necessary.

    Args:
        text (str): The input text to format.
        width (int): The maximum line width for formatting.

    Returns:
        str: The formatted text with wrapped lines.
    """

    strpTxt = txt.strip()
    formTxt = textwrap.fill(strpTxt.strip(), width=width)
    return formTxt
