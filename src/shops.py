from termcolor import colored


class Shops(object):
    def __init__(self):
        super().__init__()
        self.class_instance_name = "Shops"

    def test(self, parameters):
        print(f"[{colored('OK', 'green')}][test][parameters] -> {parameters}")
        if parameters[0] == "result":
            print("[Shops][test][result] -> ", self.result)
        return {
            "status": "success",
            "data": parameters[0],
            "class_name": self.class_instance_name,
        }
