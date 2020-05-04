class Shops(object):
    def __init__(self):
        super().__init__()
        self.class_instance_name = "Shops"

    def test(self, parameters):
        print("[Shops][test][parameters] -> ", parameters)
        if parameters[0] == "result":
            print("[Shops][test][result] -> ", self.result)
        return {
            "status": "success",
            "data": "test",
            "class_name": self.class_instance_name,
        }
