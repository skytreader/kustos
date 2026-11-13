import kivy
kivy.require("1.0.6")

from kivy.app import App

class KustosApp(App):

    def build(self):
        root = self.root

    def on_pause(self):
        return True

if __name__ == "__main__":
    KustosApp().run()
