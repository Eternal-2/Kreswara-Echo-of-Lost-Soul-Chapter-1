define k  = Character("Kreswara",      color="#5bc8ff")
define a  = Character("AS-LEEN",       color="#c3b1e1")
define i  = Character("Ibu Kreswara",  color="#f5c8a0")
define b  = Character("Bapak Kreswara",color="#e07050")
define d  = Character("Damar",         color="#80d4a0")
define nr = Character(None, what_style="centered_text")
define bc = Character("Buta Cakil",    color="#ff3333")
define sk = Character("Sengkuni",  color="#9933ff")


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
image a_siluet:
    im.Scale("images/asleen/siluet_asleen.png", 850, 1600)
image a_smile:
    im.Scale("images/asleen/asleen_smile.png", 850, 1600)
image a_poisoned:
    im.Scale("images/asleen/asleen_poisoned.png", 850, 1600)
image a_poisoned_talk:
    im.Scale("images/asleen/asleen_poisoned_talk.png", 850, 1600)
image a_poisoned_smile:
    im.Scale("images/asleen/kena_poisoned_smile.png", 850, 1600)

image ibu_k:
    im.Scale("images/NPC/NPC_Kreswara Mother.png", 750, 1500)
image bpk_k:
    im.Scale("images/NPC/NPC_Kreswara Father.png", 850, 1700)
image damar:
    im.Scale("images/NPC/NPC_Damar.png", 850, 1900)

image bc_normal:
    im.Scale("images/BOSS/Buta cakil/butacakil_normal.png", 750, 1600)
image bc_talk:
    im.Scale("images/BOSS/Buta cakil/butacakil_talk.png", 750, 1600)

image sk_normal:
    im.Scale("images/BOSS/Sengkuni/Sengkuni_normal.png", 750, 1600)
image sk_talk:
    im.Scale("images/BOSS/Sengkuni/Sengkuni_talk.png", 750, 1600)

# Background Chapter 1
image bg_desa_siang       = im.Scale("images/BG/BG chapter 1/rumah kreswara ketika siang hari.png", 1920, 1080)    
image bg_desa_malam       = im.Scale("images/BG/BG chapter 1/rumah kreswara malam.png", 1920, 1080)        
image bg_ruangan_siang    = im.Scale("images/BG/BG chapter 1/DALAM RUMAH KRESWARA  (SIANG).png", 1920, 1080) 
image bg_ruangan_malam    = im.Scale("images/BG/BG chapter 1/DALAM RUMAH KRESWARA (MALAM).png", 1920, 1080)
image bg_cod              = im.Scale("images/BG/BG chapter 1/Kreswara menuju pulang ke rumah .png", 1920, 1080)
image bg_nyimping         = im.Scale("images/BG/BG chapter 1/Kreswara Nyimping Wayang.png", 1920, 1080)     
image bg_panggung         = im.Scale("images/BG/BG chapter 1/panggung wayang .png", 1920, 1080) 
image bg_panggung_khusus  = im.Scale("images/BG/BG chapter 1/Wara melihat Bapaknya Jadi dalang.png", 1920, 1080)
image bg_rakit_pupils     = im.Scale("images/BG/BG chapter 1/Kreswara Rakit Pupils.png", 1920, 1080)
image bg_perpus           = im.Scale("images/BG/BG chapter 1/perpustakaan desa malam hari.png", 1920, 1080)
image bg_masuk_pupils     = im.Scale("images/BG/BG chapter 1/KRESWARA BERADA DI PERPUSTAKAAN MENGGUNAKAN PUPILS(1).png", 1920, 1080)
image bg_dunia_lain       = im.Scale("images/BG/BG chapter 1/desa digital + anomali .png", 1920, 1080)
image bg_versus           = im.Scale("images/BG/BG chapter 1/KRESWARA LAWAN BUTA CAKIL.png", 1920, 1080)
image bg_menang           = im.Scale("images/BG/BG chapter 1/KRESWARA MENGALAHKAN BUTA CAKIL.png", 1920, 1080)


