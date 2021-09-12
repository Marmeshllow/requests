import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self._get_headers()
        params = {"path": file_name, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload(self, file_path: str):
        file_name = file_path.split(sep='/')[-1]
        print(file_name)
        href = self._get_upload_link(file_name=file_name).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")