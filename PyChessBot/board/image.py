from mss import mss


class BoardImage:

    def __init__(self, coord, width, height):
        self.region = {
            "top": coord[1],
            "left": coord[0],
            "width": width,
            "height": height
        }
        self.sct = mss()

    def snap(self):
        return self.sct.grab(self.region)