# Background Chapter 3
image bg_desa_retak        = im.Scale("images/BG/BG Chapter 3/desa digital + anomaly dengan retakan nuansa biru di langit .png", 1920, 1080)
image bg_dimensi_lain      = im.Scale("images/BG/BG Chapter 3/panggung wayang + dimensi lain .png", 1920, 1080)
image bg_black_and_white   = im.Scale("images/BG/BG Chapter 3/bakcground utama _pembuka.png", 1920, 1080)
image bg_c3_roh_kamboja    = im.Scale("images/BG/BG Chapter 3/kreswara berada di ruangan buntu dan melihat beberapa roh data kecil dengan lantai bunga kamboja .png", 1920, 1080)
image bg_c3_lorong_pintu   = im.Scale("images/BG/BG Chapter 3/kreswara dan as-leen berjalan menyusuri lorong hingga diujung bertemu pintu besar yang sudah terbuka lebar.png", 1920, 1080)
image bg_c3_jarum_retak    = im.Scale("images/BG/BG Chapter 3/setelah masuk dinding ruangan tibatiba retak ribuan jarum melesat seperti hujan pecahan kaca.png", 1920, 1080)
image bg_c3_asleen_racun   = im.Scale("images/BG/BG Chapter 3/As-leen terkena racun setelah menahan jarum yang akan mengenai kreswara.png", 1920, 1080)
image bg_c3_bertemu_sengkuni = im.Scale("images/BG/BG Chapter 3/kreswara bertemu sengkuni.png", 1920, 1080)
image bg_c3_sengkuni_hantam  = im.Scale("images/BG/BG Chapter 3/sengkuni menghantam kreswara.png", 1920, 1080)
image bg_c3_wara_serang    = im.Scale("images/BG/BG Chapter 3/kreswara menyerang sengkuni.png", 1920, 1080)
image bg_c3_sengkuni_kalah = im.Scale("images/BG/BG Chapter 3/kreswara mengalahkan Sengkuni.png", 1920, 1080)
image bg_c3_gendong        = im.Scale("images/BG/BG Chapter 3/kreswara menggendong as-leen setelah terkena racun .png", 1920, 1080)
image bg_c3_pintu_tutup_1  = im.Scale("images/BG/BG Chapter 3/pintu besar mulai tertutup sendiri yang menandakan wara dan as-leen sudah terjebak.png", 1920, 1080)
image bg_c3_pintu_tutup_2  = im.Scale("images/BG/BG Chapter 3/pintu besar mulai tertutup sendiri yang menandakan wara dan as-leen sudah terjebak  (1).png", 1920, 1080)
image bg_c3_topang_asleen  = im.Scale("images/BG/BG Chapter 3/Kreswara menopang tubuh As-leen sambil menatapnya.png", 1920, 1080)


image effect_1 = Movie(play="images/EFFECT/1.webm", loop=True, size=(1920, 3413))
image effect_2 = Movie(play="images/EFFECT/2.webm", loop=True, size=(1920, 3413))
image effect_3 = Movie(play="images/EFFECT/3.webm", loop=True, size=(1920, 3413))
image effect_4 = Movie(play="images/EFFECT/4.webm", loop=True, size=(1920, 3413))
image effect_5 = Movie(play="images/EFFECT/5.webm", loop=True, size=(1920, 3413))
image effect_6 = Movie(play="images/EFFECT/6.webm", loop=True, size=(1920, 3413))
image effect_7 = Movie(play="images/EFFECT/7.webm", loop=True, size=(1920, 3413))
image effect_8 = Movie(play="images/EFFECT/8.webm", loop=True, size=(1920, 3413))
image effect_9 = Movie(play="images/EFFECT/9.webm", loop=True, size=(1920, 3413))
image effect_10 = Movie(play="images/EFFECT/10.webm", loop=True, size=(1920, 2030))