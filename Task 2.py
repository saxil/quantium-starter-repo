import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./output.csv"

with open(OUTPUT_FILE_PATH, "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["sales", "date", "region"])

    for file_name in os.listdir(DATA_DIRECTORY):
        file_path = os.path.join(DATA_DIRECTORY, file_name)

        with open(file_path, "r", newline="") as input_file:
            reader = csv.reader(input_file)
            header = next(reader)

            for row in reader:
                product = row[0].strip().lower()
                price = float(row[1].replace("$", ""))
                quantity = int(row[2])
                date = row[3]
                region = row[4]

                if product == "pink morsel":
                    sales = price * quantity
                    writer.writerow([sales, date, region])
