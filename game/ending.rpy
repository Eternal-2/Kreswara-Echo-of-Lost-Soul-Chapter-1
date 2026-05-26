label ending_good:
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 1.0

    play sound "audio/sfx/chapter 1/suara digital halus .mp3"
    scene black with dissolve
    pause 2.0

    jump scene_rumah_sakit_good

label ending_bad:
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 1.0

    play sound "audio/sfx/chapter 1/suara digital halus .mp3"
    scene black with dissolve
    pause 2.0

    jump scene_rumah_sakit_bad


label scene_rumah_sakit_good:

    scene bg_rumah_sakit with Dissolve(2.0)
    play music "audio/backsound/ending/good_ending_ambient.mp3" fadein 2.0
    play sound "audio/sfx/ending/detak_jantung.mp3" loop

    play sound "audio/sfx/ending/angin_sore_jendela.mp3" loop

    nr "Suara mesin detak jantung begitu menggema di telinganya."
    nr "Suasana rumah sakit itu masih sama seperti berbulan-bulan lalu saat ia pertama kali datang ke sana."
    nr "Tubuh sang kasih terbaring lemah di ranjang putih bersih, masih memperjuangkan hidupnya di tengah ketidakpastian detik-detik kehidupan semu dalam komanya."

    nr "Cahaya matahari tampak berdiri megah di balik jendela yang entah sudah berapa kali ia pandangi setiap hari."
    nr "Wanita itu masih menatap layar laptop yang menampilkan credit game berjudul Kreswara: Echoes of the Lost Souls."
    nr "Sebuah game yang begitu indah hingga membuatnya kembali menangis tersedu-sedu."
    nr "Tangannya kemudian membuka buku harian biru, warna yang diyakini pemiliknya sebagai warna favorit kekasih tak terucapnya."

    play sound "audio/sfx/ending/buku_dibuka.mp3"

    nr "Isi buku itu sangat beragam, mulai dari bait-bait puisi tentang cinta, lirik lagu bertema kasih, hingga beberapa cerita pendek mengenai bagaimana jadinya jika cinta mereka bersemi di kehidupan selanjutnya."
    nr "Pada lembar paling awal, terdapat sesuatu yang mengganjal hatinya — sebuah foto dua orang yang sama-sama tidak pernah berani menyatakan perasaan masing-masing."

    centered "BIODATA"
    centered "Nama: Asleen Sankarilla"
    centered "Tanggal lahir: 15 Maret 2005"
    centered "Catatan: 'Harus diingat.'"
    centered "Warna kesukaan: Biru dan hijau"
    centered "Catatan: 'Untuk referensi kado buat dia, karena dia INFP dan Pisces.'"
    centered "Makanan kesukaan: Apa pun yang manis, terutama cokelat"
    centered "Catatan: 'Tapi harus diingetin juga biar dia nggak keseringan.'"
    centered "Hal yang paling dia sukai: Sastra, terutama novel"
    centered "Catatan: 'Hehe, aku harus rajin nabung kalau ada novel dari penulis favoritnya terbit.'"
    centered "Jurusan yang dia inginkan: Sastra Indonesia"
    centered "Catatan: 'Moga-moga kita satu kampus, hehe.'"
    centered "Note: Tes masuk universitas sudah di depan mata. Rencananya aku dan dia bakal berangkat bareng naik motor. Moga-moga kita aman di jalan, dan kita berdua masuk ke jurusan yang kita pengenin, hehe."

    asleen "Tapi pada akhirnya, kita tidak pernah sampai ke tempat tes itu ya, Kreswara Radyana."

    play sound "audio/sfx/ending/napas_bergetar.mp3"

    asleen "Kau ingat tidak? Bagaimana dulu kita hanyalah remaja penuh harapan yang akan berangkat melaksanakan tes masuk universitas?"
    asleen "Namun, kecelakaan itu menghancurkan segalanya. Setidaknya, begitulah bagiku."
    asleen "Melihatmu koma dan diam seperti ini adalah takdir yang sama sekali tidak pernah kubayangkan akan berakhir begini."
    asleen "Namun, karena itulah semuanya terasa datang terlambat, ya?"
    asleen "Bagaimana dulu aku akhirnya berniat memberitahumu bahwa aku mencintaimu."
    asleen "Mencintai dirimu yang selalu menjadi angin sejuk di tengah badai hidupku."
    asleen "Namun, aku tidak pernah menyangka ternyata kau memendam semua itu juga. Sungguh, aku tidak tahu. Maaf."
    asleen "Aku masih mengingatnya dengan jelas ketika beberapa waktu lalu ibumu memberikan buku catatanmu."
    asleen "Namun, aku justru menemukan hal paling menarik di sana — diriku sendiri."
    asleen "Jiwaku yang kau simpan dalam berbagai bentuk di dalam buku itu."
    asleen "Dan game ini… baru saja kumainkan. Aku menemukannya dari sebuah kode yang, untungnya, berhasil kupecahkan."

    jump puzzle_kode_good



