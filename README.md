# CaptchaWithStegonography

Merhabalar ben Burhan Göksel. Fırat Üniversitesi Yazılım Mühendisliği bölümünde 4. sınıf dersi olan Bilgi Sistemler Ve Güvenliği dersi için yaptığım projeyi sizler ile paylaşmak istiyorum.


Captcha islemi ile Stegonografi isleminin birlestirilmesi.

Bu proje resim captcha islemi yapilmaktadir. Secilecek olan resimlere ayni zamanda belirlene anahtar da gizlenmektedir.
Kullanıcı islemlerini tamamladıktan sonra güvenlik sorusunu yanıtlayınca resiler üzerinde saklanan anahtar tekrar cikartilip kontrol edilir ve bu sayede:
	1)Kullanıcının Robot Olup Olmaması
	2)Göndericinin Gercektende O Hesabın Sahibi Olup Olmadıgı
	3)Ucuncu Kisinin Islem Esnasında Araya Girip Girmedigi
Kontrolleri yapılmıs olur.


Python Kütüphaneleri:
	1)PyQt---->UI operations
	2)sys----->i/o operations
	3)hashlib->sha256 operations
	4)PIL----->image open operations
	5)stepic-->stegonography operations
	6)sqlite3->database operations
	7)cv2----->image read operations
	8)numpy--->matrix operations


