scene.set_background_image(assets.image("""
    level
    """))

yourconsole = sprites.create(assets.image("""console"""), SpriteKind.player)
yourconsole.set_position(9, 9)

kullanicilar = sprites.create(assets.image("""kullanıcılar"""), SpriteKind.player)
kullanicilar.set_position(9, 29)

def a_tusu():
    if mouse.overlaps_with(yourconsole):
        game.splash("YAKINDA")

    elif mouse.overlaps_with(kullanicilar):
        game.splash("YAKINDA")


controller.A.on_event(ControllerButtonEvent.PRESSED, a_tusu)

mouse = sprites.create(assets.image("""imlec"""), SpriteKind.player)
controller.player1.move_sprite(mouse)
