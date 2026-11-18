import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

a1 = "      if (e.hp <= 0) continue\n\n      // 铁墓：震击有冷却"
assert s.count(a1) == 1
s = s.replace(a1, """      if (e.hp <= 0) continue

      // 被萝莉闪避钉住的敌人：跳过本回合
      if (e.stun && e.stun > 0) {
        e.stun--
        log('「' + (e.name || '敌人') + '」被钉在原地，这一回合没动。')
        fx(e.x, e.y, '定身', '#ffc2dd', -0.4)
        continue
      }

      // 铁墓：震击有冷却""", 1)

a2 = "      log('你侧身躲开了。')"
assert s.count(a2) == 1
s = s.replace(a2, a2 + """
      // 萝莉专属：闪避成功时把攻击者钉在原地一回合
      if (S.hero.id === 'lily' && attacker && attacker.hp > 0) {
        attacker.stun = 1
        log('萝莉贴身一跃，「' + (attacker.name || '敌人') + '」被钉在原地一回合。')
        fx(attacker.x, attacker.y, '定身', '#ffc2dd', -0.5)
        shake(2.2, 120)
      }""", 1)

a3 = "desc: '娇小：闪避 28%、暴击 18%，6 项全能'"
assert s.count(a3) == 1
s = s.replace(a3, "desc: '娇小：闪避 28%，闪避成功把敌人钉住 1 回合'", 1)

io.open(p, "w", encoding="utf-8").write(s)
assert s.count("e.stun") >= 3
print("stun patch ok", len(s.encode()))
