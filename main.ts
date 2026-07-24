namespace SpriteKind {
    export const yourconsole = SpriteKind.create()
    export const yc = SpriteKind.create()
}

scene.setBackgroundImage(assets.image`
    level
    `)
let yourconsole1 = sprites.create(assets.image`
    console
    `, SpriteKind.yc)
yourconsole1.setPosition(9, 9)
let mause = sprites.create(assets.image`
    imlec
    `, SpriteKind.Player)
controller.player1.moveSprite(mause)
