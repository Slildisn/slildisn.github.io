import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

old = "{ id: 'lily', name: '铃兰'"
assert s.count(old) == 1, s.count(old)
new = "{ id: 'lily', name: '萝莉'"
s = s.replace(old, new, 1)
io.open(p, "w", encoding="utf-8").write(s)
assert "name: '萝莉'" in s
print("renamed ok")
