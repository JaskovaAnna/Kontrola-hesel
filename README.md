# Kontrola Hesel

Tento skript kontroluje, zda bylo heslo kompromitováno pomocí API služby Have I Been Pwned.

## Jak používat

1. Naklonujte tento repozitář:
    ```bash
    git clone https://github.com/vaše-uživatelské-jméno/password-checker.git
    cd password-checker
    ```

2. Nainstalujte požadované balíčky:
    ```bash
    pip install requests
    ```

3. Spusťte skript:
    ```bash
    python vaše_jméno_skriptu.py
    ```

4. Zadejte heslo, když budete vyzváni. Skript zkontroluje, zda bylo vaše heslo kompromitováno, a zobrazí výsledek.

## Vysvětlení kódu

### Funkce

- `request_api_data(query_char)`: Posílá dotaz na API Have I Been Pwned s prvními 5 znaky SHA1 hashe hesla. Vrací odpověď z API.
- `get_password_leaks_count(hashes, hash_to_check)`: Analyzuje odpověď API a počítá, kolikrát bylo heslo kompromitováno.
- `pwned_api_check(password)`: Zahashuje heslo pomocí SHA1, pošle prvních 5 znaků hashe na API a zkontroluje odpověď, zda bylo heslo kompromitováno.
- `main()`: Hlavní funkce, která získá heslo od uživatele, zkontroluje ho pomocí funkce `pwned_api_check` a zobrazí výsledek.

### Použití

Skript používá modul `getpass` pro bezpečné zadání hesla od uživatele bez jeho zobrazení na obrazovce.

### Příklad

```plaintext
Zadejte heslo: ********
Vaše heslo nebylo prolomeno.
```
### Požadavky
- Python 3.x
- Modul requests (instalace pomocí pip install requests)

### Poznámky
- Tento skript kontroluje hesla pomocí API služby Have I Been Pwned, která poskytuje bezpečný a anonymní způsob, jak zjistit, zda bylo vaše heslo kompromitováno.
- Skript nezobrazuje heslo v terminálu pro zvýšení bezpečnosti.

### Kontext
- Tento skript byl vytvořen v rámci kurzu: Complete Python Developer Zero To Mastery

### Poděkování
- Děkujeme Troyovi Huntovi za službu Have I Been Pwned a API.
