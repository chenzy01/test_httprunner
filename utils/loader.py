import yaml


def load_yaml(yml_file):
    with open(yml_file, "r") as f:
        loaded_json = yaml.load(f.read())
    return loaded_json
