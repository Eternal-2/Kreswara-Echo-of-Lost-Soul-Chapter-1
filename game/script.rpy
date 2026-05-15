# The script of the game goes in this file.

# Declare characters used by this game.

# The game starts here.

# The script of the game goes in this file.

# The game starts here.

label start:
    # PENTING: label start harus langsung return agar Ren'Py
    # menampilkan main_menu dan Save/Load aktif saat masuk game.
    # chapter_select dipanggil dari tombol START di main_menu (screens.rpy).
    return


################################################################################
## Chapter 1
################################################################################

label chapter_1:

    scene bg_desa
    with fade

    play music "audio/lemonade-by-snoozybeats.mp3" fadein 1.0

    jump chapter1_full


################################################################################
## Chapter 2
################################################################################

label chapter_2:

    "Chapter 2 - Bayangan di Hutan"
    "Konten chapter 2 belum ditambahkan."

    return


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