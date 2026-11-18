import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

# 铁墓血量：基础公式 ×1.6（层数越高越耐打）
MUL = "1.6"
pairs = [
    ("var thp1 = NUM(0) + floor * NUM(1)", "var thp1 = Math.round((NUM(0) + floor * NUM(1)) * " + MUL + ")"),
    ("var thp2 = NUM(5) + floor * NUM(1)", "var thp2 = Math.round((NUM(5) + floor * NUM(1)) * " + MUL + ")"),
    ("var bhp = NUM(0) + floor * NUM(1)", "var bhp = Math.round((NUM(0) + floor * NUM(1)) * " + MUL + ")"),
    ("var thp = NUM(5) + floor * NUM(1)", "var thp = Math.round((NUM(5) + floor * NUM(1)) * " + MUL + ")"),
]
for old, new in pairs:
    assert s.count(old) == 1, old
    s = s.replace(old, new, 1)

io.open(p, "w", encoding="utf-8").write(s)
assert s.count("* 1.6)") == 4
print("boss hp buffed, 4 spots")
