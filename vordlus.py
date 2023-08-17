







def arvuta_koguintress(panga_marginaal,euribor,aastad,laenusumma,marginaalivaba_periood):
    kuud = aastad * 12
    kuine_intress = (panga_marginaal + euribor) / 12 / 100
    kuine_makse = laenusumma * kuine_intress * (1 + kuine_intress) ** kuud / ((1 + kuine_intress) ** kuud - 1)
    tavalised_kuised_maksed = []
    marginaali_vabad_maksed = []
    intressid = []
    for i in range(kuud):
        intress = laenusumma * kuine_intress
        pohiosa = kuine_makse - intress
        if i < marginaalivaba_periood:                
            intressid.append(laenusumma * euribor / 12 / 100)
            marginaali_vabad_maksed.append(pohiosa + laenusumma * euribor / 12 / 100)
        else:
            intressid.append(laenusumma * kuine_intress)
            tavalised_kuised_maksed.append(kuine_makse)
        laenusumma = laenusumma - pohiosa
    return sum(intressid)

euribor = 3.8
swed_marginaal = 1.8 # Siia pane oma panga marginaal
seb_marginaal = 1.8 # Siia pane oma panga marginaal
lhv_marginaal = 1.8 # Siia pane oma panga marginaal

swed=arvuta_koguintress(swed_marginaal,3.8,20,219000,24)
seb=arvuta_koguintress(seb_marginaal,3.8,20,219000,0)
lhv=arvuta_koguintress(lhv_marginaal,3.8,20,219000,12)


print(swed)
print(seb)
print(lhv)


