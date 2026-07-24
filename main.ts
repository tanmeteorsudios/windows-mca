scene.setBackgroundImage(assets.image`
    level
    `)
let yourconsole = sprites.create(assets.image`console`, SpriteKind.Player)
yourconsole.setPosition(9, 9)
controller.A.onEvent(ControllerButtonEvent.Pressed, function a_tusu() {
    if (mause.overlapsWith(yourconsole)) {
        game.splash("YAKINDA")
    }
    
})
let mause = sprites.create(assets.image`
    imlec
    `, SpriteKind.Player)
controller.player1.moveSprite(mause)
