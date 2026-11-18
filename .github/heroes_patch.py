import io, re

p = "game.html"
s = io.open(p, encoding="utf-8").read()

anchor = "    { id: 'ashen', name: '灰烬', hp: 13, atk: 3, vision: 6, crit: .10, dodge: .10, potion: 1.6, desc: '灰烬：闪避 10%，药水 ×1.6', icon: '灰', emoji: '🌫️', color: '#a9b3c7' }\n  ]"
assert s.count(anchor) == 1, "anchor not unique"

new = """    { id: 'ashen', name: '灰烬', hp: 13, atk: 3, vision: 6, crit: .10, dodge: .10, potion: 1.6, desc: '灰烬：闪避 10%，药水 ×1.6', icon: '灰', emoji: '🌫️', color: '#a9b3c7' },
    { id: 'lily', name: '铃兰', hp: 10, atk: 3, vision: 7, crit: .14, dodge: .22, potion: 1.3, desc: '小小只：闪避 22%，血薄但跑得快', icon: '铃', emoji: '🎀', color: '#ffc2dd' }
  ]"""

s = s.replace(anchor, new, 1)
s = s.replace("20 位跨次元角色可选", "21 位跨次元角色可选", 1)
io.open(p, "w", encoding="utf-8").write(s)

seg = s[s.find("var HEROES") : s.find("var RELICS")]
ids = re.findall(r"id: '([^']+)'", seg)
print("heroes:", len(ids), ids[-3:])
assert len(ids) == 21, len(ids)
