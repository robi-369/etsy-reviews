thonimport json
import os
from extractors.etsy_parser import EtsyParser
from outputs.exporters import Exporter

def main():
    # Load configuration settings
    with open(os.path.join(os.path.dirname(__file__), 'config/settings.example.json')) as f:
        settings = json.load(f)

    # Initialize the EtsyParser and Exporter
    parser = EtsyParser(settings)
    exporter = Exporter()

    # Scrape reviews data
    reviews_data = parser.scrape_reviews()

    # Export the data to JSON
    exporter.export_to_json(reviews_data)

if __name__ == "__main__":
    main()