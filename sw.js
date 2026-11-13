/* 铁墓大乱斗 PWA Service Worker
 * 页面导航：网络优先，断网回退缓存
 * 静态资源：缓存优先 + 网络回填
 */
const CACHE = 'iron-tomb-v3'
const PRECACHE = ['./', './game.html', './manifest.json', './icon-192.png', './icon-512.png']

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => {
      return Promise.all(
        PRECACHE.map((url) => cache.add(new Request(url, { cache: 'reload' })).catch(() => null)),
      )
    }).then(() => self.skipWaiting()),
  )
})

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    }).then(() => self.clients.claim()),
  )
})

function cachePut(request, response) {
  if (!response || response.status !== 200) return
  const copy = response.clone()
  caches.open(CACHE).then((cache) => cache.put(request, copy)).catch(() => {})
}

self.addEventListener('fetch', (event) => {
  const req = event.request
  if (req.method !== 'GET') return

  const url = new URL(req.url)
  if (url.origin !== self.location.origin) return

  const isDoc = req.mode === 'navigate' || req.destination === 'document'

  if (isDoc) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          cachePut(req, res)
          return res
        })
        .catch(() => {
          return caches.match(req).then((hit) => hit || caches.match('./game.html'))
        }),
    )
    return
  }

  event.respondWith(
    caches.match(req).then((hit) => {
      if (hit) return hit
      return fetch(req)
        .then((res) => {
          cachePut(req, res)
          return res
        })
        .catch(() => caches.match('./icon-192.png'))
    }),
  )
})
