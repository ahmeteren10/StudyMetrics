#PROJE DENEME

#HOŞGELDİNİZ EKRaNI, 
   # ** günlükçalışma / hedef süresi
   # ** soru çözümü  > ders 
   # ** deneme netleri kayıt
   # ** okunan kitaplar kayıt/ sayfa saysıs
   # ** takvim kısmı

#GÜNLÜK ÇALIŞMA EKRANI
  # bugünkü hedef ders süreni sorar. 
  # dersleri ekranda yazar, girilen ders sürelerini toplar
  # bugünkü toplam çalışma süresi:" 3 saat 20 dakida " gibi olarak yazdırır.  
  # en çok çalışılan ders "matematik" gibi yazar.
  # günlük hedef tamamlanan "½82" gibi yazar
  # çıkış ekranı ekle

#SORU ÇÖZÜMÜ EKRANI
  # bugünkü hedef soru sayını sorar. 
  # dersleri ekranda yazar, girilen soru sayılarını toplar
  # bugünkü toplam soru sayısını:"150 soru " gibi olarak yazdırır.  
  # en çok çalışılan ders "matematik" gibi yazar.
  # günlük hedef tamamlanan "½82" gibi yazar
  # çıkış ekranı ekle
  
#DENEME NETLERİ KAYIT
  # son denemeler kısmı 
    # esi deneme netlerini görüntüler
  # yeni deneme sonucu ekle ekranı
    # ders ders ndoğru yanlış sayısını kaydet
    # yüzde istatsitikleri ile sırala
    # grafik tabloları şekilli ile göster # çıkış ekranı ekle
    
#OKUNAN KİTAP KAYIT SAYFASI
 
  # yeni okunan kitap ismi alır 
  # sayfa saysısı alır.
  # kategori alınır.
  # bu hafta okunan kitaplar : 
  # en çok okunan tür : 
  # çıkış ekranı ekle
  
#TAKVİM KISMINI AÇTIĞINDA 
   # hedef tarih sorar.
   # o gün yapılan deneme varsa deneme netlerini gösterir.
   # o gün okunan kitapları gösterir.
   # o gün çalışılan ders süresi 
   # o gün çalışılan soru sayısı

# SQL LİTE İLE TAKVİMDE KAYITLI ÇALIŞMA SÜRELERİNİ GÖSTERME, SORU ÇÖZÜM SAYILARINI GÖSTERME,
# DENEME NETLERİNİ GÖSTERME, OKUNAN KİTAPLARI GÖSTERME, GRAFİKSEL OLARAK GÖSTERME
# BUNLARI EKLENECEK. (Grafiksel olarak göstermek için matplotlib kütüphanesi kullanılabilirim.)

# GÖRSEL GÜZELLEŞTİRME İLE DAHA ZEVK ALIANBİLİR Bİ HALE GETİREBİLİRİM.

dersler = [
    "📐 matematik",
    "📚 türkçe",
    "🌍 sosyal bilgiler",
    "🔬 fen bilgisi",
    "🔠 ingilizce",
    "🕌 din kültürü"
]


def menu (giris):
    while True:
        print("\n")
        print("\n =========== HOŞGELDİNİZ =========== ")
        print("1- günlük çalişma ")
        print("2- soru çözümü  ")
        print("3- deneme netleri ")
        print("4- okunan kitaplar ") 
        print("5- takvim ")
        print("0- Çıkış")

        islem = input("Yapmak istediğiniz işlem : ")

        if islem == "1":
            günlükçalişma(giris)
        elif islem == "2":
            soruçözümü(giris)
        elif islem == "3":
            denemenetleri(giris)
        elif islem == "4":
            okunankitaplar(giris)
        elif islem == "5":
            takvim(giris)
        elif islem == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("yanliş seçim")



def günlükçalişma (giris):

    çalişma_verileri = {}
    toplam_saat = 0

    print("\n =========== GÜNLÜK ÇALIŞMA SÜRESİ GİRİŞ ===========")

    for ders in dersler:
        saat = float(input(f"\n {ders} için çalişma süresini giriniz: "))
        çalişma_verileri[ders] = saat
        toplam_saat += saat
     
    print("\n =========== GÜNLÜK ÇALIŞMA SAATLERİ ===========")
    for ders, saat in çalişma_verileri.items():
        print(f"\n {ders}: {saat} saat.")

    if toplam_saat > 0:
        print("\n =========== İSTATİKSEL DAĞILIM VE YÜZDE ETKİSİ ===========")
        yuzdeler = {}

        for ders, saat in çalişma_verileri.items():
            yuzde = (saat / toplam_saat) * 100
            yuzdeler[ders] = yuzde
            print(f"\n{ders}: Toplam çalişmanin  %{yuzde:.2f}'i")  

        en_çok_çalişilan_ders = max(çalişma_verileri, key=çalişma_verileri.get) 
        en_yüksek_saat = çalişma_verileri[en_çok_çalişilan_ders]
        en_yüksek_yüzde = yuzdeler[en_çok_çalişilan_ders]
 
        print("\n =========== EN ÇOK ÇALIŞILAN DERS ===========")
        print( f"\nEn çok vakit ayrilan ders: {en_çok_çalişilan_ders.capitalize()}")
        print(f"Süre: {en_yüksek_saat} saat (Toplam çalişmanin %{en_yüksek_yüzde:.2f}'i)")
    else:
        print("\nHenüz hiç çalişma süresi girilmedi.")   
        
    

