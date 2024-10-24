from enum import Enum
from typing import List

import tiktoken
from django.conf import settings
from langchain.schema import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


class LangchainRole(Enum):
    AI = "ai"
    HUMAN = "human"
    SYSTEM = "system"


def chat(
    messages: List[BaseMessage],
    model=settings.AI_MODEL_NAME,
    temperature=0,
    max_tokens=4096,
    timeout=None,
    max_retries=2,
) -> str:
    chat = ChatOpenAI(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
        max_retries=max_retries,
        api_key=settings.OPENAI_API_KEY,
    )
    result = chat(messages)
    return str(result.content)


def calculate_token_by_model_name(model_name: str, text: str) -> int:
    enc = tiktoken.encoding_for_model(model_name)
    tokens = enc.encode(text)

    return len(tokens)


def cast_messages(messages: list) -> List[BaseMessage]:
    cast_messages: List[BaseMessage] = []
    for message in messages:
        if message["role"] == LangchainRole.AI.value:
            cast_messages.append(AIMessage(content=message["content"]))
            continue

        if message["role"] == LangchainRole.HUMAN.value:
            cast_messages.append(HumanMessage(content=message["content"]))
            continue

        if message["role"] == LangchainRole.SYSTEM.value:
            cast_messages.append(SystemMessage(content=message["content"]))
            continue

    return cast_messages
