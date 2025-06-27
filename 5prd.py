import json

def load_json_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

        if isinstance(data, dict):
            data = data.get("relationships_following", [])
        if isinstance(data, list) and isinstance(data[0], str):
            return data
        return [entry['string_list_data'][0]['value'] for entry in data]


def compare_followers_and_following(followers_list, following_list):
    followers_set = set(followers_list)
    following_set = set(following_list)

    not_following_back = following_set - followers_set
    not_followed_by_you = followers_set - following_set

    print("\nLietotāji, kuriem tu seko, bet viņi tev neseko:")
    for user in sorted(not_following_back):
        print(" -", user)
    print("\nLietotāji, kuri tev seko, bet tu viņiem neseko:")
    for user in sorted(not_followed_by_you):
        print(" -", user)
    print("\n")
    
if __name__ == "__main__":
    following = load_json_list("following_1.json")
    followers = load_json_list("followers_1.json")
    compare_followers_and_following(followers, following)

#  python 5prd.py <----ievadīt terminālī