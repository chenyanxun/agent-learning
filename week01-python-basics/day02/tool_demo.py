"""
Day 2 示例：Agent 工具的 Python 类

对照 TS 接口：
  interface Tool { name: string; description: string; run(args): dict; }
"""


class Tool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def schema(self) -> dict:
        return {"name": self.name, "description": self.description}

    def run(self, **kwargs) -> dict:
        raise NotImplementedError


class SearchNotesTool(Tool):
    def __init__(self):
        super().__init__(
            name="search_notes",
            description="Search local notes by keyword",
        )
        self._notes = [
            {"id": 1, "text": "Agent loop: observe think act"},
            {"id": 2, "text": "RAG retrieves documents then generates"},
        ]

    def run(self, query: str = "", limit: int = 3) -> dict:
        query_lower = query.lower()
        hits = [n for n in self._notes if query_lower in n["text"].lower()][:limit]
        return {"ok": True, "count": len(hits), "results": hits}


if __name__ == "__main__":
    tool = SearchNotesTool()
    print("schema:", tool.schema())
    print("run:", tool.run(query="agent"))
