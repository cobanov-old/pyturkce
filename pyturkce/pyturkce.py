from .utils import getData


class Sozluk:
    """TDK API kullanarak verilen kelimeler hakkinda JSON datasi dondurur, 
    ayni zamanda anlam, deyim ve cumle ici ornekler getirir.
    """

    def __init__(self, kelime):
        self.data = getData(kelime)
        self.kelime = kelime
        self.anlamlar = []
        self.deyimler = []
        self.ornekler = []
        self.parseData()

    # def __str__(self):

    #     return f"Anlam: {self.anlamlar[0]}\nOrnek: {self.ornekler[0]}\nAtasozu: {self.deyimler[0]}\nDaha fazla anlam ve ornek icin lutfen metodlari kullanin."

    def getAnlamlar(self):

        self.anlamlar = [anlam['anlam']
                         for anlam in self.data[0]['anlamlarListe']]

    def getDeyimler(self):  # Deyimler
        try:
            self.deyimler = [anlam['madde']
                             for anlam in self.data[0]['atasozu']]
        except KeyError:
            self.deyimler = 'Bu kelime icin atasozu bulunamadi!'

    def getOrnekler(self):    # Ornekler
        self.ornekler = []
        try:
            for anlam in self.data[0]['anlamlarListe']:
                for ornek in anlam['orneklerListe']:
                    self.ornekler.append(ornek['ornek'])
        except KeyError:
            self.ornekler = 'Bu kelime icin ornek cumle bulunamadi!'

    def parseData(self):
        self.getAnlamlar()
        self.getDeyimler()
        self.getOrnekler()


def tr2eng(text):
    """Turkce karakterlere sahip metinleri ingilizce karakterler ile degistirir

    Args:
        text (string): Turkce karakterlere sahip metin

    Returns:
        string: Ingilizce karakterlere sahip cumleyi dondurur
    """
    eslestirici = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    sonuc = text.translate(eslestirici)
    return sonuc
