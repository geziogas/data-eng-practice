import yaml
import argparse

def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

# def filter_people(people, min_age):
#     return [p for p in people if p["age"] >= min_age]

def filter_people(people, min_age):
    filtered = []
    for p in people:
        age = p.get("age")
        if age is None:
            print(f"Skipping {p['name']}: age is missing.")
            continue
        if age >= min_age:
            filtered.append(p)
    return filtered

def main():
    parser = argparse.ArgumentParser(description="Filter people by minimum age.")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config file")
    args = parser.parse_args()

    config = load_config(args.config)
    people = config["input_data"]
    min_age = config["filters"]["min_age"]
    filtered = filter_people(people, min_age)

    print("Filtered people:")
    for person in filtered:
        print(f"{person['name']} ({person['age']})")

if __name__ == "__main__":
    main()