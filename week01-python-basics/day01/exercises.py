"""
Day 1 练习 —— 运行（在 week01-python-basics 目录）:
  ..\.venv\Scripts\python.exe day01/exercises.py
"""


def exercise_1_greet(name: str) -> str:
    """返回 f"Hello, {name}!"

    TS 等价: function greet(name: string): string { return `Hello, ${name}!`; }
    """
    return f"Hello, {name}!"


def exercise_2_sum(nums: list) -> int:
    """返回列表元素之和。

    TS 等价: nums.reduce((a, b) => a + b, 0)
    """
    return sum(nums)


def exercise_3_filter_evens(nums: list) -> list:
    """返回所有偶数。

    TS 等价: nums.filter(x => x % 2 === 0)
    """
    return [x for x in nums if x % 2 == 0]


def exercise_4_tool_schema() -> dict:
    """返回一个工具 schema dict（Agent 里天天用）。"""
    return {
        "name": "search_notes",
        "description": "Search local notes by keyword",
        "parameters": {"query": "string"},
    }


def exercise_5_read_json_shape() -> dict:
    """模拟 Agent trace 的一条记录。"""
    return {
        "step": 1,
        "tool": "search_notes",
        "args": {"query": "agent loop"},
        "ok": True,
    }


if __name__ == "__main__":
    assert exercise_1_greet("World") == "Hello, World!"
    assert exercise_2_sum([1, 2, 3, 4]) == 10
    assert exercise_3_filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    schema = exercise_4_tool_schema()
    assert schema["name"] == "search_notes"
    assert "query" in schema["parameters"]

    trace = exercise_5_read_json_shape()
    assert trace["step"] == 1 and trace["ok"] is True

    print("[OK] Day 1 全部练习通过！")
