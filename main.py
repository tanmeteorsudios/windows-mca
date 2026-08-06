scene.set_background_image(assets.image("""level_startup"""))

music.set_volume(100)
music.play(music.create_song(assets.song("""
        acılıs
        """)),
    music.PlaybackMode.UNTIL_DONE)

scene.set_background_image(assets.image("""level"""))
pause(1000)
game.splash("HOS GELDİNİZ")
game.splash("ADMİN")
pause(1000)

"""
**************windows kodu***************
"""

scene.set_background_image(assets.image("""
    level
    """))

yourconsole = sprites.create(assets.image("""
    console
    """), SpriteKind.player)
yourconsole.set_position(9, 9)

kullanicilar = sprites.create(assets.image("""
        kullanıcılar
        """),
    SpriteKind.player)
kullanicilar.set_position(9, 29)

off = sprites.create(assets.image("""off"""),
    SpriteKind.player)
off.set_position(9, 50)

def a_tusu():
    if mouse.overlaps_with(yourconsole):
        game.splash("WİNDOWS MAKECODEACARDE")
        game.splash("BY TANMETEORSUDİOS")
    elif mouse.overlaps_with(kullanicilar):
        game.splash("SU AN KULLANICI")
        game.splash("ADMİN")
    elif mouse.overlaps_with(off):
        game.splash("BAY BAY ADMİN")
        sprites.destroy(mouse)
        pause(1000)
        sprites.destroy(off)
        pause(1000)
        sprites.destroy(kullanicilar)
        pause(1000)
        sprites.destroy(yourconsole)
        pause(1000)        
        scene.set_background_image(assets.image("""level_startup"""))
        def on_forever():
            game.splash("KAPATMAK GÜVENLİ")
        forever(on_forever)
controller.A.on_event(ControllerButtonEvent.PRESSED, a_tusu)

mouse = sprites.create(assets.image("""
    imlec
    """), SpriteKind.player)
controller.player1.move_sprite(mouse)