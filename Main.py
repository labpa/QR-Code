import qrcode
import os

def qr_code_erstellen(link, filename):
    # QR-Code erstellen
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )
    qr.add_data(link)
    qr.make(fit=True)

    # QR-Code als Bild
    img = qr.make_image(fill="black", back_color="white")

    # Ordner erstellen
    save_folder = "QR-Code"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Speicherort festlegen
    dateipfad = os.path.join(save_folder, f"{filename}.png")

    # Speichern des QR-Codes als Bild
    img.save(dateipfad)
    print(f" QR-Code wurde erfolgreich als '{dateipfad}' gespeichert!")

while True:
    # Prüfe eingabe auf Inhalt
    link = input("Bitte Link eingeben: ")
    if not link.strip():
        print("Fehler: Der Link darf nicht leer sein!")
        continue

    filename = input("Bezeichnung eingeben: ")
    if not filename.strip():
        print("Fehler: Der Dateiname darf nicht leer sein!")
        continue

    qr_code_erstellen(link, filename)

    weitermachen = input("Möchtest du einen weiteren QR-Code erstellen? (ja/nein): ").strip()
    if weitermachen not in ["ja", "j"]:
        print("Programm beendet.")
        break