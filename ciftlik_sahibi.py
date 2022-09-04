try:
    import streamlit as st
    import streamlit.components.v1 as components
    from PIL import Image
except Exception as e:
    print(e)
# Resimlerle ilgili bilgiler
STYLE = """
    <style>
    img {
        max-width: 100%;
    }
    </style>
    """
# Sayfa yapısı
astyle = """
    display: inline;
    width: 200px;
    height: 40px;
    background: #F63366;
    padding: 9px;
    margin: 8px;
    text-align: center;
    vertical-align: center;
    border-radius: 5px;
    color: white;
    line-height: 25px;
    text-decoration: none;
    """
#sayfalar
st.set_page_config(
    page_title="Tarıma Yeni Bir Soluk",
    )
#sekmeler
tabs = ["Çiftlik Sahibi Erişim Sayfası"]
page = st.sidebar.radio("Sayfalar", tabs)
#resimler
image11 = Image.open("tarim_blokzinciri.png")
image13 = Image.open("python.png")
image14 = Image.open("arduino.png")
image15 = Image.open("pycharm.png")
image16 = Image.open("arduino_ide.png")
image18= Image.open("akillli_tarim_1.png")
image19=Image.open("esp32.png")
image20 = Image.open("dht11-isi-ve-nem-sensoru-kart-14197-17-B.jpg")
image21=Image.open("YL69-800x800.jpg")
image22=Image.open("download.jpg")
image23=Image.open("4-pinli-push-buton-siyah-6x6x5mm-11612-51-B.jpg")
image24=Image.open("16x2-lcd-ekran-yesil-uzerine-siyah-27412-11-B.jpg")

if page==("Çiftlik Sahibi Erişim Sayfası"):
    st.markdown("<h1 style='text-align:center;'><b> Geliştirilen Proje</b></h1>", unsafe_allow_html=True)
    st.image(image11,width=700, caption="Akıllı Tarım ve Blokzinciri")
    st.markdown("Bu çalışmada yapılmak istenen proje, dış etkilerden arındırılmış bir sera ortamında çalışacaktır.Ortamdaki ürünlerin çeşitliliğine bağlı olarak sera farklı bölümlere ayrılacaktır. Yetiştirilecek bitkilerin ideal ortamlarının oluşturulması için sıcaklık ve nem sensörleri gibi farklı sensörlerle veri toplanacaktır. Akıllı tarım denmesinin bir diğer sebebi olan ürünün durum değerlendirmesinde bulunmasıdır. Yani sensörlerden elde edilen değerlerin çiftlik sahibine, çiftlik çalışanlarına, toptancıya kısacası uygulamayı kullanan herkese ürün hakkında gerekli bilgilerin(ortamın sıcaklık, nem gibi ortam bilgilerinin yanında ürünün verim kalitesi) verilmeye çalışılacaktır. Ürün kalitesi değerlendirilme aşamasında bulanık mantıktan destek alınacaktır. ")
    st.image(image18,width=700, caption="Akıllı Tarım")
    if st.button("Sera Bilgisi"):
        components.iframe("http://192.168.43.232", width=600, height=2200)
    if st.checkbox("Projede Kullanılan Program dilleri"):
        st.image(image13, "Python")
        st.markdown("<a href='https://www.python.org/'>Python</a>", unsafe_allow_html=True)
        st.image(image14, "Arduino")
        st.markdown("<a href='https://www.arduino.cc/'>Arduino</a>", unsafe_allow_html=True)
    elif st.checkbox("Projede Kullanılan Editörler ve Ideler"):
        st.image(image15, "Pycharm")
        st.markdown("<a href='https://www.jetbrains.com/pycharm/'>Pycharm</a>", unsafe_allow_html=True)
        st.image(image16, "Arduino Ide")
        st.markdown("<a href='https://www.arduino.cc/'>Arduino</a>", unsafe_allow_html=True)
    elif st.checkbox("Projede Kullanılan Cihazlar"):
        st.image(image19, "Esp32")
        st.markdown( "<a href='https://www.robotistan.com/esp32-esp-32s-wifi-bluetooth-dual-mode-gelistirme-karti'>ESP32</a>", unsafe_allow_html=True)
        st.image(image20, "DHT11 Sensörü")
        st.markdown("<a href='https://www.robotistan.com/dht11-isi-ve-nem-sensoru-kart'>DHT11 Sensörü</a>",  unsafe_allow_html=True)
        st.image(image21, "Toprak Nem Sensörü ")
        st.markdown("<a href='https://www.robotistan.com/toprak-nemi-algilama-sensoru'>Toprak Nem Sensörü </a>", unsafe_allow_html=True)
        st.image(image22, "Fan ")
        st.markdown( "<a href='https://www.pttavm.com/4-cm-5v-2-pinli-fan-4x4x1-cm-boyutlarinda-fan-p-125737918'>Toprak Nem Sensörü </a>", unsafe_allow_html=True)
        st.image(image23, "Buton ")
        st.markdown("<a href='https://www.robotistan.com/4-pinli-push-buton-siyah-6x6x5mm?#ins_sr=eyJwcm9kdWN0SWQiOiIxNTcwMiJ9'>Buton</a>",   unsafe_allow_html=True)
        st.image(image24, "LCD Ekran ")
        st.markdown( "<a href='https://www.robotistan.com/16x2-lcd-ekran-i2c-lehimli-mavi-display?#ins_sr=eyJwcm9kdWN0SWQiOiIyMDI4NSJ9'>LCD Ekran</a>", unsafe_allow_html=True)
    elif st.checkbox("Örnek Görseller "):
        pass

