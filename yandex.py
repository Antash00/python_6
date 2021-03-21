import requests

token = input()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
            resp = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params={'path': file_path},
                                headers={'Authorization': f'OAuth {self.token}'})
            return resp.json()


uploader = YaUploader(token)
result = uploader.upload('1.txt')
print(result)
