import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

# 1) 新增两组羁绊数据
anchor = "    { id: 'train', name: '星穹列车组', members: ['trailblazer', 'march', 'danheng'], tiers: [{ n: 2, desc: '全队攻击 +1' }, { n: 3, desc: '攻击 +2、暴击 +10%' }] },\n  ]"
assert s.count(anchor) == 1, "synergy anchor"
new_groups = """    { id: 'train', name: '星穹列车组', members: ['trailblazer', 'march', 'danheng'], tiers: [{ n: 2, desc: '全队攻击 +1' }, { n: 3, desc: '攻击 +2、暴击 +10%' }] },
    { id: 'deepsea', name: '深海方舟', members: ['whale', 'nightwatch', 'corn', 'lily'], tiers: [{ n: 2, desc: '全队闪避 +12%' }, { n: 4, desc: '闪避 +25%、暴击 +12%' }] },
    { id: 'shell', name: '铁壳军团', members: ['ironshell', 'zero', 'ashen'], tiers: [{ n: 2, desc: '全队生命上限 +5' }, { n: 3, desc: '生命上限 +12、攻击 +1' }] },
  ]"""
s = s.replace(anchor, new_groups, 1)

# 2) P1 主计算：生命
hp_anchor = """    var wantHp = 0
    if (next.chaos >= 2) wantHp += 5
    if (next.chaos >= 4) wantHp += 10"""
assert s.count(hp_anchor) == 1
s = s.replace(hp_anchor, hp_anchor + "\n    if (next.shell >= 3) wantHp += 12\n    else if (next.shell >= 2) wantHp += 5", 1)

# 3) 攻击
atk_anchor = "    var wantAtk = next.train >= 3 ? NUM(9) : next.train >= 2 ? NUM(7) : 0"
assert s.count(atk_anchor) == 1
s = s.replace(atk_anchor, atk_anchor + "\n    if (next.shell >= 3) wantAtk += NUM(7)", 1)

# 4) 暴击
crit_anchor = """    var wantCrit = next.otaku >= 3 ? 0.30 : next.otaku >= 2 ? 0.15 : 0
    if (next.train >= 3) wantCrit += NUM(8) / 100"""
assert s.count(crit_anchor) == 1
s = s.replace(crit_anchor, crit_anchor + "\n    if (next.deepsea >= 4) wantCrit += 0.12", 1)

# 5) 闪避
dodge_anchor = "    var wantDodge = next.abyss >= 2 ? 0.15 : 0"
assert s.count(dodge_anchor) == 1
s = s.replace(dodge_anchor, dodge_anchor + "\n    if (next.deepsea >= 4) wantDodge += 0.25\n    else if (next.deepsea >= 2) wantDodge += 0.12", 1)

# 6) P2 计算
p2_anchor = "      if (sy.id === 'train') out.atk += tier >= 3 ? 2 : tier >= 2 ? 1 : 0"
assert s.count(p2_anchor) == 1
s = s.replace(p2_anchor, p2_anchor + "\n      if (sy.id === 'deepsea') { out.dodge += tier >= 4 ? 0.25 : tier >= 2 ? 0.12 : 0; if (tier >= 4) out.crit += 0.12 }\n      if (sy.id === 'shell') { if (tier >= 3) { out.hp += 12; out.atk += 1 } else if (tier >= 2) out.hp += 5 }", 1)

io.open(p, "w", encoding="utf-8").write(s)
for k in ["'deepsea'", "'shell'", "wantDodge += 0.25"]:
    assert k in s, k
print("patch ok, bytes:", len(s.encode()))
