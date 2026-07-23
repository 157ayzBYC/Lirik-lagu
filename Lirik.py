import sys
import time
import os

#warna Terminal
os.system('')
PINK = "\033[38;5;206m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"
def jalanin_lirik():
    lirik = [
        ("Kuberikan semua perasaan ini", 0.1, PINK),
        ("Tapi mengapa cinta berpaling dariku", 0.09, BLUE),
        ("Aku hanya ingin kembali bahagia", 0.09, YELLOW),
        ("Oh Tuhan kembalikan senyumku yang dulu", 0.09, CYAN),
    ]

    # Jeda antar baris lirik (dalam detik)
    delay = [0.3, 0.2, 0.3, 0.6]

    print(f"{PINK}{BOLD}\n== Senyumku Yang Dulu - Willy Anggawinata =={RESET}\n")
    time.sleep(1)
    for i, (baris_lagu, delay_karakter, warna_baris) in enumerate(lirik):
        print(warna_baris, end='')

        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)

        print(RESET, end='')
        time.sleep(delay[i])
        print('')


jalanin_lirik()
