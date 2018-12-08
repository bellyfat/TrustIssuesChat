from src.ui.input import MessageInput
from src.message.send_message_controller import SendMessageController
from src.temp_decrypt.controller import DecryptionController


class TrustIssuesChat(object):

    @staticmethod
    def start():
        print("**********TrustIssues Chat**********")
        TrustIssuesChat._home_screen()

    @staticmethod
    def _home_screen():
        while True:
            try:
                selection = int(input("\nMain Menu\n(1) Send a new message\n(2) Exit\n\nSelection: "))
                if selection != 1 and selection != 2:
                    print("Not a valid selection\n")
                else:
                    break
            except ValueError:
                print("Not a valid input\n")

        # this dictionary has the function names
        options = {1: TrustIssuesChat._create_message, 2: TrustIssuesChat._exit}
        options[selection]()  # this calls the function using the '()' with the name selected from the dictionary

    @staticmethod
    def _create_message():
        message_text = MessageInput.read_message()
        TrustIssuesChat._confirm_message(message_text)


    @staticmethod
    def _confirm_message(message_text):
        selection = "N"
        while True:
            try:
                selection = str(input("Send message? (Y/N) "))
                if selection.upper() != "Y" and selection.upper() != "N":
                    print("Not a valid selection\n")
                else:
                    break
            except ValueError:
                print("Not a valid input\n")
            finally:
                if selection.upper() == "Y":
                    TrustIssuesChat._send_message(message_text)
                elif selection.upper() == "N":
                    TrustIssuesChat._home_screen()

    @staticmethod
    def _send_message(message_text):
            controller = SendMessageController('''session''')
            controller.send_message(message_text, '''recipient_username''')
            # controller = DecryptionController(encrypted_message_obj, "C:\\Users\\tlindblom\\RSAKeys\\private.pem")
            # print(controller.decrypt_message().get_text().decode())

    @staticmethod
    def _exit():
        print("\nGoodbye!")

