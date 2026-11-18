import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

old = "{ id: 'lily', name: '萝莉', hp: 10, atk: 3, vision: 7, crit: .14, dodge: .22, potion: 1.3, desc: '小小只：闪避 22%，血薄但跑得快', icon: '铃', emoji: '🎀', color: '#ffc2dd', img: 'assets/hero-lily.webp', hidden: true, cost: 50 }"
assert s.count(old) == 1, s.count(old)
new = "{ id: 'lily', name: '萝莉', hp: 14, atk: 4, vision: 8, crit: .18, dodge: .28, potion: 1.6, desc: '娇小：闪避 28%、暴击 18%，6 项全能', icon: '铃', emoji: '🎀', color: '#ffc2dd', img: 'assets/hero-lily.webp', hidden: true, cost: 50 }"
s = s.replace(old, new, 1)
io.open(p, "w", encoding="utf-8").write(s)
print("ok", "hp: 14" in s)
