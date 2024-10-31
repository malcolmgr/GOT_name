import os

def get_non_empty_input(prompt):
    """Ensures user input is not empty or just whitespace."""
    while True:
        response = input(prompt).strip()
        if response:
            return response
        print("Input cannot be empty. Please try again.")

def get_choice_input(prompt, options):
    """Display multiple-choice options and ensure valid input."""
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the corresponding number: ")) - 1
            if 0 <= choice < len(options):
                return options[choice]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_next_filename(base_name="throne_name", extension=".txt"):
    """Generates the next sequential filename in the same directory as the script."""
    i = 1
    while True:
        filename = f"{base_name}_{i}{extension}"
        if not os.path.exists(filename):
            return filename
        i += 1

def generate_throne_name():
    # 1. First Name and Predefined Titles
    first_name = get_non_empty_input("What is your first name? ")
    predefined_titles = [
        "Stormborn", "Breaker of Ice", "The Young Wolf",
        "Heir to the Iron Throne", "The Unbowed"
    ]
    title_choice = get_choice_input(
        "Select a title for yourself:", predefined_titles
    )

    # 2. Special Circumstance
    special_circumstance = input(
        "Was your birth marked by an unusual event (e.g., 'born under a blood moon')? "
    )

    # 3. Noble House Selection
    noble_houses = [
        "Starks", "Lannisters", "Arryns", "Greyjoys",
        "Tullys", "Tyrells", "Baratheons", "Martells", "Stormborn"
    ]
    noble_house = get_choice_input(
        "Which House are you from?", noble_houses
    )

    # 4. Title + Historical Reason
    titles = ["Butcher", "Prince", "Defender", "Custom title"]
    title_1 = get_choice_input("Choose a title that reflects your accomplishments:", titles)
    if title_1 == "Custom title":
        title_1 = get_non_empty_input("Enter your custom title: ")

    historical_reason = input(
        "Is there a specific event that earned you this title (e.g., 'for defeating the Night Serpent')? "
    )

    # 5. Region and Traditional Title
    title_2 = get_non_empty_input(
        "Name a distant land or people you govern (e.g., 'The Wildlands'): "
    )
    traditional_title = input(
        "What ancient title is associated with this land (e.g., 'Warden', 'Overseer')? "
    )

    # 6. Mythical Creatures
    mythical_creatures = [
        "Dragons", "Fae", "Phoenixes", "Chimeras", "Griffins"
    ]
    creature = get_choice_input(
        "Which mythical creatures or beings are you tied to?", mythical_creatures
    )

    # 7. Area or Landmark (US State or Country)
    area_landmark = get_non_empty_input(
        "Name a U.S. state or country you rule over: "
    )

    # 8. Unique Trait
    unique_trait = input(
        "What unique trait or life event sets you apart (e.g., 'The Unburnt')? "
    )

    # 9. Additional Handpicked Title
    additional_title = get_non_empty_input("Give me your best handpicked title: ")

    # Construct the Throne Name
    throne_name = (
        f"{first_name} {title_choice}, {' '.join(filter(None, [special_circumstance, 'of House', noble_house]))}\n"
        f"The First of {first_name}\n"
        f"{title_1}, {historical_reason}\n"
        f"{traditional_title} of {title_2}\n"
        f"The {creature}\n"
        f"Ruler of {area_landmark}\n"
        f"The {unique_trait}\n"
        f"The {additional_title}"
    )

    # Write to a Sequential Output File
    filename = get_next_filename()
    try:
        with open(filename, "w") as file:
            file.write(throne_name)
        print(f"Your throne name has been written to {filename}")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")

generate_throne_name()
