define k  = Character("Kreswara",      color="#5bc8ff")
define a  = Character("AS-LEEN",       color="#c3b1e1")
define i  = Character("Ibu Kreswara",  color="#f5c8a0")
define b  = Character("Bapak Kreswara",color="#e07050")
define d  = Character("Damar",         color="#80d4a0")
define nr = Character(None, what_style="centered_text")
define bc = Character("Buta Cakil",    color="#ff3333")



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

image bc_normal:
    im.Scale("images/BOSS/Buta cakil/butacakil_normal.png", 750, 1600)
image bc_talk:
    im.Scale("images/BOSS/Buta cakil/butacakil_talk.png", 750, 1600)


image bg_desa_siang       = im.Scale("images/BG/rumah kreswara ketika siang hari.png", 1920, 1080)    
image bg_desa_malam       = im.Scale("images/BG/rumah kreswara malam.png", 1920, 1080)        
image bg_ruangan_siang    = im.Scale("images/BG/DALAM RUMAH KRESWARA  (SIANG).png", 1920, 1080) 
image bg_ruangan_malam    = im.Scale("images/BG/DALAM RUMAH KRESWARA (MALAM).png", 1920, 1080)
image bg_cod              = im.Scale("images/BG/Kreswara menuju pulang ke rumah .png", 1920, 1080)     
image bg_panggung         = im.Scale("images/BG/panggung wayang .png", 1920, 1080) 
image bg_panggung_khusus  = im.Scale("images/BG/Wara melihat Bapaknya Jadi dalang.png", 1920, 1080)
image bg_rakit_pupils     = im.Scale("images/BG/Kreswara Rakit Pupils.png", 1920, 1080)
image bg_perpus           = im.Scale("images/BG/perpustakaan desa malam hari.png", 1920, 1080)
image bg_masuk_pupils     = im.Scale("images/BG/KRESWARA BERADA DI PERPUSTAKAAN MENGGUNAKAN PUPILS(1).png", 1920, 1080)
image bg_dunia_lain       = im.Scale("images/BG/desa digital + anomali .png", 1920, 1080)
image bg_versus           = im.Scale("images/BG/KRESWARA LAWAN BUTA CAKIL.png", 1920, 1080)
image bg_menang           = im.Scale("images/BG/KRESWARA MENGALAHKAN BUTA CAKIL.png", 1920, 1080)

image effect_1 = Movie(play="images/EFFECT/1.webm", loop=True, size=(1920, 3413))
image effect_2 = Movie(play="images/EFFECT/2.webm", loop=True, size=(1920, 3413))
image effect_3 = Movie(play="images/EFFECT/3.webm", loop=True, size=(1920, 3413))
image effect_4 = Movie(play="images/EFFECT/4.webm", loop=True, size=(1920, 3413))
image effect_5 = Movie(play="images/EFFECT/5.webm", loop=True, size=(1920, 3413))
image effect_6 = Movie(play="images/EFFECT/6.webm", loop=True, size=(1920, 3413))
image effect_7 = Movie(play="images/EFFECT/7.webm", loop=True, size=(1920, 3413))
image effect_8 = Movie(play="images/EFFECT/8.webm", loop=True, size=(1920, 3413))
image effect_9 = Movie(play="images/EFFECT/9.webm", loop=True, size=(1920, 3413))