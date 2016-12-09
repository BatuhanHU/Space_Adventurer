from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

#oyuncu gemisi texture si
class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = (120, 80)

# arka plan texture si
class Sprite2(Image):
    def __init__(self, **kwargs):
        super(Sprite2, self).__init__(**kwargs)
        self.size = self.texture_size

#arka plan haraketliliğini sağlayan class
class BG(Widget):
    def __init__(self, source):
        super(BG, self).__init__()
        self.image = Sprite2(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite2(source=source, x=self.width)
        self.add_widget(self.image_dupe)


    def update(self):
        self.image.x -= 0.5
        self.image_dupe.x -= 0.5

        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width

#gemi haraketliliğini sağlayan class
class PlayerShip(Sprite):
    def __init__(self, pos):
        super(PlayerShip, self).__init__(source="Spaceship1.png", pos=pos)
        self.velocity_y = 0
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.velocity_y = 10
        elif keycode[1] == 's':
            self.velocity_y = -10
        #return True


    def update(self):

        self.y += self.velocity_y
        self.velocity_y = 0


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.background = BG(source="BackGround1.png")
        self.size = self.background.size
        self.add_widget(self.background)
        self.PlayerShip = PlayerShip(pos=(0, self.height / 2))
        self.add_widget(self.PlayerShip)
        Clock.schedule_interval(self.update, 1.0/60.0)

    def update(self, *ignore):
        self.background.update()
        self.PlayerShip.update()


class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == "__main__":
    GameApp().run()