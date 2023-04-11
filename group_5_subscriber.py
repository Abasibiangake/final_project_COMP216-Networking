import json

import paho.mqtt.client as mqtt
import tkinter as tk

root = tk.Tk()


class subscriber:
    def __init__(self, topic='COMP216'):
        self.client = mqtt.Client()
        self.client.on_message = subscriber.message_handler
        self.client.connect('localhost', 1883)
        self.client.subscribe(topic)
        print(f'Subscriber listening to : {topic}\n...')

    # def message_handler(client, userdata, message):  # handler for on_message
    #     # data = message.payload.decode("utf-8")
    #     # # TODO: Process data as necessary
    #     # self.update_graph([float(x) for x in data.split(",")])
    #     print(f'\n{message.topic} \n{message.payload.decode("utf-8")}')
    #     data = [float(x) for x in message.payload.decode("utf-8").split(",")]
    #     print("Im here2")
    #     print(data)

    @staticmethod
    def message_handler(client, userdat, message):
        try:
            # Parse the data from the message
            data_str = message.payload.decode("utf-8")
            data_dict = json.loads(data_str)
            print('data_dict:', data_dict)
            #
            # Check if the data is in the expected format
            if "id" not in data_dict or "temperature" not in data_dict:
                print('data_dict:', data_dict)
                raise ValueError("Data is missing required fields")

            # Check if the data is within the expected range
            temperature = float(data_dict["temperature"])
            if temperature < 10 or temperature > 30:
                raise ValueError("Temperature is out of range")

            # TODO: Process data as necessary
            #self.update_graph(value)
            print(f'\n{message.topic} \n{data_str}')
        except Exception as e:
            # Handle errors and missing data
            print(f"Error processing message: {e}")
            print(f"\n{message.topic} \n{data_str}")

        # TODO: Update the visual display with the new data
    def block(self):
        self.client.loop_forever()

sub = subscriber()
# # Run the tkinter main loop
# root.mainloop()
sub.block()

