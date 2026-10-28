
def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose 1 or 2: ").strip()

    try:
        temperature = float(input("Enter temperature: "))

        if choice == "1":
            result = temperature * 9 / 5 + 32
            print(f"Result: {result:.2f} °F")
        elif choice == "2":
            result = (temperature - 32) * 5 / 9
            print(f"Result: {result:.2f} °C")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


def distance_converter():
    print("\nDistance Converter")
    print("1. Kilometres to miles")
    print("2. Miles to kilometres")

    choice = input("Choose 1 or 2: ").strip()

    try:
        distance = float(input("Enter distance: "))

        if distance < 0:
            print("Distance cannot be negative.")
        elif choice == "1":
            print(f"Result: {distance * 0.621371:.2f} miles")
        elif choice == "2":
            print(f"Result: {distance / 0.621371:.2f} km")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


def text_analyzer():
    print("\nText Analyzer")
    text = input("Enter your text: ")

    print(f"Characters: {len(text)}")
    print(f"Words: {len(text.split())}")


def main():
    while True:
        print("\n" + "=" * 28)
        print("       ZENITH TOOLS")
        print("=" * 28)
        print("1. Temperature converter")
        print("2. Distance converter")
        print("3. Text analyzer")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            distance_converter()
        elif choice == "3":
            text_analyzer()
        elif choice == "4":
            print("Keep building. See you next time.")
            break
        else:
            print("Invalid choice. Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
