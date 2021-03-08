# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# IF U SEE THIS GET OFF THIS FILE IMMEDIATELY, YOU DO NOT BELONG HERE
# Hello there, I'll leave a hint about who i man ;)
#wot do u mean 'who i man'?
# shoudnt it be who i am?
import arcade 
WIDTH = 500
HEIGHT = 500
TITLE = "MY GAME"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5

class Game(arcade.Window):
  def __init__(self):
    super().__init__(WIDTH, HEIGHT, TITLE)
    arcade.set_background_color(arcade.csscolor.AQUAMARINE)
    self.coin_list = None
    self.wall_list = None
    self.player_list = None
    self.player_sprite = None

  def setup(self):
    self.player_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList(use_spatial_hash=True)
    self.coin_list = arcade.SpriteList(use_spatial_hash=True)
    image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    self.player_sprite.center_x = 64
    self.player_sprite.center_y = 128
    self.player_list.append(self.player_sprite)
    for x in range(0, 1250, 64):
        wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
        wall.center_x = x
        wall.center_y = 32
        self.wall_list.append(wall)
    coordinate_list = [[512, 96],
                        [256, 96],
                        [768, 96]]
    for coordinate in coordinate_list:
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
        wall.position = coordinate
        self.wall_list.append(wall)

  def on_draw(self):
    arcade.start_render()
    self.wall_list.draw()
    self.coin_list.draw()
    self.player_list.draw()

  def on_key_press(self, key, modifiers):
    if key == arcade.key.UP or key == arcade.key.W:
        self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.DOWN or key == arcade.key.S:
        self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.LEFT or key == arcade.key.A:
        self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
    elif key == arcade.key.RIGHT or key == arcade.key.D:
        self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

  def on_key_release(self, key, modifiers):
    if key == arcade.key.UP or key == arcade.key.W:
        self.player_sprite.change_y = 0
    elif key == arcade.key.DOWN or key == arcade.key.S:
        self.player_sprite.change_y = 0
    elif key == arcade.key.LEFT or key == arcade.key.A:
        self.player_sprite.change_x = 0
    elif key == arcade.key.RIGHT or key == arcade.key.D:
        self.player_sprite.change_x = 0
    
  #def on_update(self, delta_time):
  #  self.physics_engine.update()
      
def main():
    window = Game()
    window.setup()
    arcade.run()

main()