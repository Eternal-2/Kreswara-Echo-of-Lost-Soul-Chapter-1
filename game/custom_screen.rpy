screen chapter_title_screen(nomor="1", judul="", subjudul=""):
    modal True

    # Overlay gelap semi-transparan di atas background
    add "#000000a0"

    # Garis dekorasi atas
    frame:
        xalign 0.5
        yalign 0.42
        xsize 700
        ysize 4
        background "#c8a96e"

    # Konten utama
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 18

        # Label chapter kecil
        text ("CHAPTER  " + nomor):
            xalign 0.5
            size 18
            color "#c8a96ecc"
            kerning 5.0
            bold True

        # Judul besar
        text judul:
            xalign 0.5
            size 52
            color "#f5ead8"
            bold True
            text_align 0.5

        # Sub-judul / tagline
        if subjudul != "":
            text ("\" " + subjudul + " \""):
                xalign 0.5
                size 22
                color "#aaaaaa"
                text_align 0.5
                italic True

    # Garis dekorasi bawah
    frame:
        xalign 0.5
        yalign 0.60
        xsize 700
        ysize 4
        background "#c8a96e"


    # Klik di mana saja untuk lanjut
    key "K_RETURN" action Return()
    key "K_SPACE"  action Return()
    imagebutton:
        idle Solid("#00000000")
        xfill True
        yfill True
        action Return()

screen timer_screen(length=50.0, on_timeout="waktu_habis_boss"):
    zorder 200
    modal False

    timer length action Jump(on_timeout)

    frame:
        xalign 0.5
        yalign 0.0
        yoffset 18
        xsize 680
        ysize 90
        background Frame("#0a0a0aee", 10, 10)
        left_padding 20
        right_padding 20
        top_padding 10
        bottom_padding 10

        vbox:
            xfill True
            spacing 6

            hbox:
                xfill True
                yalign 0.5

                hbox:
                    spacing 8
                    yalign 0.5
                    text "⏱":
                        size 22
                        yalign 0.5
                    text "WAKTU TERSISA":
                        size 14
                        color "#c8a96e"
                        kerning 2.0
                        yalign 0.5

                add DynamicDisplayable(countdown_text_color, length=length):
                    xalign 1.0
                    yalign 0.5

            frame:
                xfill True
                ysize 18
                background Frame("#1a1a2aee", 4, 4)
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0

                add DynamicDisplayable(countdown_bar, length=length):
                    xalign 0.0
                    yalign 0.5

screen radar_roh_screen(level=0):
    $ img_radar = "images/ASSET/RADAR ROH/radar roh #%s.png" % level
    add img_radar at efek_kedip_radar
        
    timer 2.0 action Hide("radar_roh_screen")

screen state_roh_screen(state="tenang"):
    $ img_state = "images/ASSET/STATE ROH/%s.png" % state
    add img_state at efek_kedip_state
        
    timer 2.0 action Hide("state_roh_screen")

screen panel_coding(border="border1", show_error=False):
    if show_error:
        add "images/ASSET/PANEL CODING/border_error.png" xalign 0.5 yalign 0.5 zoom 0.6
    else:
        add "images/ASSET/PANEL CODING/[border].png" xalign 0.5 yalign 0.5 zoom 0.6
    imagebutton:
        idle "images/ASSET/PANEL CODING/button_run.png"
        hover "images/ASSET/PANEL CODING/button_run.png"
        at transform:
            zoom 0.35
            xalign 0.72 
            yalign 0.78
        action Return(True)

screen feedback_screen(result="berhasil"):
    add "images/ASSET/FEEDBACK VISUAL/[result].png" xalign 0.5 yalign 0.5 zoom 0.55
    timer 1.5 action Hide("feedback_screen")

transform kalah_fadein:
    alpha 0.0 yoffset 40
    linear 0.6 alpha 1.0 yoffset 0

transform kalah_title_in:
    alpha 0.0 yoffset -20
    linear 0.5 alpha 1.0 yoffset 0

