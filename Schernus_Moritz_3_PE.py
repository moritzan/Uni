# %% Mensch-Maschinen Katzenbrunnen
import time #fuer sleep() 

#Frage Wasserstandssensor ab (fiktiv)
def GetWasserstand():
    #Fiktiver Code
    #wasserstand = sensor.readValue() <- fiktiver Code

    #Fiktiver Wasserstand
    wasserstand = 100

    return wasserstand

#Frage Zustand eines Physikalischen Knopfes ab
def getButton(buttonName = ""):

    #Dictionary Mapping um nach Pin eines Buttons zu schauen
    #Knopfname, Pin
    Buttons = {
        "Powerbutton": 12,
        "Resetbutton": 13,
        "AndererFiktiverButton": 14
    }

    #durchsuche dictionary
    button = Buttons.get(buttonName, "Ungueltiger Knopf")

    """
    Dictionary Debug-Zone!
    print ("gesuchter Button: " + str(buttonName))
    print ("gefundener Button: " + str(button))
    """

    #Falls Knopf ungueltig, dann gebe False zurueck
    if button == "Ungueltiger Knopf":
        return False


    #hole nun Status des Knopfes
    #buttonStatus = physButtonInput(button) <- fiktiver Code
    buttonStatus = True #unser fiktiver Button ist immer an, pscht

    return buttonStatus

#Pumpensteuerung
def PumpeSteuerung(status = False):
    #steuer Pumpe
    #pumpe.active(status) <- Fiktiver Code
    return

#aender LED Farbe 
def StatusLEDSteuerung(R,G,B):
    #checke ob keine unsinnigen Werte vorhanden sind
    #ansosten Wertkorrektur
    if R > 256:
        R = 256
    if G > 256:
        G = 256
    if B > 256:
        B = 256

    #aendere LED Farbe
    #LED.setColor(R,G,B) <- fiktiver Code
    return

#Logik des Katzenbrunnen
def Katzenbrunnen():
    Angeschaltet = getButton("Powerbutton")
    laufzeitZyklen = 0 #Wie lange die Maschine schon laeuft
    Wasserstand = GetWasserstand()

    #solange Angeschaltet, laufzeitzyklus unter 5 und Wasserstand über oder gleich 0
    while (Angeschaltet and laufzeitZyklen <= 5 and Wasserstand >= 0):
        #do something
        #Ich lebe!
        print("Brunnen aktiv")

        laufzeitZyklen += 1 #zaehle zyklus hoch

        #Mach Pumpe an (oder lass sie an)
        PumpeSteuerung(True)

        #Mach die LED Gruen
        StatusLEDSteuerung(0,256,0)

        #Warte 1 Sekunde
        time.sleep(1)

    #Programm wurde beendet
    print("Brunnen nicht aktiv")

    #Schalte Pumpe aus
    PumpeSteuerung(False)

    #Mach die LED Rot
    StatusLEDSteuerung(256,0,0)


#Programmstart
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Programmstart")
print("")

#fuehre Katzenbrunnenprogramm aus
Katzenbrunnen()

#nachdem programm beendet wurde
print ("Programm wurde beendet")



# %%
