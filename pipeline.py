import yaml
import argparse
import csv

def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

# def filter_people(people, min_age):
#     return [p for p in people if p["age"] >= min_age]

def filter_people(people, min_age):
    return [p for p in people if p.get("age", 0) >= min_age]

def load_people_from_csv(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        people = []
        for row in reader:
            try:
                name = row["name"]
                age = int(row["age"]) if row["age"] else None
                if age is not None:
                    people.append({"name": name, "age": age})
            except Exception as e:
                print(f"Skipping row due to error: {row} - {e}")
        return people

def write_people_to_csv(people, path):
    with open(path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(people)

# def filter_people(people, min_age):
#     filtered = []
#     for p in people:
#         age = p.get("age")
#         if age is None:
#             print(f"Skipping {p['name']}: age is missing.")
#             continue
#         if age >= min_age:
#             filtered.append(p)
#     return filtered

def main():
    parser = argparse.ArgumentParser(description="Filter people by minimum age.")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config file")
    parser.add_argument("--input", type=str, default="input.csv")
    parser.add_argument("--output", type=str, default="output.csv")
    args = parser.parse_args()

    config = load_config(args.config)
    # people = config["input_data"]
    min_age = config["filters"]["min_age"]
    # filtered = filter_people(people, min_age)

    # print("Filtered people:")
    # for person in filtered:
    #     print(f"{person['name']} ({person['age']})")

    people = load_people_from_csv(args.input)
    filtered = filter_people(people, min_age)

    write_people_to_csv(filtered, args.output)
    print(f"Filtered {len(filtered)} people. Output written to {args.output}")

if __name__ == "__main__":
    main()