label puzzle_kode_good:

    play sound "audio/sfx/chapter 1/keyboar komputer .mp3"

    nr "Asleen mengingat kembali saat dia sangat bersusah payah memecahkan kode itu."

    menu:
        caption "Kode apa yang tertulis di halaman terakhir buku?\n\n01000001 01010011 01001100 01000101 01000101 01001110"

        "ASLEEN":
            play sound "audio/sfx/ending/notif_berhasil.mp3"
            jump puzzle_kode_good_berhasil

        "KRESWARA":
            play sound "audio/sfx/ending/notif_error.mp3"
            nr "Bukan itu jawabannya..."
            jump puzzle_kode_good

        "PUPILS":
            play sound "audio/sfx/ending/notif_error.mp3"
            nr "Bukan itu jawabannya..."
            jump puzzle_kode_good


label puzzle_kode_good_berhasil:

    nr "Sebuah titik kehidupan datang menyeruak di tengah lamunan tak berujung milik Asleen."
    nr "Harapan yang selama ini selalu ia simpan di wajahnya — harapan bahwa suatu hari nanti Kreswara akan bangun."
    nr "Dan akhirnya, saat itu tiba."

    stop sound
    play sound "audio/sfx/ending/monitor_berubah.mp3"

    nr "Sepasang mata jernih yang masih kebingungan mencari cahaya perlahan menatap sosok yang selama ini ia dambakan."

    play sound "audio/sfx/ending/napas_pelan.mp3"

    nr "Kreswara akhirnya bangun."
    nr "Dan kini ia tahu, Asleen merasakan cinta yang sama dengannya."
    nr "Cinta yang dulu lama terpendam itu akhirnya menyala terang."

    play sound "audio/sfx/ending/tangis_bahagia.mp3"

    scene black with Dissolve(3.0)
    pause 1.5

    play music "audio/backsound/ending/good_ending_theme.mp3" fadein 2.0

    centered "── GOOD ENDING ──"
    centered "\"Cahaya yang Akhirnya Tiba\""
    pause 2.0

    centered "Kreswara dan Asleen — dua jiwa yang lama menahan kata,"
    centered "akhirnya menemukan jalannya pulang."
    pause 2.0

    centered "Terima kasih sudah bermain."
    centered "Digital Wayang: Kreswara and the Lost Souls"
    pause 3.0

    $ persistent.chapter2_unlocked = True
    $ persistent.chapter3_unlocked = True
    $ persistent.chapter4_unlocked = True

    scene black with Dissolve(2.0)
    pause 1.0
    jump chapter_select_screen


label scene_rumah_sakit_bad:

    scene bg_rumah_sakit with Dissolve(2.0)
    play music "audio/backsound/ending/bad_ending_ambient.mp3" fadein 2.0
    play sound "audio/sfx/ending/detak_jantung.mp3" loop
    play sound "audio/sfx/ending/hujan_samar.mp3" loop

    nr "Suara mesin detak jantung begitu menggema di telinganya."
    nr "Suasana rumah sakit itu masih sama seperti berbulan-bulan lalu saat ia pertama kali datang ke sana."
    nr "Tubuh sang kasih terbaring lemah di ranjang putih bersih, masih memperjuangkan hidupnya."

    nr "Cahaya tertutup awan mendung yang tampak menutupi matahari di balik jendela."
    nr "Wanita itu masih menatap layar laptop yang menampilkan credit game berjudul Kreswara: Echoes of the Lost Souls."
    nr "Air matanya lagi-lagi jatuh dari kedua mata indah yang kini sembab dan tampak lesu itu."

    play sound "audio/sfx/ending/isakan_pelan.mp3"

    play sound "audio/sfx/ending/buku_dibuka.mp3"

    nr "Tangannya kemudian membuka buku harian biru."
    nr "Isi buku itu sangat beragam — yang kini hanyalah menjadi kenangan yang abadi."

    centered "BIODATA"
    centered "Nama: Asleen Sankarilla"
    centered "Tanggal lahir: 15 Maret 2005"
    centered "Catatan: 'Harus diingat.'"
    centered "Warna kesukaan: Biru dan hijau"
    centered "Makanan kesukaan: Apa pun yang manis, terutama cokelat"
    centered "Hal yang paling dia sukai: Sastra, terutama novel"
    centered "Jurusan yang dia inginkan: Sastra Indonesia"
    centered "Note: Tes masuk universitas sudah di depan mata. Rencananya aku dan dia bakal berangkat bareng naik motor. Moga-moga kita aman di jalan, dan kita berdua masuk ke jurusan yang kita pengenin, hehe."

    asleen "Tapi pada akhirnya, kita tidak pernah sampai ke tempat tes itu ya, Kreswara Radyana."

    asleen "Kau ingat tidak? Bagaimana dulu kita hanyalah remaja penuh harapan?"
    asleen "Namun, kecelakaan itu menghancurkan segalanya. Kejadian yang membuat semuanya menjadi sendu."
    asleen "Melihatmu koma dan diam seperti ini adalah takdir yang sama sekali tidak pernah kubayangkan."
    asleen "Namun, karena itulah semuanya terasa datang terlambat, ya?"
    asleen "Bagaimana dulu aku akhirnya berniat memberitahumu bahwa aku mencintaimu."
    asleen "Mencintai dirimu yang selalu menjadi angin sejuk di tengah badai hidupku."
    asleen "Namun, aku tidak pernah menyangka ternyata kau memendam semua itu juga. Maaf."
    asleen "Dan game ini… baru saja kumainkan. Aku menemukannya dari sebuah kode yang berhasil kupecahkan."

    jump puzzle_kode_bad


