scene.setBackgroundImage(assets.image`
    level
    `)
let yourconsole = sprites.create(assets.image`console`, SpriteKind.Player)
yourconsole.setPosition(9, 9)
let kullanicilar = sprites.create(assets.image`kullanıcılar`, SpriteKind.Player)
kullanicilar.setPosition(9, 29)
controller.A.onEvent(ControllerButtonEvent.Pressed, function a_tusu() {
    if (mouse.overlapsWith(yourconsole)) {
        game.splash("YAKINDA")
    } else if (mouse.overlapsWith(kullanicilar)) {
        game.splash("YAKINDA")
    }
    
})
let mouse = sprites.create(assets.image`imlec`, SpriteKind.Player)
controller.player1.moveSprite(mouse)
