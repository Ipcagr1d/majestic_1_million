import csv
import io
import requests
from zipfile import ZipFile

MAJESTIC_DATA_URL = 'http://downloads.majestic.com/majestic_million.csv'


def majestic_etl():
    """
    Generator that:
        Downloads the CSV file from Majestic.
        Extracts the data from the CSV.
        Yields each site's rank and domain as a tuple.
    """

    response = requests.get(MAJESTIC_DATA_URL)
    with io.BytesIO(response.content) as zip_file:
        with ZipFile(zip_file, 'r') as zfile:
            csv_filename = zfile.namelist()[0]
            with zfile.open(csv_filename, 'r') as csv_file:
                reader = csv.reader(io.TextIOWrapper(csv_file, 'utf-8'))
                for row in reader:
                    rank = int(row[0])
                    domain = row[2]
                    yield rank, domain


def top_list(num=100):
    majestic_generator = majestic_etl()
    return [next(majestic_generator) for _ in range(num)]


if __name__ == "__main__":
    print(top_list())
