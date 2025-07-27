from functions.get_files_info import get_files_info

def run_tests():
    print("Running tests on \".\" as directory.")
    print(get_files_info("calculator", ".") + "\n")

    print("Running tests on \"pkg\" as directory.")
    print(get_files_info("calculator", "pkg") + "\n") 

    print("Running tests on \"/bin\" as directory.")
    print(get_files_info("calculator", "/bin") + "\n")

    print("Running tests on \"../\" as directory.")
    print(get_files_info("calculator", "../") + "\n")

    print(f"All tests complete")

if __name__ == "__main__":
    run_tests()