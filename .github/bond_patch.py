import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

a1 = "    { id: 'shell', name: '铁壳军团', members: ['ironshell', 'zero', 'ashen'], tiers: [{ n: 2, desc: '全队生命上限 +5' }, { n: 3, desc: '生命上限 +12、攻击 +1' }] },\n  ]"
assert s.count(a1) == 1
s = s.replace(a1, """    { id: 'shell', name: '铁壳军团', members: ['ironshell', 'zero', 'ashen'], tiers: [{ n: 2, desc: '全队生命上限 +5' }, { n: 3, desc: '生命上限 +12、攻击 +1' }] },
    { id: 'mortal', name: '凡尘行旅', members: ['murasame', 'mika', 'firefly', 'sparkle', 'taffy', 'trailblazer', 'march', 'danheng', 'zero', 'lily', 'nightwatch'], tiers: [{ n: 2, desc: '全队暴击 +8%' }, { n: 5, desc: '暴击 +16%、闪避 +10%、生命上限 +4' }] },
    { id: 'alien', name: '异种同盟', members: ['thanos', 'pig', 'nailong', 'fatcat', 'mimi', 'dem', 'ironshell', 'corn', 'whale', 'ashen'], tiers: [{ n: 2, desc: '全队攻击 +1' }, { n: 5, desc: '攻击 +2、生命上限 +8' }] },
  ]""", 1)

a2 = "    if (next.shell >= 3) wantHp += 12\n    else if (next.shell >= 2) wantHp += 5"
assert s.count(a2) == 1
s = s.replace(a2, a2 + """
    if (next.mortal >= 5) wantHp += 4
    if (next.alien >= 5) wantHp += 8""", 1)

a3 = "    if (next.shell >= 3) wantAtk += NUM(7)"
assert s.count(a3) == 1
s = s.replace(a3, a3 + """
    if (next.alien >= 5) wantAtk += NUM(3)
    else if (next.alien >= 2) wantAtk += NUM(7)""", 1)

a4 = "    if (next.deepsea >= 4) wantCrit += 0.12"
assert s.count(a4) == 1
s = s.replace(a4, a4 + """
    if (next.mortal >= 5) wantCrit += 0.16
    else if (next.mortal >= 2) wantCrit += 0.08""", 1)

a5 = "    if (next.deepsea >= 4) wantDodge += 0.25\n    else if (next.deepsea >= 2) wantDodge += 0.12"
assert s.count(a5) == 1
s = s.replace(a5, a5 + """
    if (next.mortal >= 5) wantDodge += 0.10""", 1)

a6 = "      if (sy.id === 'shell') { if (tier >= 3) { out.hp += 12; out.atk += 1 } else if (tier >= 2) out.hp += 5 }"
assert s.count(a6) == 1
s = s.replace(a6, a6 + """
      if (sy.id === 'mortal') { if (tier >= 5) { out.crit += 0.16; out.dodge += 0.10; out.hp += 4 } else if (tier >= 2) out.crit += 0.08 }
      if (sy.id === 'alien') { if (tier >= 5) { out.atk += 2; out.hp += 8 } else if (tier >= 2) out.atk += 1 }""", 1)

io.open(p, "w", encoding="utf-8").write(s)
assert s.count("mortal") >= 4 and s.count("alien") >= 5
print("bond patch ok", len(s.encode()))
