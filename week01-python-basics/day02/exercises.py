"""
Day 2 练习 —— 运行:
  ..\.venv\Scripts\python.exe day02/exercises.py
"""


def exercise_1_first_and_last(items: list) -> tuple:
    """返回 (第一个元素, 最后一个元素)。"""
    # TODO
    raise NotImplementedError


def exercise_2_word_count(text: str) -> dict:
    """统计每个单词出现次数。"""
    # TODO
    raise NotImplementedError


def exercise_3_merge_tool_results(results: list) -> list:
    """合并多个工具返回的 list，去掉空 list。"""
    # TODO
    raise NotImplementedError


def exercise_4_get_trace_step(traces: list, step: int) -> dict:
    """从 trace 列表里找指定 step，找不到返回 {}。"""
    # TODO
    raise NotImplementedError


def exercise_5_tool_names(tools: list) -> list:
    """从工具 dict 列表中提取 name 字段。"""
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    assert exercise_1_first_and_last(["a", "b", "c"]) == ("a", "c")
    assert exercise_2_word_count("agent agent loop") == {"agent": 2, "loop": 1}
    assert exercise_3_merge_tool_results([[1, 2], [], [3]]) == [1, 2, 3]
    assert exercise_4_get_trace_step(
        [{"step": 1, "tool": "search"}, {"step": 2, "tool": "write"}], 2
    ) == {"step": 2, "tool": "write"}
    assert exercise_4_get_trace_step([], 1) == {}
    assert exercise_5_tool_names([{"name": "search"}, {"name": "write"}]) == [
        "search",
        "write",
    ]
    print("[OK] Day 2 全部练习通过！")
