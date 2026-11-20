import kivy
kivy.require("1.0.6")

from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from os.path import join, dirname
from glob import glob

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    rootpath = "/home/cestioco"

class KustosApp(App):

    def build(self):
        root = self.root
        curdir = dirname(__file__)
        self.files = [filename for filename in glob(join(curdir, "images", "*"))]
        
        self.image_idx = 0
        self.root.ids["main_img"].source = self.files[self.image_idx]
        self._popup = None

    def on_pause(self):
        return True

    def next_image(self):
        self.image_idx += 1
        self.root.ids["main_img"].source = self.files[self.image_idx]

    def show_load(self):
        content = LoadDialog()
        self._popup = Popup(title="Load Source Directory", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def callback_load(self, path, filename):
        pass

    def close_popup(self):
        self._popup.dismiss()

Factory.register("LoadDialog", cls=LoadDialog)

if __name__ == "__main__":
    KustosApp().run()
