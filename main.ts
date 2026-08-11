scene.setBackgroundImage(assets.image`level_startup`)
music.setVolume(100)
music.play(music.createSong(assets.song`
        acılıs
        `), music.PlaybackMode.UntilDone)
scene.setBackgroundImage(assets.image`level`)
pause(1000)
game.splash("HOS GELDİNİZ")
game.splash("ADMİN")
pause(1000)
/** **************windows kodu*************** */
scene.setBackgroundImage(assets.image`
    level
    `)
let yourconsole = sprites.create(assets.image`
    console
    `, SpriteKind.Player)
yourconsole.setPosition(9, 9)
let kullanicilar = sprites.create(assets.image`
        kullanıcılar
        `, SpriteKind.Player)
kullanicilar.setPosition(9, 29)
let off = sprites.create(assets.image`off`, SpriteKind.Player)
off.setPosition(9, 90)
let youtube = sprites.create(assets.image`youtube`, SpriteKind.Player)
youtube.setPosition(9, 50)
let steam = sprites.create(assets.image`steam`, SpriteKind.Player)
steam.setPosition(9, 70)
controller.A.onEvent(ControllerButtonEvent.Pressed, function a_tusu() {
    if (mouse.overlapsWith(yourconsole)) {
        game.splash("WİNDOWS MAKECODEACARDE")
        game.splash("BY TANMETEORSUDİOS")
    } else if (mouse.overlapsWith(kullanicilar)) {
        game.splash("SU AN KULLANICI")
        game.splash("ADMİN")
    } else if (mouse.overlapsWith(off)) {
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
        scene.setBackgroundImage(assets.image`level_startup`)
        forever(function on_forever() {
            game.splash("KAPATMAK GÜVENLİ")
        })
    } else if (mouse.overlapsWith(youtube)) {
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
    } else if (mouse.overlapsWith(steam)) {
        game.splash("GİT GERÇEĞİNDEN OYUN OYNA")
    }
    
})
let mouse = sprites.create(assets.image`
    imlec
    `, SpriteKind.Player)
controller.player1.moveSprite(mouse)
