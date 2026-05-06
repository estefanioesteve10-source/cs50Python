def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            # Tenta o formato numérico: MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")
                # Converte para int para validar
                month, day = int(month), int(day)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            # Tenta o formato de texto: Month Day, Year
            elif "," in date:
                # Remove a vírgula para facilitar o split
                parts = date.replace(",", "").split()

                if parts[0] in months:
                    month = months.index(parts[0]) + 1
                    day = int(parts[1])
                    year = parts[2]

                    if 1 <= day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

        except (ValueError, IndexError):
            # Se algo der errado na conversão ou split, pede a data de novo
            pass

if __name__ == "__main__":
    main()
