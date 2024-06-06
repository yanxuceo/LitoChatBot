import os
from openai import OpenAI

from typing_extensions import override
from openai import AssistantEventHandler


openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)


# Create assistant
assistant = client.beta.assistants.create(
    name="Lito",
    instructions="You play a helpful, supportive personal assistant, and always give inspiring and precise response.",
    model="gpt-3.5-turbo-0125",
)

# Create thread
thread = client.beta.threads.create()

print(assistant)
print(thread)
