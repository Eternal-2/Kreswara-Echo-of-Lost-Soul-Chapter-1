screen soal_panel(nomor="1", tema="", kode="", pertanyaan=""):
    add "#000000aa"

    frame:
        xalign 0.5
        yalign 0.3
        xsize 820
        xpadding 36
        ypadding 30
        background Frame("#111318ee", 12, 12)

        vbox:
            spacing 20
            xfill True

            vbox:
                spacing 6
                xfill True

                hbox:
                    spacing 10
                    xfill True
                    text "⚔ SERANGAN DATA":
                        size 12
                        color "#c8a96e"
                        kerning 3.0
                        yalign 0.5
                    text "#[nomor]":
                        size 12
                        color "#c8a96e"
                        bold True
                        yalign 0.5

                text "[tema]":
                    size 22
                    color "#f5ead8"
                    bold True

                frame:
                    background "#c8a96e55"
                    xfill True
                    ysize 1

            if kode != "":
                frame:
                    background "#0d1117"
                    xfill True
                    xpadding 18
                    ypadding 14
                    left_margin 0
                    text "[kode]":
                        size 18
                        color "#79c0ff"
                        font "gui/font/SourceCodePro-Regular.ttf"
                        line_spacing 8

            text "[pertanyaan]":
                size 19
                color "#e0e0e0"
                xalign 0.5
                text_align 0.5
                line_spacing 4



define k  = Character("Kreswara",      color="#5ds8ff")
define a  = Character("AS-LEEN",       color="#c3b1e1")
define i  = Character("Ibu Kreswara",  color="#f5c8a0")
define b  = Character("Bapak Kreswara",color="#e07050")
define d  = Character("Damar",         color="#80d4a0")
define nr = Character(None, what_style="centered_text")
define ds = Character("Dursasana",    color="#ff3333")



image k_normal:
    im.Scale("images/kreswara/kreswara_normal.png", 750, 1500)
image k_smile:
    im.Scale("images/kreswara/kreswara_smile.png", 750, 1500)
image k_talk:
    im.Scale("images/kreswara/kreswara_talk.png", 750, 1500)
image k_angry:
    im.Scale("images/kreswara/kreswara_angry.png", 750, 1500)
image k_angrytalk:
    im.Scale("images/kreswara/kreswara_angrytalk.png", 750, 1500)
image k_think:
    im.Scale("images/kreswara/kreswara_thinking.png", 750, 1500)

image a_normal:
    im.Scale("images/asleen/asleen_normal.png", 850, 1600)
image a_talk:
    im.Scale("images/asleen/asleen_talk.png", 850, 1600)

image ibu_k:
    im.Scale("images/NPC/NPC_Kreswara Mother.png", 750, 1500)
image bpk_k:
    im.Scale("images/NPC/NPC_Kreswara Father.png", 850, 1700)
image damar:
    im.Scale("images/NPC/NPC_Damar.png", 850, 1900)

image ds_normal:
    im.Scale("images/BOSS/Dursasana/dursasana_normal.png", 750, 1600)
image ds_talk:
    im.Scale("images/BOSS/Dursasana/dursasana_talk.png", 750, 1600)


image bg_rumah_siang       = im.Scale("images/BG/rumah kreswara ketika siang hari.png", 1920, 1080)    
image bg_rumah_malam       = im.Scale("images/BG/rumah kreswara malam.png", 1920, 1080)        
image bg_starry     = "images/BG/bg starrysky.png"   
image bg_n2         = "images/BG/bg n2.png"        

image effect_1 = Movie(play="images/EFFECT/1.webm", loop=True, size=(1920, 3413))
image effect_2 = Movie(play="images/EFFECT/2.webm", loop=True, size=(1920, 3413))
image effect_3 = Movie(play="images/EFFECT/3.webm", loop=True, size=(1920, 3413))
image effect_4 = Movie(play="images/EFFECT/4.webm", loop=True, size=(1920, 3413))
image effect_5 = Movie(play="images/EFFECT/5.webm", loop=True, size=(1920, 3413))
image effect_6 = Movie(play="images/EFFECT/6.webm", loop=True, size=(1920, 3413))
image effect_7 = Movie(play="images/EFFECT/7.webm", loop=True, size=(1920, 3413))
image effect_8 = Movie(play="images/EFFECT/8.webm", loop=True, size=(1920, 3413))
image effect_9 = Movie(play="images/EFFECT/9.webm", loop=True, size=(1920, 3413))


label chapter2_full:

    scene bg_rumah_malam with dissolve
    
    centered "Setelah mengalahkan buta cakil, wara harus mencari lawan selanjutnya."
    centered "Dia pun sudah siap bergerak menuju arah yang diberikan oleh as-leen."
    centered "namun baru beberapa langkah berjalan. tiba tiba as-leen mengeluarkan suara aneh."

    play sound "audio/sfx/chapter 1/1.suara jangkrik.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "a-ada apa as-leen?......... Apa kamu baik baik saja?"
    hide k_talk

    stop sound

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "aku baik baik saja…..hanya aja navigasiku bermasalah."
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "baiklah….. kamu cukup memperhatikan saja, biar aku yang urus"
    hide k_talk
    
    centered "Wara pun mencari boss dengan mengitari desa, untuk mencari boss nya. selama perjalanan ia harus melewati semua tantangan yang ia lewati."
    centered "setelah menempuh perjalanan yang jauh. sampailah ia di sebuah tempat reruntuhan labirin."
    centered "empat yang terlihat megah namun tertutup dengan retakan retakan yang membuat keindahan nya tertutup."
    centered "di dalam nya penuh dengan bangku sekolah yang melayang dan tidak satupun yang menyentuh lantai."

    scene bg_rumah_malam with fade

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(bingung)"
    hide k_think

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "tempat apa ini?......."
    hide k_talk

    centered "wara berjalan perlahan memasuki labirin itu, ia melihat sekitar dan menganalisis apa yang akan dia lawan pada kali ini. terlintas di pikiran nya, ia mengingat sekolah yang dulu mengajarkan nya koding."

    