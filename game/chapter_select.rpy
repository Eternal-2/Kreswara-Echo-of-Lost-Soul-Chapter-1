default persistent.chapter2_unlocked = False
default persistent.chapter3_unlocked = False
default persistent.chapter4_unlocked = False

init python:
    def get_chapters():
        return [
            {
                "number"  : 1,
                "title"   : "Awal Mula",
                "subtitle": "...",
                "label"   : "chapter1_full",
                "locked"  : False,
            },
            {
                "number"  : 2,
                "title"   : "...",
                "subtitle": "...",
                "label"   : "chapter_2",
                "locked"  : not persistent.chapter2_unlocked,
            },
            {
                "number"  : 3,
                "title"   : "...",
                "subtitle": "...",
                "label"   : "chapter_3",
                "locked"  : not persistent.chapter3_unlocked,
            },
            {
                "number"  : 4,
                "title"   : "...",
                "subtitle": "...",
                "label"   : "chapter_4",
                "locked"  : not persistent.chapter4_unlocked,
            },
        ]

screen chapter_select():
    tag menu

    ## Background
    add gui.main_menu_background
    add "#000000bb"

    ## Judul
    vbox:
        xalign 0.5
        ypos   45
        spacing 10

        text "PILIH CHAPTER":
            xalign 0.5
            size   40
            color  "#c8a96e"

        frame:
            background "#c8a96e"
            xalign 0.5
            xsize  360
            ysize  2

    textbutton "KEMBALI":
        xalign 0.05
        yalign 0.95
        text_size 30
        text_color "#c8a96e"
        text_hover_color "#ffffff"
        action ShowMenu("main_menu")


    vpgrid:
        cols       2
        xalign     0.5
        yalign     0.55
        xsize      1060
        ysize      500
        spacing    28
        mousewheel True

        for ch in get_chapters():
            $ _locked = ch["locked"]

            if not _locked:
                button:
                    action Jump(ch["label"])
                    xsize   510
                    ysize   240
                    background "#161616ee"
                    hover_background "#222222ee"

                    frame:
                        background "#c8a96e"
                        xpos  0
                        ypos  0
                        xsize 4
                        yfill True

                    vbox:
                        xpos    24
                        ypos    20
                        xsize   460
                        spacing 8

                        text "CHAPTER [ch['number']]":
                            size    12
                            color   "#c8a96e"
                            kerning 3.0

                        text "[ch['title']]":
                            size  30
                            color "#f0e6d0"

                        frame:
                            background "#c8a96e55"
                            xsize 180
                            ysize 1

                        text "[ch['subtitle']]":
                            size       16
                            color      "#999999"

                        text "▶  Klik untuk mulai":
                            size       14
                            color      "#c8a96e99"

            else:
                frame:
                    xsize   510
                    ysize   240
                    background "#0d0d0dee"

                    frame:
                        background "#2a2a2a"
                        xpos  0
                        ypos  0
                        xsize 4
                        yfill True

                    vbox:
                        xpos    24
                        ypos    20
                        xsize   460
                        spacing 8

                        text "CHAPTER [ch['number']]":
                            size    12
                            color   "#3a3a3a"
                            kerning 3.0

                        text "[ch['title']]":
                            size  30
                            color "#333333"

                        frame:
                            background "#2a2a2a"
                            xsize 180
                            ysize 1

                        text "[ch['subtitle']]":
                            size       16
                            color      "#2a2a2a"

                        hbox:
                            spacing    8

                            text "🔒":
                                size  16
                                color "#444444"

                            text "Terkunci":
                                size  14
                                color "#444444"

style chapter_select_frame is frame:
    padding (0, 0)
