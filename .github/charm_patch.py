import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

old1 = """      // 被萝莉闪避钉住的敌人：跳过本回合
      if (e.stun && e.stun > 0) {
        e.stun--
        log('「' + (e.name || '敌人') + '」被钉在原地，这一回合没动。')
        fx(e.x, e.y, '定身', '#ffc2dd', -0.4)
        continue
      }"""
assert s.count(old1) == 1
new1 = """      // 被萝莉魅惑的小怪：这一回合改为攻击最近的同伴
      if (e.charm && e.charm > 0) {
        e.charm--
        var chT = null, chD = 9999
        for (var ci = 0; ci < S.enemies.length; ci++) {
          var ce = S.enemies[ci]
          if (ce === e || ce.hp <= 0) continue
          var cd = Math.abs(ce.x - e.x) + Math.abs(ce.y - e.y)
          if (cd < chD) { chD = cd; chT = ce }
        }
        if (chT) {
          var chDmg = Math.max(1, e.atk)
          chT.hp -= chDmg
          fx(chT.x, chT.y, '-' + chDmg, '#ffb3d9', -0.4)
          log('「' + (e.name || '小怪') + '」被萝莉迷了眼，转身砍向「' + (chT.name || '同伴') + '」。')
          S.impact = { x: chT.x, y: chT.y, t: Date.now(), color: '#ffb3d9' }
          if (chT.hp <= 0) killEnemy(chT, teamOf('p1')[0])
          continue
        }
        log('「' + (e.name || '小怪') + '」找不到同伴，原地发愣。')
        continue
      }"""
s = s.replace(old1, new1, 1)

old2 = """      // 萝莉专属：闪避成功时把攻击者钉在原地一回合
      if (S.hero.id === 'lily' && attacker && attacker.hp > 0) {
        attacker.stun = 1
        log('萝莉贴身一跃，「' + (attacker.name || '敌人') + '」被钉在原地一回合。')
        fx(attacker.x, attacker.y, '定身', '#ffc2dd', -0.5)
        shake(2.2, 120)
      }"""
assert s.count(old2) == 1
new2 = """      // 萝莉专属：闪避成功时魅惑那只小怪，让它下一回合反打同伴
      if (S.hero.id === 'lily' && attacker && attacker.hp > 0) {
        if (attacker.type === 'tomb' || attacker.type === 'dick') {
          log('萝莉的魅惑对「' + (attacker.name || 'BOSS') + '」无效。')
        } else {
          attacker.charm = 1
          log('萝莉飞了个吻，「' + (attacker.name || '小怪') + '」眼神变了——下回合它会打自己人。')
          fx(attacker.x, attacker.y, '魅惑', '#ffb3d9', -0.5)
          shake(2.2, 120)
        }
      }"""
s = s.replace(old2, new2, 1)

old3 = "desc: '娇小：闪避 28%，闪避成功把敌人钉住 1 回合'"
assert s.count(old3) == 1
s = s.replace(old3, "desc: '娇小：闪避 28%，闪避成功后魅惑小怪反打同伴'", 1)

io.open(p, "w", encoding="utf-8").write(s)
assert "e.stun" not in s
assert s.count("charm") >= 4
print("charm patch ok", len(s.encode()))
