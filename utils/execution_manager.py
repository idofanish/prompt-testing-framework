from pathlib import Path
from utils.test_scenario_loader import load_all_yaml_test_scenarios
from utils.testcase_executor import execute_testcase

DIR = Path(__file__).resolve().parent.parent / "tests"


def manage_execution() -> str:
    """Manages the execution of a logic.
    Returns:
        str: The execution status[TBD]
    """

    test_cases = load_all_yaml_test_scenarios()
    print(f"Count of test cases loaded: {len(test_cases)}.")
    print("Running local model for each test case...\n")
    # Iterate through each test case and run the local model
    # Note: This assumes that the test cases have a 'prompt' key and optionally a 'model' key
    # If 'model' is not specified, it defaults to 'distilgpt2'

    for i, test_case in enumerate(test_cases, 1):
        model_name = test_case.get("model", "distilgpt2")
        prompt = test_case["prompt"]
        print(f"\nTest {i}: {test_case['id']} - {test_case['title']}")
        print(f"Model: {model_name}")
        response = execute_testcase(model_name, prompt)
        print(f"Model Response:\n\n{response}\n{'-'*60}")
