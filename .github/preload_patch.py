import io

p = "game.html"
s = io.open(p, encoding="utf-8").read()

a1 = "    return rec.ready ? rec.img : null\n  }"
assert s.count(a1) == 1
s = s.replace(a1, a1 + """

  function preloadHeroImgs() {
    for (var pi = 0; pi < HEROES.length; pi++) if (HEROES[pi].img) heroImg(HEROES[pi])
  }""", 1)

a2 = "    buildPicker()\n    setMenuChrome(true)"
assert s.count(a2) == 1
s = s.replace(a2, "    buildPicker()\n    preloadHeroImgs()\n    setMenuChrome(true)", 1)

a3 = "    } else if (emojiOk(S.hero.emoji)) {"
assert s.count(a3) == 1
s = s.replace(a3, """    } else if (S.hero.img) {
      // 头像尚未加载完成：先画应援色圆盘 + 名字首字，避免先闪一下 emoji
      ctx.fillStyle = pcolor
      ctx.beginPath(); ctx.arc(pxx, pyy, TS * .3, 0, Math.PI * 2); ctx.fill()
      ctx.fillStyle = '#120a18'
      ctx.font = 'bold ' + Math.round(TS * .42) + 'px -apple-system,\"PingFang SC\",sans-serif'
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      ctx.fillText(String(S.hero.name).charAt(0), pxx, pyy)
    } else if (emojiOk(S.hero.emoji)) {""", 1)

a4 = "(S.hero.emoji && emojiOk(S.hero.emoji) ? S.hero.emoji + ' ' : '') + S.hero.name"
assert s.count(a4) == 1
s = s.replace(a4, "(!S.hero.img && S.hero.emoji && emojiOk(S.hero.emoji) ? S.hero.emoji + ' ' : '') + S.hero.name", 1)

io.open(p, "w", encoding="utf-8").write(s)
assert s.count("preloadHeroImgs") == 2
assert "S.hero.img) {" in s
print("preload patch ok", len(s.encode()))
