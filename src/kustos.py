import kivy
kivy.require("1.0.6")

from kivy.app import App
from kivy.uix.image import Image
from os.path import join, dirname
from glob import glob

class KustosApp(App):

    def build(self):
        root = self.root
        curdir = dirname(__file__)
        self.files = [filename for filename in glob(join(curdir, "images", "*"))]
        
        self.image_idx = 0
        self.root.ids["main_img"].source = self.files[self.image_idx]

    def on_pause(self):
        return True

    def next_image(self):
        self.image_idx += 1
        self.root.ids["main_img"].source = self.files[self.image_idx]

if __name__ == "__main__":
    KustosApp().run()
