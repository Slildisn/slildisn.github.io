import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

old = "{ id: 'lily', name: '萝莉', hp: 10, atk: 3, vision: 7, crit: .14, dodge: .22, potion: 1.3, desc: '小小只：闪避 22%，血薄但跑得快', icon: '铃', emoji: '🎀', color: '#ffc2dd', img: 'assets/hero-lily.webp' }"
assert s.count(old) == 1, s.count(old)
new = "{ id: 'lily', name: '萝莉', hp: 10, atk: 3, vision: 7, crit: .14, dodge: .22, potion: 1.3, desc: '小小只：闪避 22%，血薄但跑得快', icon: '铃', emoji: '🎀', color: '#ffc2dd', img: 'assets/hero-lily.webp', hidden: true, cost: 50 }"
s = s.replace(old, new, 1)
io.open(p, "w", encoding="utf-8").write(s)

import re
seg = s[s.find("var HEROES") : s.find("var RELICS")]
for line in re.findall(r"\{ id: '([^']+)'.*?\}", seg):
    pass
print("hidden+cost 50 ok", "hidden: true, cost: 50" in s)
