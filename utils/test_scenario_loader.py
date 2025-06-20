import yaml
from pathlib import Path
import os

FILE_DIR = Path(__file__).resolve().parent.parent / "tests"


def load_yaml_test_scenario(filename="TestScenario_011.yaml"):
    """
    Load test cases from a specific YAML file in the 'tests/' directory.
    """

    file_path = FILE_DIR / filename
    print(f"Loading all test cases from the YAML file in {file_path}")
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        if not isinstance(data, list):
            raise ValueError(f"Expected a list of test cases, got {type(data)}")
        return data


def load_all_yaml_test_scenarios():
    """
    Load and merge all test cases from YAML files in the 'tests/' directory.
    """
    all_cases = []
    print(f"Searching test scenarios YAML files in: {FILE_DIR}")
    has_yaml = any(FILE_DIR.glob("*.yaml"))
    if has_yaml:
        for file in sorted(FILE_DIR.glob("*.yaml")):
            try:
                print(f"Processing file: {file.name}")
                # Read and parse the YAML file
                with open(file, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if isinstance(data, list):
                        all_cases.extend(data)
                    else:
                        print(
                            f"Skipping {file.name}: expected a list, got {type(data)}"
                        )
            except yaml.YAMLError as e:
                print(f"YAML error in {file.name}: {e}")
            except Exception as e:
                print(f" Error processing {file.name}: {e}")
        if all_cases:
            print(f"Successfully loaded {len(all_cases)} test cases from YAML files.")
        else:
            print("No valid test cases found in the YAML files.")
    else:
        print("No YAML files found.")

    return all_cases
