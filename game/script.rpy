# The script of the game goes in this file.

label splashscreen:

    scene black

    pause 1.0

    $ renpy.movie_cutscene("video/intro (1).webm")

    scene black with dissolve

    pause 0.5

    return

label start:

    return


################################################################################
## Chapter 1
################################################################################

label chapter_1:

    play music "audio/backsound/Chapter 1/[Scene Suasana Desa].mp3" fadein 2.0
    scene bg_desa_siang with dissolve
    call screen chapter_title_screen(
        nomor    = "1",
        judul    = "Malam Mencekam",
        subjudul = "Siapkah kamu?"
    )
    jump chapter1_full


################################################################################
## Chapter 2
################################################################################

label chapter_2:

    play music "audio/backsound/Chapter 2/royaltyfreemusicstudio-mystic-fantasy-ambience-441255.mp3" fadein 2.0
    scene bg_ch2_nav_error with dissolve
    call screen chapter_title_screen(
        nomor    = "2",
        judul    = "Perburuan Fajar",
        subjudul = "Bahaya ada di setiap langkah"
    )
    jump chapter2_full


################################################################################
## Chapter 3
################################################################################

label chapter_3:

    play music "audio/backsound/Chapter 3/delosound-emotional-violin-strings-453280.mp3" fadein 2.0
    scene bg_panggung_dimensi_lain with fade
    call screen chapter_title_screen(
        nomor    = "3",
        judul    = "Jebakan di Balik Ketenangan",
        subjudul = "Waspada di balik ketenangan"
    )
    jump chapter3_full


################################################################################
## Chapter 4
################################################################################

label chapter_4:

    play music "audio/backsound/Chapter 4/game/audio/backsound/alexguz-the-wild-tribal-war_full_vocal_version-ethnic-east-african-386467.mp3" fadein 2.0
    scene bg_batu with dissolve
    call screen chapter_title_screen(
        nomor    = "4",
        judul    = "Pertempuran Jiwa",
        subjudul = "Satu pilihan, satu takdir"
    )
    jump chapter4_full
