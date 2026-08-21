from irc.client import SimpleIRCClient

from .config_loader import SERVER, CHANNEL

import datetime
import json
import os

class TwitchChatLogger(SimpleIRCClient):
    def __init__(self):
        super().__init__()
        self.messages = []
        self.log_filename = "chat_log.jsonl"

    def on_welcome(self, connection, event):
        """After successful connection, we request opportunities and enter the channel."""
        print(f"Connected to {SERVER}. Request Opportunities...")
        connection.cap("REQ", "twitch.tv/tags twitch.tv/commands twitch.tv/membership")
        connection.join(CHANNEL)
        print(f"Join the channel {CHANNEL}")

    def on_join(self, connection, event):
        """Channel entry confirmation."""
        print(f"Successfully joined {event.target}")

    def on_pubmsg(self, connection, event):
        """Handler for new messages in a channel."""
        # Extract the sender's nickname
        user = event.source.nick

        # Extract the text of the message
        message = event.arguments[0] if event.arguments else ""

        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S")
    
        log_entry = {
            "user": user,
            "message": message,
            "timestamp": timestamp
        }

        self.messages.append(log_entry)
        self._append_to_json(log_entry)
        print(f"[{timestamp}] {user}: {message}")

    def remove_json(self):
        """Deletes the JSON file with logs"""
        if os.path.exists(self.log_filename):
            os.remove(self.log_filename)

    def _append_to_json(self, log_entry):
        """Appends one message to the JSON file with logs"""
        with open(self.log_filename, "a", encoding="utf-8") as f:
            json.dump(log_entry, f, ensure_ascii=False)
            f.write("\n")

    