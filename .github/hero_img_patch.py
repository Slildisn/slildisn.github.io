import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

# 1) 铃兰绑定头像
old = "{ id: 'lily', name: '铃兰', hp: 10, atk: 3, vision: 7, crit: .14, dodge: .22, potion: 1.3, desc: '小小只：闪避 22%，血薄但跑得快', icon: '铃', emoji: '🎀', color: '#ffc2dd' }"
assert s.count(old) == 1
new = "{ id: 'lily', name: '铃兰', hp: 10, atk: 3, vision: 7, crit: .14, dodge: .22, potion: 1.3, desc: '小小只：闪避 22%，血薄但跑得快', icon: '铃', emoji: '🎀', color: '#ffc2dd', img: 'assets/hero-lily.webp' }"
s = s.replace(old, new, 1)

# 2) 图片加载器
anchor = """  function heroColor(h) {
    return (h && h.color) || '#ff9ec4'
  }"""
assert s.count(anchor) == 1
loader = anchor + """

  /* ---------------- 角色头像图片 ---------------- */
  var HERO_IMGS = {}
  function heroImg(h) {
    if (!h || !h.img) return null
    var rec = HERO_IMGS[h.id]
    if (!rec) {
      rec = HERO_IMGS[h.id] = { img: new Image(), ready: false }
      rec.img.onload = function () { rec.ready = true }
      rec.img.onerror = function () { rec.ready = false }
      rec.img.src = h.img
    }
    return rec.ready ? rec.img : null
  }"""
s = s.replace(anchor, loader, 1)

# 3) 画布玩家渲染
p_anchor = """    if (emojiOk(S.hero.emoji)) {
      var emojiSize = Math.max(16, Math.round(TS * 0.95))"""
assert s.count(p_anchor) == 1
p_new = """    var himg = heroImg(S.hero)
    if (himg) {
      // 有头像图片：圆形裁剪绘制
      ctx.save()
      ctx.beginPath(); ctx.arc(pxx, pyy, TS * .38, 0, Math.PI * 2); ctx.clip()
      ctx.drawImage(himg, pxx - TS * .38, pyy - TS * .38, TS * .76, TS * .76)
      ctx.restore()
      ctx.strokeStyle = pcolor
      ctx.lineWidth = Math.max(2, TS * .08)
      ctx.beginPath(); ctx.arc(pxx, pyy, TS * .4, 0, Math.PI * 2); ctx.stroke()
    } else if (emojiOk(S.hero.emoji)) {
      var emojiSize = Math.max(16, Math.round(TS * 0.95))"""
s = s.replace(p_anchor, p_new, 1)

# 4) 选人面板显示头像
sel_anchor = "b.innerHTML = '<b>' + (h.emoji || '') + ' ' + h.name + '</b><i>' + h.desc + '</i>'"
assert s.count(sel_anchor) == 1
sel_new = "b.innerHTML = '<b>' + (h.img ? '<img class=\"hero-avatar\" src=\"' + h.img + '\" alt=\"\">' : (h.emoji || '')) + ' ' + h.name + '</b><i>' + h.desc + '</i>'"
s = s.replace(sel_anchor, sel_new, 1)

# 5) 头像样式
css_anchor = "#ov-select .pick::-webkit-scrollbar-thumb{background:rgba(255,158,196,.3);border-radius:99px}"
assert s.count(css_anchor) == 1
css_new = css_anchor + "\n  .hero-avatar{width:20px;height:20px;border-radius:50%;object-fit:cover;vertical-align:-4px;margin-right:2px;border:1px solid rgba(255,158,196,.5)}"
s = s.replace(css_anchor, css_new, 1)

io.open(p, "w", encoding="utf-8").write(s)
print("patched bytes:", len(s.encode()))
for key in ["heroImg", "hero-avatar", "assets/hero-lily.webp"]:
    assert key in s, key
print("checks ok")
