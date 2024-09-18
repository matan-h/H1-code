from openai import OpenAI
from typing import Callable

chat_system_prompt = """v
You are a highly intelligent code converter specialized in converting code to H1-quality {lang} code. H1-quality code adheres to the following guidelines:
0. No hallucinations: dont invent things that arent there yet (for example, dont create a new class out of no where). if you cant convert this file, only write a single line "Error: <short explanation>". no codeblock, and DONT write a placeholder
1. Clear Code
2. No redundant or duplicate code.
3. Concise and Relevant Comments: Include only useful, *professional comments* that describe the code flow or clarify important logic. Avoid trivial comments (e.g., "//set a to 5") and keep comments short.
3. Write comments only when you fully understand the code and its context. *Do not add comments if you're unsure of their correctness or necessity*.
4. Retain only essential, concise comments when absolutely necessary to explain complex logic or the overall flow.
5. very very very minimal (ideally one line or less), Clean and clear documentation.
6. No commented-out or unused code. 
7. High-quality {lang} code with best practices.
8. Thoughtful and meaningful naming conventions.
9. No typos in the code or comments.
10. Smart conversion that improves code without introducing issues.  For example, do not replace variables with functions or make unnecessary changes that alter the code's intent or efficiency.
11. Preserve high-quality code from the original and ensure no functionality is lost. (for example, Make sure you dont change constants values that make the code works.)

Your task is to convert the code strictly according to these principles. The output should be code only. note that the files given to you are just a part of a larger codebase."""


# Default callback that prints streamed messages
print_callback = lambda message: print(message, end="", flush=True)


# Class for configuration settings
class AiConfig:
    def __init__(
        self,
        model: str = "llama3.1",
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",
    ):
        self.model = model
        self.base_url = base_url
        self.api_key = api_key


def ai(
    source_code: str,
    lang: str,
    filename,
    config: AiConfig,
    stream_callback: Callable[[str], None] = print_callback,
):
    # Initialize OpenAI client with config parameters
    client = OpenAI(
        base_url=config.base_url,
        api_key=config.api_key,  # required, but unused
    )

    # Set up streaming from the client
    stream = client.chat.completions.create(
        model=config.model,
        messages=[
            {
                "role": "system",
                "content": chat_system_prompt.format(lang=lang),
            },
            {
                "role": "user",
                "content": f"rewrite this code in H1 quality:\nfilename:{filename}:```{lang.lower()}\n{source_code}\n```",
            },
        ],
        stream=True,
        stop=["```\n"],
    )

    full_markdown = ""
    for chunk in stream:
        message = chunk.choices[0].delta.content
        if message:
            full_markdown += message
            stream_callback(message)

    # If a valid code block is not found, raise an error
    if f"```{lang.lower()}" in full_markdown:
        code = full_markdown.split(f"```{lang.lower()}")[1]
        return code
    else:
        raise ValueError(
            full_markdown,'have no codeblock in the correct language'
        )

    return full_markdown


# print(response['message']['content'])
# breakpoint()