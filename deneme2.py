from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App

class PongGame(Widget):


    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            print(1)
        elif keycode[1] == 's':
            print(2)
        elif keycode[1] == 'up':
            print(3)
        elif keycode[1] == 'down':
            print(4)
        return True

class GameApp(App):
    def build(self):
        game = PongGame()
        Window.size = game.size
        return game

if __name__ == "__main__":
    GameApp().run()