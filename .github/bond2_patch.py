import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

a1 = "tiers: [{ n: 2, desc: '全队攻击 +1' }, { n: 5, desc: '攻击 +2、生命上限 +8' }] },\n  ]"
assert s.count(a1) == 1
s = s.replace(a1, """tiers: [{ n: 2, desc: '全队攻击 +1' }, { n: 5, desc: '攻击 +2、生命上限 +8' }] },
    { id: 'bulwark', name: '铁壁同盟', members: ['ironshell', 'ashen', 'thanos', 'whale', 'dem', 'corn'], tiers: [{ n: 2, desc: '全队生命上限 +6' }, { n: 3, desc: '生命上限 +12、攻击 +1' }] },
    { id: 'gale', name: '疾影组', members: ['mimi', 'lily', 'zero', 'sparkle', 'taffy', 'nightwatch'], tiers: [{ n: 2, desc: '全队闪避 +10%' }, { n: 3, desc: '闪避 +18%、暴击 +8%' }] },
    { id: 'fireline', name: '火力组', members: ['murasame', 'mika', 'firefly', 'nailong', 'fatcat', 'pig'], tiers: [{ n: 2, desc: '全队攻击 +1' }, { n: 3, desc: '攻击 +2、暴击 +10%' }] },
    { id: 'starcall', name: '星轨残响', members: ['trailblazer', 'march', 'danheng', 'whale', 'zero', 'ashen'], tiers: [{ n: 2, desc: '全队生命上限 +2、攻击 +1' }, { n: 3, desc: '生命上限 +6、攻击 +1、暴击 +6%' }] },
  ]""", 1)

a2 = "    if (next.alien >= 5) wantHp += 8"
assert s.count(a2) == 1
s = s.replace(a2, a2 + """
    if (next.bulwark >= 3) wantHp += 12
    else if (next.bulwark >= 2) wantHp += 6
    if (next.starcall >= 3) wantHp += 6
    else if (next.starcall >= 2) wantHp += 2""", 1)

a3 = "    else if (next.alien >= 2) wantAtk += NUM(7)"
assert s.count(a3) == 1
s = s.replace(a3, a3 + """
    if (next.fireline >= 3) wantAtk += NUM(3)
    else if (next.fireline >= 2) wantAtk += NUM(7)
    if (next.bulwark >= 3) wantAtk += NUM(7)
    if (next.starcall >= 2) wantAtk += NUM(7)""", 1)

a4 = "    else if (next.mortal >= 2) wantCrit += 0.08"
assert s.count(a4) == 1
s = s.replace(a4, a4 + """
    if (next.gale >= 3) wantCrit += 0.08
    if (next.fireline >= 3) wantCrit += 0.10
    if (next.starcall >= 3) wantCrit += 0.06""", 1)

a5 = "    if (next.mortal >= 5) wantDodge += 0.10"
assert s.count(a5) == 1
s = s.replace(a5, a5 + """
    if (next.gale >= 3) wantDodge += 0.18
    else if (next.gale >= 2) wantDodge += 0.10""", 1)

a6 = "      if (sy.id === 'alien') { if (tier >= 5) { out.atk += 2; out.hp += 8 } else if (tier >= 2) out.atk += 1 }"
assert s.count(a6) == 1
s = s.replace(a6, a6 + """
      if (sy.id === 'bulwark') { if (tier >= 3) { out.hp += 12; out.atk += 1 } else if (tier >= 2) out.hp += 6 }
      if (sy.id === 'gale') { if (tier >= 3) { out.dodge += 0.18; out.crit += 0.08 } else if (tier >= 2) out.dodge += 0.10 }
      if (sy.id === 'fireline') { if (tier >= 3) { out.atk += 2; out.crit += 0.10 } else if (tier >= 2) out.atk += 1 }
      if (sy.id === 'starcall') { if (tier >= 3) { out.hp += 6; out.atk += 1; out.crit += 0.06 } else if (tier >= 2) { out.hp += 2; out.atk += 1 } }""", 1)

io.open(p, "w", encoding="utf-8").write(s)
assert "bulwark" in s and "starcall" in s
print("bond2 ok", len(s.encode()))
