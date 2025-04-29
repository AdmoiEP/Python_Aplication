import requests

# URL для API GitHub (публичный репозиторий)
repo_url = "https://api.github.com/repos/AdmoiEP/First_step"

# Делаем GET-запрос
response = requests.get(repo_url)

# Проверяем статус ответа
if response.status_code == 200:
    repo_data = response.json()
    print("Информация о репозитории:")
    print(f"Название: {repo_data['name']}")
    print(f"Владелец: {repo_data['owner']['login']}")
    print(f"Описание: {repo_data.get('description', 'нет описания')}")
    print(f"Звёзды: {repo_data['stargazers_count']}")
    print(f"Форки: {repo_data['forks_count']}")
    print(f"URL: {repo_data['html_url']}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())  # GitHub обычно возвращает JSON с описанием ошибки