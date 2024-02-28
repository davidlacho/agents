from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from pyboxen import boxen


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print("\n\n======== Sending Messages ========\n\n")
        for message in messages[0]:
            self._print_formatted_message(message)

    def _get_message_color(self, message_type):
        """
        Returns the color based on the message type.
        """
        color_map = {
            "system": "blue",
            "human": "yellow",
            "function": "green",
            "ai": "cyan",
        }
        return color_map.get(message_type, "red")

    def _format_message_content(self, message):
        """
        Formats the message content based on its type and additional arguments.
        """
        if message.additional_kwargs.get("function_call"):
            call = message.additional_kwargs["function_call"]
            return f"Running tool {call['name']} with args {call['arguments']}"
        return message.content

    def _print_formatted_message(self, message):
        """
        Prints the message in a box with the appropriate color and title.
        """
        color = self._get_message_color(message.type)
        content = self._format_message_content(message)
        self._print_message_box(content, title=message.type, color=color)

    @staticmethod
    def _print_message_box(content, title, color):
        """
        Prints the content in a box using the specified title and color.
        """
        print(boxen(content, title=title, color=color))
