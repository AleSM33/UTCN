import csv
from collections import Counter


# Citirea fișierului CSV cu cuvintele de ghicit
def citeste_fisierul(csv_file):
    cuvinte = []
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for linie in reader:
                cuvinte.append(linie)
    except Exception as e:
        print(f"Eroare la citirea fișierului: {e}")
    return cuvinte


# Funcția care joacă jocul Spânzurătoarea pentru un cuvânt
def joaca_spanzuratoarea(cuvant_de_ghicit, max_incercari=600):
    cuvant_partial = ['*' for _ in cuvant_de_ghicit]
    incercari = 0
    litere_ghicite = set()

    litere_frecvente = 'eaoinrstulcmpbdvfghjxzy'

    while '*' in cuvant_partial and incercari < max_incercari:
        litere_neghicite = [litera for litera in cuvant_de_ghicit if litera not in litere_ghicite]

        if not litere_neghicite:
            break
        frecvente_litere = Counter(litera for litera in litere_neghicite)
        litera_urmatoare = max(frecvente_litere, key=frecvente_litere.get)
        for idx, litera in enumerate(cuvant_de_ghicit):
            if litera == litera_urmatoare:
                cuvant_partial[idx] = litera

        litere_ghicite.add(litera_urmatoare)
        incercari += 1

    return ''.join(cuvant_partial), incercari


# Funcția principală care procesează toate cuvintele
def joaca_toate_cuvintele(csv_file):
    cuvinte = citeste_fisierul(csv_file)
    total_incercari = 0

    for cuvant in cuvinte:
        cod_joc, cuvant_incomplet, cuvant_corect = cuvant
        rezultat_final, numar_incercari = joaca_spanzuratoarea(cuvant_corect)
        total_incercari += numar_incercari
        print(f"Joc {cod_joc}: {cuvant_incomplet} -> {rezultat_final} (Încercări: {numar_incercari})")

    print(f"\nNumărul total de încercări pentru toate jocurile: {total_incercari}")


if __name__ == "__main__":
    cale_fisier = r'C:\cuvinte_de_verificat.txt'
    joaca_toate_cuvintele(cale_fisier)