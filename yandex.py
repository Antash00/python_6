import requests

token = 'AgAAAAATdS1xAADLWzHrhreCWkdanreXl-ZdUQE'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
            resp = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params={'path': file_path},
                                headers={'Authorization': f'OAuth {self.token}'})
            result = resp.json()
            if 'href' in result:
                response = requests.put(result['href'], params={'path': file_path})
                return response.json()
            else:
                return result


uploader = YaUploader(token)
result = uploader.upload('1.txt')
print(result)
