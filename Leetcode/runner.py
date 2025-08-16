import importlib
import sys
import argparse
import inspect
import re
import ast

def parse_raw_input(raw_input_line: str):
    """
    'Input: nums = [2,7,11,15], target = 9' 처럼 리트코드 스타일 입력 문자열을
    파이썬 딕셔너리 형태로 분해
    """
    # "Input:" 제거
    raw = raw_input_line.strip()
    if raw.lower().startswith("input:"):
        raw = raw[6:].strip()

    # 쉼표로 구분된 "키 = 값" 조각들 분리
    parts = re.split(r',(?![^\[]*\])', raw)  # 리스트 내 콤마 무시하며 분리
    input_dict = {}
    for part in parts:
        if '=' not in part:
            continue
        key, val_str = part.split('=', 1)
        key = key.strip()
        val_str = val_str.strip()
        try:
            # ast.literal_eval 로 문자열, 숫자, 리스트, dict 안전 파싱
            val = ast.literal_eval(val_str)
        except Exception:
            val = val_str  # 파싱실패시 그냥 문자열 그대로
        input_dict[key] = val
    return input_dict

def parse_raw_output(raw_output_line: str):
    """
    'Output: [0,1]' 등 출력 문자열을 파이썬 값으로 변환
    """
    raw = raw_output_line.strip()
    if raw.lower().startswith("output:"):
        raw = raw[7:].strip()
    try:
        val = ast.literal_eval(raw)
    except Exception:
        val = raw
    return val

def transform_testcases(raw_testcases):
    """
    리트코드 스타일 raw input-output 문자열 쌍들을
    runner.py에서 쓰는 testcases 리스트 구조로 변환
    """
    parsed = []
    for raw_case in raw_testcases:
        lines = [line.strip() for line in raw_case.split('\n') if line.strip()]
        input_line = next((l for l in lines if l.lower().startswith("input:")), None)
        output_line = next((l for l in lines if l.lower().startswith("output:")), None)
        if not input_line or not output_line:
            continue
        input_dict = parse_raw_input(input_line)
        output_val = parse_raw_output(output_line)
        parsed.append({"input": input_dict, "output": output_val})
    return parsed

def run(problem_id, solution_version=1):
    problem_module_name = f"problems.lc{problem_id:04d}.solution"
    test_module_name = f"problems.lc{problem_id:04d}.testcase"

    try:
        problem_module = importlib.import_module(problem_module_name)
    except ModuleNotFoundError:
        print(f"[에러] 문제 모듈 '{problem_module_name}'을(를) 찾을 수 없습니다. 폴더명과 파일명을 확인해주세요.")
        return
    except Exception as e:
        print(f"[에러] 문제 모듈 로딩 중 알 수 없는 오류가 발생했습니다: {e}")
        return

    try:
        test_module = importlib.import_module(test_module_name)
    except ModuleNotFoundError:
        print(f"[에러] 테스트 모듈 '{test_module_name}'을(를) 찾을 수 없습니다. testcase.py 파일이 존재하는지 확인해주세요.")
        return
    except Exception as e:
        print(f"[에러] 테스트 모듈 로딩 중 알 수 없는 오류가 발생했습니다: {e}")
        return

    classes = [cls for name, cls in inspect.getmembers(problem_module, inspect.isclass) if cls.__module__ == problem_module_name]

    class_name = 'Solution' if solution_version == 1 else f'Solution{solution_version}'
    solution_class = next((cls for cls in classes if cls.__name__ == class_name), None)
    if solution_class is None:
        print(f"[에러] 문제 모듈 내에 클래스 '{class_name}'을(를) 찾을 수 없습니다. 클래스 이름을 확인해 주세요.")
        return

    if not hasattr(test_module, 'raw_testcases'):
        print(f"[에러] '{test_module_name}'에 'raw_testcases' 리스트가 없습니다. testcase.py에 raw_testcases 변수를 정의해 주세요.")
        return

    raw_testcases = getattr(test_module, 'raw_testcases')
    testcases = transform_testcases(raw_testcases)

    solution = solution_class()

    funcs = [func for func in dir(solution) if callable(getattr(solution, func)) and not func.startswith("__")]

    if not funcs:
        print(f"[에러] 클래스 '{class_name}'에 호출 가능한 메서드가 없습니다. 문제 풀이 메서드를 작성해 주세요.")
        return

    # 첫 번째 Callable 메서드 실행
    method_name = funcs[0]
    method = getattr(solution, method_name)

    print(f"\nRunning Problem lc{problem_id:04d} | Using: {class_name}.{method_name}\n")

    for idx, case in enumerate(testcases, 1):
        inputs = case.get("input", {})
        expected = case.get("output", None)
        result = None
        try:
            # 풀이 함수 인자 형태에 맞게 입력 전달: **inputs 방식으로 unpacking
            result = method(**inputs)
            success = (result == expected)
            if not success:
                print(f"테스트 케이스 {idx} 실패: 출력값이 기대값과 다릅니다.")
        except TypeError as e:
            print(f"테스트 케이스 {idx}에서 TypeError가 발생했습니다.")
            print("▶ Solution 클래스 메서드 시그니처와 testcase 입력 변수를 확인해 주세요.")
            print(f"  오류 메시지: {e}")
            success = False
        except Exception as e:
            print(f"테스트 케이스 {idx}에서 예기치 못한 오류가 발생했습니다: {e}")
            success = False

        status = "✅ PASS" if success else "❌ FAIL"
        print(f"Test case {idx}:")
        print(f" Input: {inputs}")
        print(f" Output: {result}")
        print(f" Expected: {expected}")
        print(f" Result: {status}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run LeetCode problem tests.")
    parser.add_argument("problem_id", type=int, help="Problem number (e.g., 1 for lc0001)")
    parser.add_argument("--solution", type=int, default=1, help="Solution version to run (default: 1)")

    args = parser.parse_args()
    print("현재 Python 모듈 경로 목록(sys.path):")
    import os
    print(sys.path)
    run(args.problem_id, args.solution)
