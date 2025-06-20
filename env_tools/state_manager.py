from pathlib import Path

DIR = Path(__file__).resolve().parent.parent / "env_tools"



def reset_test_state(vars_to_clear, globals_dict):
    """
    Clears specified variables from the global namespace.

    Args:
        vars_to_clear (list): List of variable names as strings.
        globals_dict (dict): Typically passed as globals()

    Example:
        reset_test_state(["response", "result", "test_case"], globals())
    """
    cleared = []
    for var in vars_to_clear:
        if var in globals_dict:
            del globals_dict[var]
            cleared.append(var)
    if cleared:
        print(f"Cleared: {', '.join(cleared)}")
    else:
        print("No matching variables to clear.")


def reset_kernel():
    """
    Example usage:
    reset_test_state(["response", "result", "test_case"], globals())
    reset_kernel()
    Resets the kernel by clearing all variables and reloading the main module.
    This is useful for starting fresh without restarting the entire notebook kernel.

    """
    import sys
    import os
    import importlib

    # Clear all variables in the global namespace
    reset_test_state(list(globals().keys()), globals())

    # Reload the main module (if applicable)
    if "main" in sys.modules:
        import main

        importlib.reload(main)
        print(" Reloaded main module.")

    print("Kernel reset complete. Ready for a fresh start!")
