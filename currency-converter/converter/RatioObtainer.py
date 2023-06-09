import json, datetime, urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        try:
            with open('currency_.json') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return False
        date = str(datetime.date.today())
        
        for entry in data['entries']:
            if entry['base_currency'] == self.base and entry['target_currency'] == self.target and entry['date_fetched'] == date:
                return True
        return False

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        url = f'https://api.exchangerate.host/convert?from={self.base}&to={self.target}'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        if data['success']:
            ratio = data['info']['rate']
            # date = data['date']
            self.save_ratio(ratio)
        else:
            raise RuntimeError("Fetching failed")
        
    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        
        try:
            with open('currency_ratios.json') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {'entries':[]}

        date = str(datetime.date.today())
        
        for entry in data['entries']:
            if entry['base_currency'] == self.base and entry['target_currency'] == self.target and entry['date_fetched'] == date:
                entry['ratio'] = ratio
                break
        else:
            new_entry = {"base_currency":self.base, "target_currency": self.target, "date_fetched": date, "ratio": ratio}
            data["entries"].append(new_entry)

        with open('currency_ratios.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        with open('currency_ratios.json') as json_file:
            data = json.load(json_file)
        date = str(datetime.date.today())

        for entry in data['entries']:
            if entry['base_currency'] == self.base and entry['target_currency'] == self.target and entry['date_fetched'] == date:
                return entry['ratio']