def soruçözümü(giris):
    soru_verileri = {}
    toplam_cozulen = 0
    toplam_dogru = 0
    toplam_yanlis = 0
    toplam_bos = 0
   

    print("\n =========== GÜNLÜK SORU ÇÖZÜMÜ GİRİŞİ ===========")
    for ders in dersler:
        print(f"\n>> {ders.upper()} <<")
        dogru = int(input("Doğru sayısı: "))
        yanlis = int(input("Yanlış sayısı: "))
        bos = int(input("boş sayısı: "))
        
        toplam_ders_sorusu = dogru + yanlis + bos
        
        #Verileri saklama
        soru_verileri[ders] = {
            "dogru": dogru,
            "yanlis": yanlis,
            "bos": bos,
            "toplam": toplam_ders_sorusu
        }
        
        toplam_cozulen += toplam_ders_sorusu
        toplam_dogru += dogru
        toplam_yanlis += yanlis
        toplam_bos += bos

    #ÖZET VE İSTATİSTİK YAZDIRMA
    print("\n ========= GÜNLÜK SORU RAPORU ==========")
    for ders, veri in soru_verileri.items():
         print(f"\n {ders.capitalize():<16}: {veri['dogru']} D | {veri['yanlis']} Y | {veri['bos']} B")

    print("-" * 55)
    print(f"TOPLAM ÇÖZÜLEN SORU : {toplam_cozulen}")
    print(f"GENEL DOĞRU / YANLIŞ : {toplam_dogru} Doğru | {toplam_yanlis} Yanlış")
    print(f"GENEL BOŞ SORU : {toplam_bos} Boş")

    if toplam_cozulen > 0:
        #Doğruluk Başarı Yüzdesi 
        basari_yuzdesi = (toplam_dogru / toplam_cozulen) * 100
        print(f"\n GENEL BAŞARI ORANI  : %{basari_yuzdesi:.2f}")

        #En çok soru çözülen ders
        en_cok_soru_ders = max(soru_verileri, key=lambda d: soru_verileri[d]['toplam'])
        print(f"\n EN ÇOK SORU ÇÖZÜLEN : {en_cok_soru_ders.capitalize()} ({soru_verileri[en_cok_soru_ders]['toplam']} soru)")

        #En az soru çözülen ders
        en_az_soru_ders = min(soru_verileri, key=lambda d: soru_verileri[d]['toplam'])
        print(f"\n EN AZ SORU ÇÖZÜLEN : {en_az_soru_ders.capitalize()} ({soru_verileri[en_az_soru_ders]['toplam']} soru)")
 
# Derslerin genel puan hesaplamasındaki ağırlık katsayıları 
DERS_KATSAYILARI = {
    "matematik": 4.0,
    "türkçe": 4.0,
    "fen bilgisi": 4.0,
    "sosyal bilgiler": 2.0,
    "ingilizce": 2.0,
    "din kültürü": 2.0
}

