import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

anchor = "    { id: 'dem', name: '德谬歌', hp: 16, atk: 5, vision: 4, crit: .2, dodge: 0, potion: .8, desc: '重量：攻高血厚，但看不远', icon: '德', emoji: '🌑', color: '#b9a0ff', hidden: true, cost: 35 }\n  ]"
assert s.count(anchor) == 1, "anchor not unique"

new = """    { id: 'dem', name: '德谬歌', hp: 16, atk: 5, vision: 4, crit: .2, dodge: 0, potion: .8, desc: '重量：攻高血厚，但看不远', icon: '德', emoji: '🌑', color: '#b9a0ff', hidden: true, cost: 35 },
    { id: 'nightwatch', name: '守夜人', hp: 16, atk: 3, vision: 8, crit: .10, dodge: .05, potion: 1.0, desc: '提灯：视野 8，血量 16', icon: '夜', emoji: '🕯️', color: '#8fc7ff' },
    { id: 'ironshell', name: '铁壳母鸡', hp: 20, atk: 2, vision: 5, crit: .05, dodge: 0, potion: 1.0, desc: '铁壳：血 20，全场最耐打', icon: '壳', emoji: '🐔', color: '#f0c659' },
    { id: 'corn', name: '玉米粒', hp: 12, atk: 4, vision: 6, crit: .15, dodge: .08, potion: 1.45, desc: '补给：药水 ×1.45，攻 4', icon: '粒', emoji: '🌽', color: '#e8b84b' },
    { id: 'whale', name: '深海鲸', hp: 15, atk: 4, vision: 7, crit: .10, dodge: 0, potion: 1.0, desc: '回声：视野 7、攻 4，血厚实', icon: '鲸', emoji: '🐋', color: '#39d0e8' },
    { id: 'zero', name: '超频零', hp: 11, atk: 5, vision: 6, crit: .22, dodge: .05, potion: 1.0, desc: '超频：攻 5、暴击 22%，血很薄', icon: '零', emoji: '⚡', color: '#7de2ff' },
    { id: 'ashen', name: '灰烬', hp: 13, atk: 3, vision: 6, crit: .10, dodge: .10, potion: 1.6, desc: '灰烬：闪避 10%，药水 ×1.6', icon: '灰', emoji: '🌫️', color: '#a9b3c7' }
  ]"""

s = s.replace(anchor, new, 1)
s = s.replace("14 位跨次元角色可选", "20 位跨次元角色可选", 1)
io.open(p, "w", encoding="utf-8").write(s)

import re
ids = re.findall(r"id: '([^']+)'", s[s.find("var HEROES") : s.find("var RELICS")])
print("heroes:", len(ids))
assert len(ids) == 20, len(ids)
