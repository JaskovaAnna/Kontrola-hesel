import requests
import hashlib
import sys
import getpass


def request_api_data(query_char):
    """
    Posílá dotaz na API pomocí prvních 5 znaků zahashovaného hesla.
    """
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Chyba načítání {res.status_code}, zkontrolujte API a zkuste znova"
        )
    return res


def get_password_leaks_count(hashes, hash_to_chack):
    """
    Prochází odpověď API a hledá, kolikrát bylo heslo prolomeno.
    """
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_chack:
            return count
    return 0


def pwned_api_check(password):  # skutečné heslo ne hash
    """
    Zkontroluje, zda heslo bylo prolomeno pomocí API Have I Been Pwned.
    """
    # Zhashuje heslo pomocí SHA1
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    # Rozdělí hash na prvních a posledních 5 znaků
    fisrt5_char, tail = sha1password[:5], sha1password[5:]
    # Pošle dotaz na API s prvních 5 znaky hash
    response = request_api_data(fisrt5_char)
    # Vrátí počet prolomení hesla
    return get_password_leaks_count(response, tail)


def main():
    """
    Hlavní funkce, která zajišťuje zadání hesla, kontrolu přes API a zobrazení výsledku.
    """
    # Bezpečně získá heslo od uživatele
    password = getpass.getpass("Zadejte heslo: ")
    # Zkontroluje heslo přes API
    count = pwned_api_check(password)
    # Zobrazí výsledek
    if count:
        print(f"Vaše heslo bylo nalezeno v databázi prolomených hesel.")
        print(f"Bylo nalezeno {count} krát. Potřeba změna hesla!")
    else:
        print(f"Vaše heslo nebylo prolomeno.")

    return 


if __name__ == "__main__":
    # Spustí hlavní funkci a ukončí program
    sys.exit(main())
