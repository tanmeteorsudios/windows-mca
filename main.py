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
off.set_position(9, 90)

youtube = sprites.create(assets.image("""youtube"""),
    SpriteKind.player)
youtube.set_position(9, 50)

steam = sprites.create(assets.image("""steam"""),
    SpriteKind.player)
steam.set_position(9, 70)

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
        sprites.destroy(steam)
        pause(1000)
        sprites.destroy(youtube)
        pause(1000)        
        sprites.destroy(kullanicilar)
        pause(1000)
        sprites.destroy(yourconsole)
        pause(1000)        
        scene.set_background_image(assets.image("""level_startup"""))
        def on_forever():
            game.splash("KAPATMAK GÜVENLİ")
        forever(on_forever)
    elif mouse.overlaps_with(youtube):
        game.splash("RIDVAN KERVEK")
        game.splash("GEÇMİŞTEKİ FİYATLAR GÜNÜMÜZDE OLSA(MCA)")
        game.splash("-")
        game.splash("RIDVAN:(YERDE KOLYE BULUR)")
        game.splash("RIDVAN:BU NE YA")
        game.splash("RIDVAN:(KOLYEYİ ALIR VE BAKKALA GİDER)")
        game.splash("RIDVAN:KOLAY GELSİN SİGARA NE KADAR")
        game.splash("BAKKALCI:100 LİRA")
        game.splash("RIDVAN:(KOLYE YE DOKUNUR)")
        game.splash("RIDVAN:ESKİDEN 50 LİRAYA BAKKALDAN BİRSÜRÜ ŞEY ALIRDIK")
        game.splash("BAKKALCI:SENİN KAÇ LİRAN VAR")
        game.splash("RIDVAN:75")
        game.splash("BAKKALCI:O PARAYA 75 TANE SIGARA ALIRSIN")
        game.splash("RIDVAN:DAYI SİGARA 100 LİRA DEDİN NASIL 75 TL YE 75 TANE SİGARA ALAYIM DAHA 1 SİGARA BİLE ALAMIYORUM")
        game.splash("BAKKALCI:SİGARA 1 LİRA")
        game.splash("RIDVAN:(İÇİNDEN:DELİ HERHALDE)")
        game.splash("RIDVAN:SEN AL BU PARAYI BANA 75 TANE SİGARA VER")
        game.splash("RIDVAN:(75 TL VERİR)")
        game.splash("VE SON")
    elif mouse.overlaps_with(steam):
        game.splash("GİT GERÇEĞİNDEN OYUN OYNA")
controller.A.on_event(ControllerButtonEvent.PRESSED, a_tusu)

mouse = sprites.create(assets.image("""
    imlec
    """), SpriteKind.player)
controller.player1.move_sprite(mouse)