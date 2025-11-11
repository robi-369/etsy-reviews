thonimport json
from datetime import datetime

class Exporter:
    def __init__(self):
        self.output_dir = "data/"

    def export_to_json(self, data):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"etsy_reviews_{timestamp}.json"
        output_path = self.output_dir + file_name
        with open(output_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Exported reviews data to {output_path}")