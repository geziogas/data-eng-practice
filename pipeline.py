import yaml

def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def filter_people(people, min_age):
    return [p for p in people if p["age"] >= min_age]

if __name__ == "__main__":
    config = load_config()
    people = config["input_data"]
    min_age = config["filters"]["min_age"]
    filtered = filter_people(people, min_age)
    print("Filtered people:")
    for person in filtered:
        print(f"{person['name']} ({person['age']})")
