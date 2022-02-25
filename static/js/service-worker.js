// var staticCacheName = "bubot-v1";

// self.addEventListener("install", function (event) {
//     event.waitUntil(
//         caches.open(staticCacheName).then(function (cache) {
//             return cache.addAll([""]);
//         })
//     );
// });

// self.addEventListener("fetch", function (event) {
//     var requestUrl = new URL(event.request.url);
//     if (requestUrl.origin === location.origin) {
//         if (requestUrl.pathname === "/") {
//             event.respondWith(caches.match(""));
//             return;
//         }
//     }
//     event.respondWith(
//         caches.match(event.request).then(function (response) {
//             return response || fetch(event.request);
//         })
//     );
// });
var staticCacheName = "bubotapp" + new Date().getTime();
var filesToCache = [
    "/static/icon-192x192.png",
    "/static/icon-256x256.png",
    "/static/icon-384x384.png",
    "/static/icon-512x512.png",
    "/static/assets/favicon.ico/apple-touch-icon.png",
];
// Cache on install
self.addEventListener("install", (event) => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName).then((cache) => {
            return cache.addAll(filesToCache);
        })
    );
});

// Clear cache on activate
self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames
                    .filter((cacheName) => cacheName.startsWith("django-pwa-"))
                    .filter((cacheName) => cacheName !== staticCacheName)
                    .map((cacheName) => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", (event) => {
    event.respondWith(
        caches
            .match(event.request)
            .then((response) => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match("offline");
            })
    );
});
