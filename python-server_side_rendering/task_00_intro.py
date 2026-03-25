def generate_invitations(template, attendees):
    # Vérification des types
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Vérification template vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Vérification liste vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Traitement des attendees
    for i, attendee in enumerate(attendees, start=1):
        try:
            # Récupération des valeurs avec fallback "N/A"
            name = attendee.get("name") or "N/A"
            event_title = attendee.get("event_title") or "N/A"
            event_date = attendee.get("event_date") or "N/A"
            event_location = attendee.get("event_location") or "N/A"

            # Remplacement des placeholders
            output = template
            output = output.replace("{name}", str(name))
            output = output.replace("{event_title}", str(event_title))
            output = output.replace("{event_date}", str(event_date))
            output = output.replace("{event_location}", str(event_location))

            # Nom du fichier
            filename = f"output_{i}.txt"

            # Écriture du fichier
            with open(filename, "w") as file:
                file.write(output)

        except Exception as e:
            print(f"Error processing attendee {i}: {e}")
