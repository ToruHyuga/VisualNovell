# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
init:
    image bg road = "images/LvKiq04m308.jpg"
    image bg white = "images/white-bg.jpg"
    image logo = "images/logo.png"
    $ narrator = Character(None, kind=nvl)

    $ flash = Fade(.75, 0, .5, color="#fff")
    # Declare characters used by this game.
    define belphegor = Character('Бельфегор', color="#9b2d30")
    define belphegorEmpty = Character(color="#9b2d30")
    image movie = Movie(size=(config.screen_width, config.screen_height))

# The game starts here.
label start:
    scene black
    with Pause(1)

    play movie "videos/final1.ogv" loop
    show movie with dissolve
    
    belphegorEmpty "Души"
    belphegorEmpty "..."   
    belphegorEmpty "Души"
    belphegorEmpty "..."
    belphegorEmpty "Грешные души, протекающие мимо меня, походили на бурлящий поток."
    belphegorEmpty "Все они кричат, стонут, и плачут"
    belphegorEmpty "Но кто заставлял их так поступать? Это был их выбор - так прожить жизнь"
    belphegorEmpty "И для меня это радость"
    belphegorEmpty "Наблюдать за ними, за тем, как они корчатся от боли за свои деяния при жизни..."
    belphegorEmpty "Деяния"
    belphegorEmpty "..."
    belphegorEmpty "Интересно, меня охватило любопытство"
    belphegorEmpty "Все их грехи отображаются на них, и все они описываются в наших книгах"
    belphegorEmpty "Но как все происходит?"
    belphegorEmpty "Я никогда не наблюдал за этим, я всегда видел только последствия"
    belphegorEmpty "Хочу"
    belphegorEmpty "Хочу увидеть"
    belphegorEmpty "Любопытство пожирает меня изнутри"
    belphegorEmpty "Решено"
    belphegorEmpty "Я отправлюсь наверх..."
    belphegorEmpty"...к людям"
    belphegorEmpty "Низшие демоны и без меня справятся с работой"
    belphegorEmpty "Я Высший! Мне все дозволено!"
    belphegor "Я - Бельфегор!"

    hide movie
    stop movie
    
    scene bg white
    with flash
    
    show logo at truecenter with dissolve
    $ renpy.pause(1.5)
    hide logo with dissolve
    
    scene bg road
    with flash
    narrator "Вокруг стоял невообразимый шум."
    narrator "Люди сновали по улице, каждый следуя по своим делам. "
    narrator "Неожиданно какой-то парень столкнулся с появившимся из неоткуда человеком. "
    narrator "Извинившись, он пошел дальше по своим делам, так и не поняв откуда взялся тот парень."
    return
