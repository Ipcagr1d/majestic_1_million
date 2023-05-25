import csv
import io
import requests

MAJESTIC_DATA_URL = 'http://downloads.majestic.com/majestic_million.csv'


def majestic_etl():
    """
    Generator that:
        Downloads the CSV file from Majestic.
        Yields each site's rank and domain as a tuple.
    """

    response = requests.get(MAJESTIC_DATA_URL)
    response.raise_for_status()
    csv_text = response.text

    reader = csv.reader(csv_text.splitlines())
    next(reader)  # Skip header row

    for row in reader:
        rank = int(row[0])
        domain = row[2]
        yield rank, domain


def top_list(num=100):
    majestic_generator = majestic_etl()
    return [next(majestic_generator) for _ in range(num)]


if __name__ == "__main__":
    print(top_list())
