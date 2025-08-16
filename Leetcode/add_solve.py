import os
import sys
import shutil

def create_problem_folder(problem_id):
    # 루트 경로 기준
    base_dir = os.path.abspath(os.path.dirname(__file__))
    problems_dir = os.path.join(base_dir, "problems")
    example_dir = os.path.join(problems_dir, "_example")

    # 새 문제 폴더명 (lc0001 형식)
    folder_name = f"lc{int(problem_id):04d}"
    new_problem_dir = os.path.join(problems_dir, folder_name)

    # _example 폴더와 파일 유무 체크
    if not os.path.exists(example_dir):
        print(f"Error: Example folder not found at {example_dir}")
        return

    example_solution = os.path.join(example_dir, "solution.py")
    example_testcase = os.path.join(example_dir, "testcase.py")
    
    if not (os.path.isfile(example_solution) and os.path.isfile(example_testcase)):
        print(f"Error: Required example files not found in {example_dir}")
        return

    # 이미 문제 폴더가 존재할 경우 경고 후 종료
    if os.path.exists(new_problem_dir):
        print(f"Folder '{folder_name}' already exists under 'problems'. Aborting to avoid overwrite.")
        return

    # 폴더 생성 및 파일 복사
    os.makedirs(new_problem_dir)
    shutil.copy2(example_solution, os.path.join(new_problem_dir, "solution.py"))
    shutil.copy2(example_testcase, os.path.join(new_problem_dir, "testcase.py"))
    shutil.copy2(example_testcase, os.path.join(new_problem_dir, "__init__.py"))

    print(f"Problem folder created: {new_problem_dir}")
    print("Files copied: solution.py, testcase.py")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_folder.py <problem_number>")
        print("Example: python add_folder.py 0001")
    else:
        create_problem_folder(sys.argv[1])
