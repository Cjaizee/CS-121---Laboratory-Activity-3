import pygame
import time
from abc import ABC, abstractmethod

pygame.init()

def play_audio(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

class MusicalInstrument(ABC):
    def __init__(self, instrument_type, instrument_classification, material, brand, price):
        self.instrument_type = instrument_type
        self.instrument_classification = instrument_classification
        self.material = material
        self.brand = brand
        self.price = price
        self.is_tuned = False

    @abstractmethod
    def play_sound(self): pass

    @abstractmethod
    def tune(self): pass

    @abstractmethod
    def maintenance(self): pass

    @abstractmethod
    def store(self): pass

class Guitar(MusicalInstrument):
    def __init__(self, material, brand, price, strings, type, fretboard_material, pickup_type):
        super().__init__('Guitar', 'String', material, brand, price)
        self.strings = strings
        self.type = type
        self.fretboard_material = fretboard_material
        self.pickup_type = pickup_type

    def play_sound(self):
        if self.is_tuned:
            play_audio("audio/guitar_tuned.wav")
        else:
            play_audio("audio/guitar_untuned.mp4")

    def tune(self):
        self.is_tuned = True

    def maintenance(self):
        print("Change strings regularly and clean fretboard.")

    def store(self):
        print("Store in a hard case to avoid warping.")
        print("Returning to main menu...\n")
        time.sleep(1)

class Piano(MusicalInstrument):
    def __init__(self, material, brand, price, keys, pedals, soundboard_material, tuning_stability):
        super().__init__('Piano', 'Keyboard', material, brand, price)
        self.keys = keys
        self.pedals = pedals
        self.soundboard_material = soundboard_material
        self.tuning_stability = tuning_stability

    def play_sound(self):
        if self.is_tuned:
            play_audio("audio/piano_tuned.wav")
        else:
            play_audio("audio/piano_untuned.wav")

    def tune(self):
        self.is_tuned = True

    def maintenance(self):
        print("Regular key action checks and tuning.")

    def store(self):
        print("Keep in temperature-controlled room.")
        print("Returning to main menu...\n")
        time.sleep(1)

class Drums(MusicalInstrument):
    def __init__(self, material, brand, price, size, drumhead_material, shell_material):
        super().__init__('Drums', 'Percussion', material, brand, price)
        self.size = size
        self.drumhead_material = drumhead_material
        self.shell_material = shell_material

    def play_sound(self):
        if self.is_tuned:
            play_audio("audio/drums_tuned.wav")
        else:
            play_audio("audio/drums_untuned.wav")

    def tune(self):
        self.is_tuned = True

    def maintenance(self):
        print("Check and replace drumheads.")

    def store(self):
        print("Cover and keep in dry room.")
        print("Returning to main menu...\n")
        time.sleep(1)

class Violin(MusicalInstrument):
    def __init__(self, material, brand, price, bow_type, size, string_material, chin_rest_type):
        super().__init__('Violin', 'String', material, brand, price)
        self.bow_type = bow_type
        self.size = size
        self.string_material = string_material
        self.chin_rest_type = chin_rest_type

    def play_sound(self):
        if self.is_tuned:
            play_audio("audio/violin_tuned.mp3")
        else:
            play_audio("audio/violin_untuned.wav")

    def tune(self):
        self.is_tuned = True

    def maintenance(self):
        print("Clean and re-hair bow, maintain strings.")

    def store(self):
        print("Store in a violin case with dehumidifier.")
        print("Returning to main menu...\n")
        time.sleep(1)

instruments = [
    Guitar("Mahogany", "Ibanez", 12000, 6, "Acoustic", "Rosewood", "Humbucker"),
    Piano("Spruce", "Kawai", 350000, 88, True, "Maple", "Stable"),
    Drums("Birch", "Pearl", 85000, "Full Size", "Mylar", "Birch"),
    Violin("Maple", "Stradivarius", 200000, "Baroque", "4/4", "Nylon", "Ebony")
]

def main_menu():
    while True:
        print("\nInstrument Menu:")
        for i, instr in enumerate(instruments):
            print(f"{i+1}. {instr.instrument_type} ({instr.brand})")
        print("0. Exit")

        choice = input("Choose an instrument: ")
        if choice == '0':
            print("Thank you po for your time!")
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(instruments)):
            print("Invalid choice.")
            continue

        instrument = instruments[int(choice)-1]
        instrument_menu(instrument)

def instrument_menu(instrument):
    print(f"\n--- {instrument.instrument_type} Properties ---")
    for attr, value in instrument.__dict__.items():
        print(f"{attr.replace('_', ' ').capitalize()}: {value}")

    while True:
        print(f"\n{instrument.instrument_type} - {instrument.brand}")
        print("1. Play Sound")
        print("2. Tune")
        print("3. Maintenance Info")
        print("4. Store (Back to Menu)")
        choice = input("Choose an action: ")

        if choice == '1':
            instrument.play_sound()
        elif choice == '2':
            instrument.tune()
        elif choice == '3':
            instrument.maintenance()
        elif choice == '4':
            instrument.store()
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main_menu()