label puzzle_kode_bad:

    play sound "audio/sfx/ending/keyboard_perlahan.mp3"

    nr "Asleen mengingat kembali saat dia sangat bersusah payah memecahkan kode itu."

    menu:
        caption "Kode apa yang tertulis di halaman terakhir buku?\n\n01000001 01010011 01001100 01000101 01000101 01001110"

        "ASLEEN":
            play sound "audio/sfx/ending/notif_berhasil.mp3"
            jump puzzle_kode_bad_berhasil

        "KRESWARA":
            play sound "audio/sfx/ending/notif_error.mp3"
            nr "Bukan itu jawabannya..."
            jump puzzle_kode_bad

        "PUPILS":
            play sound "audio/sfx/ending/notif_error.mp3"
            nr "Bukan itu jawabannya..."
            jump puzzle_kode_bad


label puzzle_kode_bad_berhasil:

    nr "Setelah untaian kata yang terucap dari hatinya, ia kini bersiap-siap untuk kembali pulang."
    nr "Dengan hati yang berat ia mengucap salam perpisahan yang sudah sekian kali terucap."

    play sound "audio/sfx/ending/kursi_bergeser.mp3"

    asleen "Aku pulang dulu yah… aku harap kamu membaik dan kita bisa bepergian kemana-mana lagi sama-sama."

    play sound "audio/sfx/ending/langkah_menjauh.mp3"

    nr "Matahari pun mulai terbit di keesokan harinya."
    nr "Dengan energi yang kembali terisi penuh, dengan bunga yang aromanya masuk ke seluruh penjuru ruangan."
    nr "Ditambah dengan buah apel yang sangat Wara sukai."

    play sound "audio/sfx/ending/burung_pagi.mp3"

    asleen "Semoga dia suka dengan buahnya…"

    nr "Dengan perlahan ia melangkahkan kaki kecilnya menuju ruang 07 yang biasa ia kunjungi."
    nr "Ia membuka pintu itu dengan satu tangan dan tangan lainnya memegang bunga dan buah kesukaan Wara."

    play sound "audio/sfx/ending/pintu_dibuka.mp3"

    nr "Namun yang ia lihat justru beberapa petugas kesehatan dan dokter yang sedang menutupi tubuh pasangannya itu dengan kain putih."
    nr "Dari jauh kakinya terlihat pucat dan sudah tidak bergerak."
    nr "Perlahan dokter melepas alat bantu pernapasan itu."

    stop sound
    play sound "audio/sfx/ending/monitor_panjang.mp3"

    nr "Kakinya terkukur lemas. Hatinya bergetar. Lalu air matanya bertetesan jatuh."
    nr "Beberapa petugas dan dokter mencoba untuk menguatkan dan memeluknya dengan kuat."
    nr "Namun itu tidak ada artinya, karena semua itu tidak bisa mengembalikan wajah pucat dengan selimut putih yang menyelimuti tubuhnya."

    play sound "audio/sfx/ending/bunga_jatuh.mp3"

    nr "Kreswara pergi meninggalkan Asleen selamanya dan tidak akan pernah kembali."

    play sound "audio/sfx/ending/tangisan_pecah.mp3"

    scene black with Dissolve(3.0)
    pause 1.5

    play music "audio/backsound/ending/bad_ending_theme.mp3" fadein 2.0

    centered "── BAD ENDING ──"
    centered "\"Terlambat\""
    pause 2.0

    centered "Kreswara dan Asleen — dua jiwa yang lama menahan kata,"
    centered "namun waktu tidak pernah menunggu siapa pun."
    pause 2.0

    centered "Terima kasih sudah bermain."
    centered "Digital Wayang: Kreswara and the Lost Souls"
    pause 3.0

    $ persistent.chapter2_unlocked = True
    $ persistent.chapter3_unlocked = True
    $ persistent.chapter4_unlocked = True

    scene black with Dissolve(2.0)
    pause 1.0
    jump chapter_select_screen
