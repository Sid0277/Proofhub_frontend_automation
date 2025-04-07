# # run_tests.py
# import pytest
#
# if __name__ == "__main__":
#     # Run specific test cases in sequence
#     pytest.main([
#         # "tests/test_login.py::test_valid_login",
#         "tests/test_signup.py::test_valid_signup"
#         # "tests/test_profile.py::test_edit_profile",
#         # "-v",  # Verbose output
#         # "--order-dependencies",  # Ensure order is maintained
#     ])


import pytest


def run_selected_tests(test_cases):
    """Run selected test cases dynamically."""
    pytest_args = ["-v", "--html=report.html"]

    for test in test_cases:
        pytest_args.append(f"tests/{test}.py")

    pytest.main(pytest_args)


if __name__ == "__main__":
    # Select test cases to run
    # selected_tests = ["test_signup", "test_login"]  # Modify this list as needed
    selected_tests = ["test_signup"]  # Modify this list as needed
    run_selected_tests(selected_tests)
