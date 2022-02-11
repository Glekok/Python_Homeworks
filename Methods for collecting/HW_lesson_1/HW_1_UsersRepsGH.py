import requests
import json


user_name = input(str("Для кого ищем список репозиториев? >>> "))

URL_LIST_OF_REPS = f"https://api.github.com/users/{user_name}/repos"


def get_list_of_reps(response):
    repos = []

    for data in response:
        if "id" in data:
            repos.append(data["full_name"])
        else:
            print("Wrong user! Try again...")
            break

    return repos


if __name__ == "__main__":
    r = requests.get(URL_LIST_OF_REPS)
    r_json = r.json()
    with open(file=f"{user_name}_repos", mode="w") as file:
        json.dump(r.json(), file)
    list_of_reps = get_list_of_reps(r_json)
    print(f'{user_name} has {len(list_of_reps)} repositories >>> {list_of_reps}')
