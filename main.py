@namespace
class SpriteKind:
    yourconsole = SpriteKind.create()
    yc = SpriteKind.create()
scene.set_background_image(assets.image("""
    level
    """))

yourconsole1 = sprites.create(assets.image("""
    console
    """), SpriteKind.yc)
yourconsole1.set_position(9, 9)

mause = sprites.create(assets.image("""
    imlec
    """), SpriteKind.player)
controller.player1.move_sprite(mause)