from functions.get_file_content import get_file_content

def run_tests():
    print(f"Running test on \"main.py\"...")
    print(get_file_content("calculator", "main.py") + "\n")
    print(f"Running test on \"pkg/calculator.py\"...")
    print(get_file_content("calculator", "pkg/calculator.py") + "\n")
    print(f"Running test on \"/bin/cat\"...")
    print(get_file_content("calculator", "/bin/cat") + "\n")
    print(f"Running test on \"pkg/does_not_exist.py\"...")
    print(get_file_content("calculator", "pkg/does_not_exist.py") + "\n")

if __name__ == "__main__":
    run_tests()