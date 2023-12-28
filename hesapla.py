def Ayrac():
    print("-----------------------------------------------------------------------------")

def AsgariUcretZamOrani(mevcutMaas, zamliMaas):
    asgariUcret2023=11402
    asgariUcret2024=17002
    asgariUcretZamOrani=(asgariUcret2024/asgariUcret2023)*100-100
    Ayrac()
    print("Asgari Ücret Zam Orani % {0} " .format(asgariUcretZamOrani))
    Ayrac()

    Ayrac()
    print("Eski Maaşinizla Eski Asgari Ücret Arasindaki Fark: {0}" .format(mevcutMaas-asgariUcret2023))
    Ayrac()

    Ayrac()
    print("Zaamli Maaşinizla Zamli Asgari Ücret Arasindaki Fark: {0}" .format(zamliMaas-asgariUcret2024))
    Ayrac()
    

def MaasZamOrani(mevcutMaas,zamliMaas):
    zamOrani=(zamliMaas/mevcutMaas)*100-100
    return zamOrani

while True:

    secim=int(input("[1] Maasiniz'a Yüzde Kaç Zaam Yapilmis \n[2] Zam Oranina Göre Maaşini Hesapla \n[3] Cikis \nSecim Giriniz: "))

    if (secim==1):
        mevcutMaas=int(input("Mevcut Maaş Giriniz: "))
        zamliMaas=int(input("Zamli Maaş Giriniz: "))
        maasZamOrani=MaasZamOrani(mevcutMaas,zamliMaas)

        AsgariUcretZamOrani(mevcutMaas,zamliMaas)

        Ayrac()
        print("Sizin Zam Orani % {0} " .format(maasZamOrani))
        Ayrac()


    elif (secim==2):
        mevcutMaas=float(input("Mevcut Maaş Giriniz: "))
        oran=float(input("Oran Giriniz: % "))
        zamliMaas= (mevcutMaas*oran)/100 + mevcutMaas
        Ayrac()
        print("Girilen Oran'a Göre Yeni Maasiniz: {0}" .format(zamliMaas))
        Ayrac()

        AsgariUcretZamOrani(mevcutMaas,zamliMaas)

    elif (secim==3):
        print("Cikis Yapiliyor...")   
        break     
    
    else:
        print("Farkli Bir seçim Yaptiniz:")    











