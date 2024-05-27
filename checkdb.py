import os
import platform
import subprocess

Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

def clear_screen():
    """Efface l'écran en fonction du système d'exploitation."""
    os_name = platform.system().lower()
    if os_name == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def display_banner():
    """Affiche une bannière personnalisée."""
    clear_screen()
    print(f"""{Mage}
                                                                                                                                                      
  ▄▄█▀▀▀█▄█████▀  ▀████▀▀███▀▀▀███  ▄▄█▀▀▀█▄█████▀ ▀███▀▀███▀▀▀██▄ ▀███▀▀▀██▄
▄██▀     ▀█ ██      ██    ██    ▀█▄██▀     ▀█ ██   ▄█▀    ██    ▀██▄ ██    ██
██▀       ▀ ██      ██    ██   █  ██▀       ▀ ██ ▄█▀      ██     ▀██ ██    ██
██          ██████████    ██████  ██          █████▄      ██      ██ ██▀▀▀█▄▄
██▄         ██      ██    ██   █  ▄█▄         ██  ███     ██     ▄██ ██    ▀█
▀██▄     ▄▀ ██      ██    ██     ▄███▄     ▄▀ ██   ▀██▄   ██    ▄██▀ ██    ▄█
  ▀▀█████▀▄████▄  ▄████▄▄██████████ ▀▀█████▀▄████▄   ███▄████████▀ ▄████████ 
                                                                             
                                                                            discord.gg/searchhub
                  
            {Wh} [~] C O D E   B Y   H I M M L E R [~]  
        
    {Wh}[ 1 ] {Mage}SEARCH
    {Wh}[ 0 ] {Mage}Exit
""")

def search_in_files(directory, query):
    results = []
    try:
        command = f'rg -ia "{query}" {directory}'
        completed_process = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = completed_process.stdout.splitlines()
        for line in output:
            parts = line.split(':', 2)
            if len(parts) >= 2:
                results.append({
                    'file': parts[0],
                    'line_number': parts[1],
                    'line': parts[2] if len(parts) > 2 else ''
                })
    except Exception as e:
        print(f"{Re} Une erreur est survenue : {str(e)}")
    return results

def display_results(results):
    """Affiche les résultats de la recherche."""
    print(f"\n {Wh}========== {Mage}RÉSULTATS CHECKDB{Wh} ==========")
    if results:
        for result in results:
            print(f"\n {Wh}Fichier         :{Mage} {result['line_number']}")
            print(f" {Wh}Resultat        :{Mage} {result['line']}")
    else:
        print(f"{Re} Aucun résultat trouvé.")

def main_menu():
    """Affiche le menu principal et gère les choix de l'utilisateur."""
    while True:
        display_banner()
        input_user = input(f'\n   {Wh}Himmler~# {Mage}')

        if input_user == '1':
            query = input(f"\n {Wh}Entre ta recherche {Mage}: {Wh}")
            directory = input(f"\n {Wh}Entre le chemin du dossier contenant les fichiers {Mage}: {Wh}")
            results = search_in_files(directory, query)
            display_results(results)
            input(f"\nAppuie sur entrer pour continuer...")

        elif input_user == '0':
            print(f"\n  {Wh}[{Ye}!{Wh}] {Ye}Merci d'avoir utilisé l'outil CHECKDB!")
            break

        else:
            print(f" {Ye}Merci de choisir une bonne option !") 

if __name__ == '__main__':
    main_menu()
