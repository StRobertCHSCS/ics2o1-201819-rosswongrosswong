import arcade


WIDTH = 640
HEIGHT = 680

def what_is_ergonomics():

    arcade.draw_text("What is ergonomics?", 30, 650, arcade.color.BLACK, 14)
    arcade.draw_text("Ergonomics is the optimization of products for us to comforatably use.", 30, 625, arcade.color.BLACK, 12)

    arcade.draw_text("What can ergonomics prevent?", 30, 550, arcade.color.BLACK, 14)
    arcade.draw_text("-Carpal tunnel", 30, 525, arcade.color.BLACK, 12)
    arcade.draw_text("-Tendinitis", 30, 500, arcade.color.BLACK, 12)
    arcade.draw_text("-Tennis elbow", 30, 475, arcade.color.BLACK, 12)
    arcade.draw_text("-Ganglion cysts", 30, 450, arcade.color.BLACK, 12)
    arcade.draw_text("-DeQuervain's Disease", 30, 425, arcade.color.BLACK, 12)
    arcade.draw_text("...and more, unfortunately.", 30, 400, arcade.color.BLACK, 12)

    meme = arcade.load_texture("ergonomics_meme.jpg", mirrored=False, scale=0.5)
    arcade.draw_xywh_rectangle_textured(25, 100, 250, 250, meme)

    meme = arcade.load_texture("good_ergonomics.png", mirrored=False, scale=0.5)
    arcade.draw_xywh_rectangle_textured(25, 100, 250, 250, meme)

def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...

    arcade.draw_circle_filled(25, 25, 65, arcade.color.RED)
    what_is_ergonomics()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Computers and Society Poster")
    arcade.set_background_color(arcade.color.PASTEL_ORANGE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