screen kalah_boss_screen():

    vbox:
        xalign 0.5 yalign 0.45 spacing 50
        at kalah_title_in

        text "Kamu Kalah..." size 52 color "#ff4444" xalign 0.5

        hbox:
            xalign 0.5 spacing 60
            imagebutton:
                idle  "images/ASSET/KALAH BOSS MENU/button_restart.png"
                hover "images/ASSET/KALAH BOSS MENU/button_restart.png"
                at transform:
                    zoom 0.5
                action Return("restart")
            imagebutton:
                idle  "images/ASSET/KALAH BOSS MENU/button_kembali ke menu.png"
                hover "images/ASSET/KALAH BOSS MENU/button_kembali ke menu.png"
                at transform:
                    zoom 0.5
                action Return("menu")

screen soal_panel(nomor="1", tema="", kode="", pertanyaan=""):
    add "#000000bb"

    frame:
        xalign 0.5
        yalign 0.0
        yoffset 140
        xsize 980
        ysize 310
        xpadding 40
        ypadding 18
        background Frame("#0e1016f0", 14, 14)

        vbox:
            spacing 14
            xfill True

            hbox:
                xfill True
                yalign 0.5
                hbox:
                    spacing 10
                    yalign 0.5
                    text "⚔":
                        size 14
                        color "#c8a96e"
                        yalign 0.5
                    text "SERANGAN DATA":
                        size 12
                        color "#c8a96e"
                        kerning 3.0
                        yalign 0.5
                text "#[nomor]":
                    xalign 1.0
                    size 13
                    color "#c8a96e88"
                    bold True

            text "[tema]":
                size 24
                color "#f5ead8"
                bold True

            frame:
                background "#c8a96e66"
                xfill True
                ysize 1

            if kode != "":
                frame:
                    background "#0a0d12"
                    xfill True
                    left_padding  20
                    right_padding 20
                    top_padding   14
                    bottom_padding 14

                    frame:
                        background Transform(Solid("#2d6a9f"), xsize=3)
                        left_padding 15
                        
                        text "[kode]":
                            size 17
                            color "#79c0ff"
                            font "gui/font/SourceCodePro-Regular.ttf"
                            line_spacing 10

            text "[pertanyaan]":
                size 18
                color "#ddd8cc"
                xalign 0.5
                text_align 0.5
                line_spacing 6

screen dialog_choice_hint(mode="cari"):
    if mode == "cari":
        add "images/ASSET/DIALOG CHOICE/cari informasi.png" xalign 0.85 yalign 0.85 zoom 0.28
    else:
        add "images/ASSET/DIALOG CHOICE/serap roh.png"      xalign 0.85 yalign 0.85 zoom 0.28

screen pilihan_ending_screen():
    modal True

    add "#000000dd"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        text "Kreswara berdiri di persimpangan terakhir.":
            xalign 0.5
            size 22
            color "#ddd8cc"
            text_align 0.5
            italic True

        text "Apa yang akan ia pilih?":
            xalign 0.5
            size 18
            color "#aaaaaa"
            text_align 0.5

        null height 20

        ## Pilihan Bad Ending — Tetap tinggal
        frame:
            xalign 0.5
            xsize 620
            ysize 100
            background Frame("#1a0a0aee", 8, 8)
            hover_background Frame("#3d0000ee", 8, 8)
            xpadding 30
            ypadding 20

            button:
                xfill True
                yfill True
                action Return("bad")

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6

                    text "Tetap tinggal di dunia ini":
                        xalign 0.5
                        size 22
                        color "#ff6b6b"
                        bold True
                        text_align 0.5

                    text "Biarkan semua ini berlanjut selamanya...":
                        xalign 0.5
                        size 14
                        color "#aa5555"
                        text_align 0.5

        ## Pilihan Good Ending — Keluar ke dunia nyata
        frame:
            xalign 0.5
            xsize 620
            ysize 100
            background Frame("#0a1a0aee", 8, 8)
            hover_background Frame("#003d00ee", 8, 8)
            xpadding 30
            ypadding 20

            button:
                xfill True
                yfill True
                action Return("good")

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6

                    text "Keluar menghadapi dunia nyata":
                        xalign 0.5
                        size 22
                        color "#6bffb8"
                        bold True
                        text_align 0.5

                    text "Kembali kepada mereka yang menunggu...":
                        xalign 0.5
                        size 14
                        color "#55aa88"
                        text_align 0.5
