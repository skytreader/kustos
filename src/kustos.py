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
        
        root.add_widget(Image(source=self.files[0]))

    def on_pause(self):
        return True

if __name__ == "__main__":
    KustosApp().run()
