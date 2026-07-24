scene.set_background_image(assets.image("""
    level
    """))

yourconsole = sprites.create(assets.image("""console"""), SpriteKind.player)
yourconsole.set_position(9, 9)

def a_tusu():
    if mause.overlaps_with(yourconsole): 
        game.splash("YAKINDA")
controller.A.on_event(ControllerButtonEvent.PRESSED, a_tusu)

mause = sprites.create(assets.image("""
    imlec
    """), SpriteKind.player)
controller.player1.move_sprite(mause)
