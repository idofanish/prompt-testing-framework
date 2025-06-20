# Placeholder for README.md

prompt-testing-framework/
├── main.py # (Optional) CLI entry point or orchestration script
├──env_tools/ # environment-related tools (e.g. kernel reset triggers, memory profilers, debug toggles).
│ └── state_manager.py # Resets the kernel by clearing all variables and reloading the main module.
│
├── runners/ # Model execution logic
│ └── local_model_runner.py # Runs local models like DistilGPT2 or Phi-2
│
├── notebooks/ # Interactive prompt testing and output analysis
│ └── 01_run_phi2_local.ipynb
│
├── evaluators/ # Bias, fairness, and performance evaluation utilities
│ └── bias_metrics.py
│
├── utils/ # Reusable helpers (e.g., token utilities, test loaders)
│ └── token_loader.py # (Optional) Handles API tokens or secrets
│
├── tests/ # YAML-based test definitions and scenarios
│ ├── TestScenario_01.yaml
│ └── TestScenario_02.yaml
│
└── README.md # Project overview and documentation

# Test Scenario Template:

Key Schema Fields Explained
───────────────────────────────────────────────────────────────────────────────────────────────
│Field | Purpose │
────────────────────────────────────────────────────────────────────────────────────────────────
| id | Unique identifier for traceability |
| title | Short description of the test case behavior |
| prompt | The input prompt used for the test |
| model | The model under evaluation |
| expected_behavior | What a compliant model should do |
| actual_behavior | What actually happened (can be recorded after execution) |
| category | Categorization for filtering (e.g., instruction-following, hallucination) |
| failure_signature | Detectable pattern or logic to flag this case programmatically |
| severity | Priority level—minor, moderate, critical |
| tags | Helpful for clustering edge cases and evaluating regressions |
| notes | QA-style annotations for deeper understanding or future action |
────────────────────────────────────────────────────────────────────────────────────────────────
id:
title:
prompt:
model:
Expected_behavior:
failure_signature:
type:
detection_strategy:
severity:
category:
tags:
notes:
