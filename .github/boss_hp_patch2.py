import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

pairs = [
    ("var thp1 = NUM(0) + floor * NUM(1)", "var thp1 = Math.round((NUM(0) + floor * NUM(1)) * 1.6)"),
    ("var thp2 = NUM(5) + floor * NUM(1)", "var thp2 = Math.round((NUM(5) + floor * NUM(1)) * 1.6)"),
    ("var bhp = NUM(0) + floor * NUM(1)", "var bhp = Math.round((NUM(0) + floor * NUM(1)) * 1.6)"),
    ("var thp = NUM(5) + floor * NUM(1)", "var thp = Math.round((NUM(5) + floor * NUM(1)) * 1.6)"),
]
for old, new in pairs:
    assert s.count(old) == 1, old
    s = s.replace(old, new, 1)

io.open(p, "w", encoding="utf-8").write(s)
assert s.count("Math.round((NUM") == 4
print("boss hp buffed, 4 spots")
