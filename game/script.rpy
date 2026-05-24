# The script of the game goes in this file.

# Declare characters used by this game.

# The game starts here.

# The script of the game goes in this file.

# The game starts here.
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

    scene bg_desa
    with fade

    jump chapter1_full


################################################################################
## Chapter 2
################################################################################

label chapter_2:

    "Chapter 2 - Bayangan di Hutan"
    "Konten chapter 2 belum ditambahkan."

    jump chapter2_full


################################################################################
## Chapter 3
################################################################################

label chapter_3:

    "Chapter 3 - Rahasia Kuil"
    "Konten chapter 3 belum ditambahkan."

    return


################################################################################
## Chapter 4
################################################################################

label chapter_4:

    "Chapter 4 - Pertempuran Jiwa"
    "Konten chapter 4 belum ditambahkan."

    return