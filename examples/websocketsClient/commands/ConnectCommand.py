from bottlenest.transports.cli import Command, CommandArgument
import re
import socketio


sio = socketio.Client()


@Command(
    name="connect",
    description="Connects to a websocket server",
)
class ConnectCommand:
    def run(self, inquirer, args):
        print(f"ConnectCommand.run: ", args.port)
        # ------------------------------
        # connect to socketio server
        # on connect

        @sio.event
        def connect():
            print("I'm connected!")
        # on disconnect

        @sio.event
        def disconnect():
            print("I'm disconnected!")
        # on message

        @sio.event
        def message(data):
            print("I received a message: ", data)
        sio.connect(f"http://localhost:{args.port}")
        # ------------------------------

        # ------------------------------
        # Use inquirer to ask for input message
        question = inquirer.Text('message', message="Enter a message")
        while True:
            answer = inquirer.prompt([question])
            if answer is None or answer['message'] is None or answer['message'] == '':
                sio.disconnect()
                break
            print("Sending message: ", answer['message'])
            sio.emit('message', answer['message'])
            sio.sleep(2)

        # ------------------------------

        # ------------------------------
        # wait until socket ends
        # sio.wait()
        # ------------------------------

        # ---
        # Example from official docs
        # questions = [
        #     inquirer.List('size',
        #                   message="What size do you need?",
        #                   choices=['Jumbo', 'Large', 'Standard',
        #                            'Medium', 'Small', 'Micro'],
        #                   ),
        # ]
        # answers = inquirer.prompt(questions)
        # print("")
        # print("Answers:")
        # print(answers)
        # ---

    @CommandArgument(
        name="port",
        # dest="port",
        type=str,
    )
    def portArg(self, value):
        return value
