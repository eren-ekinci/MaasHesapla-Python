def Ayrac():
    print("-----------------------------------------------------------------------------")

def AsgariUcretZamOrani(mevcutMaas, zamliMaas):
    asgariUcret2023=11402
    asgariUcret2024=17002
    asgariUcretZamOrani=(asgariUcret2024/asgariUcret2023)*100-100
    Ayrac()
    print(f"Asgari Ücret Zam Orani % {asgariUcretZamOrani} ")
    Ayrac()

    Ayrac()
    print(f"Eski Maaşinizla Eski Asgari Ücret Arasindaki Fark: {mevcutMaas-asgariUcret2023}")
    Ayrac()

    Ayrac()
    print(f"Zaamli Maaşinizla Zamli Asgari Ücret Arasindaki Fark: {zamliMaas-asgariUcret2024}")
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
        print(f"Sizin Zam Orani % {maasZamOrani} ")
        Ayrac()


    elif (secim==2):
        mevcutMaas=float(input("Mevcut Maaş Giriniz: "))
        oran=float(input("Oran Giriniz: % "))
        zamliMaas= (mevcutMaas*oran)/100 + mevcutMaas
        Ayrac()
        print(f"Girilen Oran'a Göre Yeni Maasiniz: {zamliMaas}")
        Ayrac()

        AsgariUcretZamOrani(mevcutMaas,zamliMaas)

    elif (secim==3):
        print("Cikis Yapiliyor...")   
        break     
    
    else:
        print("Farkli Bir seçim Yaptiniz:")    











