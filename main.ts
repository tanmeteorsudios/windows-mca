scene.setBackgroundImage(assets.image`level_startup`)
music.setVolume(100)
music.play(music.createSong(assets.song`
        acılıs
        `), music.PlaybackMode.UntilDone)
scene.setBackgroundImage(assets.image`
    level
    `)
pause(1000)
game.splash("HOS GELDİNİZ")
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
controller.A.onEvent(ControllerButtonEvent.Pressed, function a_tusu() {
    if (mouse.overlapsWith(yourconsole)) {
        game.splash("WİNDOWS MAKECODEACARDE")
        game.splash("BY TANMETEORSUDİOS")
    } else if (mouse.overlapsWith(kullanicilar)) {
        game.splash("SU AN KULLANICI")
        game.splash("ADMİN")
    }
    
})
let mouse = sprites.create(assets.image`
    imlec
    `, SpriteKind.Player)
controller.player1.moveSprite(mouse)
