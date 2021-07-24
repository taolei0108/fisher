import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ""

        return r.json() if return_json else r.text


# r = requests.get("http://t.talelin.com/v2/book/isbn/9787115261274")
# print(r.text)