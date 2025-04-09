import roman10
import subprocess
import sys
# NOTE! Remember to install the "coverage" module using "pip3 install coverage" if it's not already installed.
# Roman Numeral System - Main Menu and User Interface
# This program provides a menu for converting between Roman numerals and integers.

def main_menu():
    while True:
        print("\n--- Romerska Siffersystemet ---")
        print("1. Konvertera heltal till romersk siffra")
        print("2. Konvertera romersk siffra till heltal")
        print("3. Kör alla tester")
        print("4. Kör coverage-analys")
        print("5. Avsluta")
        choice = input("Välj ett alternativ (1–5): ").strip()

        if choice == "1":
            try:
                number = int(input("Ange ett heltal (1–4999): "))
                print("Romersk siffra:", roman10.to_roman(number))
            except roman10.NotIntegerError as e:
                print("Fel:", e)
            except roman10.OutOfRangeError as e:
                print("Fel:", e)
            except Exception as e:
                print("Ett oväntat fel inträffade:", e)

        elif choice == "2":
            try:
                roman = input("Ange en romersk siffra: ").upper()
                print("Heltal:", roman10.from_roman(roman))
            except roman10.InvalidRomanNumeralError as e:
                print("Fel:", e)
            except Exception as e:
                print("Ett oväntat fel inträffade:", e)

        elif choice == "3":
            print("\nKör tester med unittest...\n")
            subprocess.run([sys.executable, "-m", "unittest", "-v", "romantest1"])

        elif choice == "4":
            print("\nKör coverage och visar rapport...\n")
            subprocess.run(["coverage", "run", "--branch", "-m", "unittest", "romantest1"])
            subprocess.run(["coverage", "report", "-m"])
            show_html = input("Vill du öppna HTML-rapporten i webbläsaren? (j/n): ").strip().lower()
            if show_html == "j":
                subprocess.run(["coverage", "html"])
                subprocess.run(["start", "htmlcov/index.html"], shell=True)

        elif choice == "5":
            print("Avslutar...")
            break

        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == '__main__':
    main_menu()