def denemenetleri(giris):
    deneme_verileri = {}
    toplam_net = 0
    toplam_puan = 100.0  #Taban puan
    toplam_soru = 0

    print("\n =========== DENEME NETLERİ VE PUAN ANALİZİ ===========")
    
    for ders in dersler:
        print(f"\n>> {ders.upper()} <<")
        dogru = int(input("Doğru sayısı : "))
        yanlis = int(input("Yanlış sayısı: "))
        bos = int(input("Boş sayısı: "))

        #BASİT Net hesabı (4 Yanlış 1 Doğruyu götürcek şekilde)
        net = dogru - (yanlis / 4)
        if net < 0:
            net = 0.0
            
        ders_toplam_soru = dogru + yanlis
        katsayi = DERS_KATSAYILARI.get(ders, 1.0)
        ders_puani = net * katsayi
        
        deneme_verileri[ders] = {
            "dogru": dogru,
            "yanlis": yanlis,
            "net": net,
            "toplam_soru": ders_toplam_soru,
            "ders_puani": ders_puani
        }
        
        toplam_net += net
        toplam_puan += ders_puani
        toplam_soru += ders_toplam_soru

    # RAPORLAMA VE ANALİZ
    print("\n ============= DENEME SONUÇ RAPORU =============")
    print(f"{'DERS':<18} | {'D':<3} | {'Y':<3} | {'NET':<6} | {'KATKI PUANI':<10}")
    print("-" * 55)
    
    for ders, veri in deneme_verileri.items():
        print(f"{ders.capitalize():<18} | {veri['dogru']:<3} | {veri['yanlis']:<3} | {veri['net']:<6.2f} | +{veri['ders_puani']:<10.2f}")

    print("=" * 55)
    print(f"TOPLAM NET     : {toplam_net:.2f} Net / {toplam_soru} Soru")
    print(f"TAHMİNİ PUAN   : {toplam_puan:.2f} Puan")

    if toplam_soru > 0:
        #En Başarılı ve En Kötü Gereken Dersler (Analiz)
        en_iyi_ders, en_iyi_veri = max(
           deneme_verileri.items(), 
        key=lambda x: x[1] ['net'] / x[1] ['toplam_soru'] if x[1]['toplam_soru'] > 0 else 0)


        zayif_ders, zayif_veri = min(
            deneme_verileri.items(),
        key=lambda x: x[1] ['net'] / x[1] ['toplam_soru'] if x[1]['toplam_soru'] > 0 else 0)

        print("\n =========== DERS BAZLI DETAYLI ANALİZ ===========")
        print(f"\n ⭐ En Başarılı Olduğun Ders   : {en_iyi_ders.capitalize()} ({deneme_verileri[en_iyi_ders]['net']:.2f} Net)")
        print(f"\n ⚠️ Öncelikli Çalışman Gereken : {zayif_ders.capitalize()} ({deneme_verileri[zayif_ders]['net']:.2f} Net)")
        
        # Puan bazında derslerin yüzde etkisi
        kazanilan_puan = toplam_puan - 100.0  # Taban puansız net katkı
        if kazanilan_puan > 0:
            en_cok_puan_getiren = max(deneme_verileri, key=lambda d: deneme_verileri[d]['ders_puani'])
            yuzde_etki = (deneme_verileri[en_cok_puan_getiren]['ders_puani'] / kazanilan_puan) * 100
            print(f"📈 Puana En Çok Katkı Sağlayan: {en_cok_puan_getiren.capitalize()} (Kazanılan toplam puanın %{yuzde_etki:.1f}'i)")


def okunankitaplar(giris):
    kitaplar = []
    toplam_sayfa = 0

    print("\n =========== OKUNAN KİTAPLAR MODÜLÜ ===========")
    
    adet = int(input("Kaç adet kitap bilgisi girmek istiyorsunuz?: "))
    
    for i in range(adet):
        print(f"\n>> {i+1}. Kitap <<")
        ad = input("Kitap Adı: ")
        yazar = input("Yazar Adı: ")
        sayfa = int(input("Okunan Sayfa Sayısı: "))
        
        kitaplar.append({
            "ad": ad,
            "yazar": yazar,
            "sayfa": sayfa
        })
        toplam_sayfa += sayfa

    # KİTAP LİSTESİ VE İSTATİSTİK
    print("\n =========== OKUNAN KİTAPLAR RAPORU ===========")
    print(f"{'KİTAP ADI':<25} | {'YAZAR':<20} | {'SAYFA':<6}")
    print("-" * 58)
    
    for k in kitaplar:
        print(f"{k['ad']:<25} | {k['yazar']:<20} | {k['sayfa']:<6}")

    print("=" * 58)
    print(f"TOPLAM OKUNAN SAYFA : {toplam_sayfa} Sayfa")

    if kitaplar:
        # En çok sayfa okunan kitabı bulma
        en_uzun_kitap = max(kitaplar, key=lambda x: x['sayfa'])
        ortak_sayfa = toplam_sayfa / len(kitaplar)
        
        print(f"📖 En Uzun Kitap    : {en_uzun_kitap['ad']} ({en_uzun_kitap['sayfa']} sayfa)")
        print(f"📊 Kitap Başı Ortalama: {ortak_sayfa:.1f} sayfa")


import calendar
from datetime import datetime

def takvim(giris):
    print("\n =========== TAKVİM VE HEDEF SAYACI ===========")
    
    # Şu anki yıl ve ayı alma
    simdi = datetime.now()
    yil = simdi.year
    ay = simdi.month
    
    # ayın takvimini basma
    print(f"\nBulunduğumuz Ay: {simdi.strftime('%B %Y')}\n")
    cal = calendar.TextCalendar(calendar.MONDAY)
    print(cal.formatmonth(yil, ay))

    # Sınav / Hedef Tarihi Sayacı
    print("-" * 40)
    print("🎯 SINAV / HEDEF GÜNÜ SAYACI")
    hedef_input = input("Hedef tarihinizi girin (YYYY-AA-GG formatında, örn: 2026-06-15): ")
    
    try:
        hedef_tarih = datetime.strptime(hedef_input, "%Y-%m-%d")
        bugun = datetime.now()
        kalan_gun = (hedef_tarih - bugun).days + 1
        
        if kalan_gun > 0:
            print(f"\n⏳ Hedefinize kalan süre: {kalan_gun} gün!")
        elif kalan_gun == 0:
            print("\n 🎉 Hedef günü bugünün kendisi!")
        else:
            print(f"\n ⚠️ Belirttiğiniz tarihin üzerinden {abs(kalan_gun)} gün geçmiş.")
    except ValueError:
        print(" ❌ Hatalı tarih formatı girdiniz.")




if __name__ == "__main__":
    menu("")