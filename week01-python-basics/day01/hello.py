"""Day 1: 第一个 Python 脚本 —— 对照 TypeScript 阅读注释。"""

# TS: const name: string = "Agent"
name = "Agent"

# TS: console.log(`Hello, ${name}!`)
print(f"Hello, {name}!")

# TS: const nums = [1, 2, 3]; nums.map(x => x * 2)
nums = [1, 2, 3]
doubled = [x * 2 for x in nums]
print("doubled:", doubled)

# TS: interface User { name: string; role: string }
# Python 用 dict 很常见（后面会学 TypedDict / Pydantic）
user = {"name": "前端开发者", "role": "learner"}
print(f"用户: {user['name']}, 角色: {user['role']}")
