from typing import Any, Dict

from django.conf import settings
from django.db import transaction

from app.chats.models import ChatMessage, ChatRoom
from app.core.services.langchain_services import (
    LangchainRole,
    calculate_token_by_model_name,
    cast_messages,
    chat,
)


def chat_usecase(
    chat_room: ChatRoom,
    user_message: str,
    ai_model_name: str = settings.AI_MODEL_NAME,
) -> Dict[str, Any]:
    """
    チャットを行う
    - メッセージを送信する
    - メッセージをdbに登録する
    - 使用カウントを更新する
    - 最終メッセージ日時を更新する
    """

    # 過去のメッセージを取得
    chat_messages = (
        ChatMessage.objects.filter(chat_room=chat_room).order_by("-id").all()
    )

    # 送信用のメッセージリストを作成
    messages = []
    for chat_message in chat_messages:
        messages.append(
            {
                "role": chat_message.role,
                "content": chat_message.message,
            }
        )
    messages.append(
        {
            "role": LangchainRole.HUMAN.value,
            "content": user_message,
        }
    )

    # メッセージを送信
    ai_message = chat(
        cast_messages(messages),
        model=ai_model_name,
        temperature=0,
        max_tokens=4096,
        timeout=None,
        max_retries=2,
    )

    # データの保存
    with transaction.atomic():
        result = __save_usecase(chat_room, user_message, ai_message, ai_model_name)

    return result


def __save_usecase(
    chat_room: ChatRoom,
    user_message: str,
    ai_message: str,
    ai_model_name: str = settings.AI_MODEL_NAME,
) -> Dict[str, Any]:
    """
    - 1メッセージごとのデータを保存する
    """

    # dbに登録
    # ユーザーのメッセージ
    user_chat_message = ChatMessage()
    user_chat_message.chat_room = chat_room
    user_chat_message.message = user_message
    user_chat_message.message_token = calculate_token_by_model_name(
        ai_model_name, user_message
    )
    user_chat_message.role = LangchainRole.HUMAN.value
    user_chat_message.ai_model_name = ai_model_name
    user_chat_message.ai_model_version = ""
    user_chat_message.ai_model_provider = ""
    user_chat_message.save()

    # aiの回答
    ai_chat_message = ChatMessage()
    ai_chat_message.chat_room = chat_room
    ai_chat_message.message = ai_message
    ai_chat_message.message_token = calculate_token_by_model_name(
        ai_model_name, ai_message
    )
    ai_chat_message.role = LangchainRole.AI.value
    ai_chat_message.ai_model_name = ai_model_name
    ai_chat_message.ai_model_version = ""
    ai_chat_message.ai_model_provider = ""
    ai_chat_message.save()

    # 使用数カウント
    chat_room.user.count_up_message_count()

    # 最終メッセージ日時
    chat_room.last_message_at = ai_chat_message.created_at
    chat_room.save()

    return {
        "user_chat_message": user_chat_message,
        "ai_chat_message": ai_chat_message,
        "ai_chat_message": ai_chat_message,
        # "user_message_count": user_message_count,
        "chat_room": chat_room,
    }


# def chat_terraform_usecase(
#     chat_room: ChatRoom,
#     user_message: str,
#     ai_model_name: str = settings.AI_MODEL_NAME,
# ) -> Dict[str, Any]:
#     """
#     terraform用のチャットを行う

#     - メッセージを送信する
#     - メッセージをdbに登録する
#     - 使用カウントを更新する
#     """

#     # 過去のメッセージを取得
#     chat_messages = (
#         ChatMessage.objects.filter(chat_room=chat_room).order_by("-id").all()
#     )

#     if chat_messages.count() == 0:
#         # 1回目のチャット スクレイピングするかどうかも返してもらう
#         pass
#     else:
#         # 2回目のチャット
#         pass

#     # 1回目のチャット スクレイピングするかどうかも返してもらう

#     # スクレイピングする場合は、スクレイピングする
#     # しない場合は、そのまま返す

#     # 2回目のチャット

#     # 結果を返す
#     return {
#         "user_chat_message": user_chat_message,
#         "ai_chat_message": ai_chat_message,
#         "ai_chat_message": ai_chat_message,
#     }
