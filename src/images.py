class Images(object):

    def __init__(self):
        super().__init__()
        self.class_instance_name = "Images"

    def test(self, parameters):
        print("[Images][test][parameters] -> ", parameters)
        return {
            "status": "success",
            "data": "test",
            "class_name": self.class_instance_name,
        }