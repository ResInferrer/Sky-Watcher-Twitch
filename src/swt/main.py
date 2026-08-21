from chat_module.config_loader import SERVER, PORT, NICKNAME, TOKEN
from chat_module.chat_logger import TwitchChatLogger

if __name__ == "__main__":
    chat_logger = TwitchChatLogger()
    chat_logger.connect(SERVER, PORT, NICKNAME, TOKEN)

    try:
        chat_logger.start()
    except KeyboardInterrupt:
        chat_logger.remove_json()
        print("\nIt's so over...")
