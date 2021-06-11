// var a1 = (new Date).getTime();
// var n1 = {cid: 508, param: "{\"cityId\":1501,\"serialId\":\"2573\"}"};
var Y = "19DDD1FBDFF065D3A4DA777D2D7A81EC";


function g(t, i, e) {
    return i ? e ? m(i, t) : v(i, t) : e ? _(t) : C(t)
}

function m(t, i) {
    return p(w(t), w(i))
}

function p(t, i) {
    var e, n, a = y(t), r = [], o = [];
    for (r[15] = o[15] = void 0,
         a.length > 16 && (a = l(a, 8 * t.length)),
             e = 0; e < 16; e += 1)
        r[e] = 909522486 ^ a[e],
            o[e] = 1549556828 ^ a[e];
    return n = l(r.concat(y(i)), 512 + 8 * i.length),
        u(l(o.concat(n), 640))
}
function w(t) {
    return unescape(encodeURIComponent(t))
}

function u(t) {
    var i, e = "", n = 32 * t.length;
    for (i = 0; i < n; i += 8)
        e += String.fromCharCode(t[i >> 5] >>> i % 32 & 255);
    return e
}
function y(t) {
            var i, e = [];
            for (e[(t.length >> 2) - 1] = void 0,
            i = 0; i < e.length; i += 1)
                e[i] = 0;
            var n = 8 * t.length;
            for (i = 0; i < n; i += 8)
                e[i >> 5] |= (255 & t.charCodeAt(i / 8)) << i % 32;
            return e
        }
function l(t, i) {
    var e, a, r, l, u;
    t[i >> 5] |= 128 << i % 32,
        t[(i + 64 >>> 9 << 4) + 14] = i;
    var y = 1732584193
        , f = -271733879
        , p = -1732584194
        , h = 271733878;
    for (e = 0; e < t.length; e += 16)
        a = y,
            r = f,
            l = p,
            u = h,
            f = d(f = d(f = d(f = d(f = s(f = s(f = s(f = s(f = c(f = c(f = c(f = c(f = o(f = o(f = o(f = o(f, p = o(p, h = o(h, y = o(y, f, p, h, t[e], 7, -680876936), f, p, t[e + 1], 12, -389564586), y, f, t[e + 2], 17, 606105819), h, y, t[e + 3], 22, -1044525330), p = o(p, h = o(h, y = o(y, f, p, h, t[e + 4], 7, -176418897), f, p, t[e + 5], 12, 1200080426), y, f, t[e + 6], 17, -1473231341), h, y, t[e + 7], 22, -45705983), p = o(p, h = o(h, y = o(y, f, p, h, t[e + 8], 7, 1770035416), f, p, t[e + 9], 12, -1958414417), y, f, t[e + 10], 17, -42063), h, y, t[e + 11], 22, -1990404162), p = o(p, h = o(h, y = o(y, f, p, h, t[e + 12], 7, 1804603682), f, p, t[e + 13], 12, -40341101), y, f, t[e + 14], 17, -1502002290), h, y, t[e + 15], 22, 1236535329), p = c(p, h = c(h, y = c(y, f, p, h, t[e + 1], 5, -165796510), f, p, t[e + 6], 9, -1069501632), y, f, t[e + 11], 14, 643717713), h, y, t[e], 20, -373897302), p = c(p, h = c(h, y = c(y, f, p, h, t[e + 5], 5, -701558691), f, p, t[e + 10], 9, 38016083), y, f, t[e + 15], 14, -660478335), h, y, t[e + 4], 20, -405537848), p = c(p, h = c(h, y = c(y, f, p, h, t[e + 9], 5, 568446438), f, p, t[e + 14], 9, -1019803690), y, f, t[e + 3], 14, -187363961), h, y, t[e + 8], 20, 1163531501), p = c(p, h = c(h, y = c(y, f, p, h, t[e + 13], 5, -1444681467), f, p, t[e + 2], 9, -51403784), y, f, t[e + 7], 14, 1735328473), h, y, t[e + 12], 20, -1926607734), p = s(p, h = s(h, y = s(y, f, p, h, t[e + 5], 4, -378558), f, p, t[e + 8], 11, -2022574463), y, f, t[e + 11], 16, 1839030562), h, y, t[e + 14], 23, -35309556), p = s(p, h = s(h, y = s(y, f, p, h, t[e + 1], 4, -1530992060), f, p, t[e + 4], 11, 1272893353), y, f, t[e + 7], 16, -155497632), h, y, t[e + 10], 23, -1094730640), p = s(p, h = s(h, y = s(y, f, p, h, t[e + 13], 4, 681279174), f, p, t[e], 11, -358537222), y, f, t[e + 3], 16, -722521979), h, y, t[e + 6], 23, 76029189), p = s(p, h = s(h, y = s(y, f, p, h, t[e + 9], 4, -640364487), f, p, t[e + 12], 11, -421815835), y, f, t[e + 15], 16, 530742520), h, y, t[e + 2], 23, -995338651), p = d(p, h = d(h, y = d(y, f, p, h, t[e], 6, -198630844), f, p, t[e + 7], 10, 1126891415), y, f, t[e + 14], 15, -1416354905), h, y, t[e + 5], 21, -57434055), p = d(p, h = d(h, y = d(y, f, p, h, t[e + 12], 6, 1700485571), f, p, t[e + 3], 10, -1894986606), y, f, t[e + 10], 15, -1051523), h, y, t[e + 1], 21, -2054922799), p = d(p, h = d(h, y = d(y, f, p, h, t[e + 8], 6, 1873313359), f, p, t[e + 15], 10, -30611744), y, f, t[e + 6], 15, -1560198380), h, y, t[e + 13], 21, 1309151649), p = d(p, h = d(h, y = d(y, f, p, h, t[e + 4], 6, -145523070), f, p, t[e + 11], 10, -1120210379), y, f, t[e + 2], 15, 718787259), h, y, t[e + 9], 21, -343485551),
            y = n(y, a),
            f = n(f, r),
            p = n(p, l),
            h = n(h, u);
    return [y, f, p, h]
}
function d(t, i, e, n, a, o, c) {
    return r(e ^ (i | ~n), t, i, a, o, c)
}
function o(t, i, e, n, a, o, c) {
    return r(i & e | ~i & n, t, i, a, o, c)
}
 function c(t, i, e, n, a, o, c) {
            return r(i & n | e & ~n, t, i, a, o, c)
        }
function s(t, i, e, n, a, o, c) {
    return r(i ^ e ^ n, t, i, a, o, c)
}

function a(t, i) {
    return t << i | t >>> 32 - i
}

function r(t, i, e, r, o, c) {
    return n(a(n(n(i, t), n(r, c)), o), e)
}
function n(t, i) {
    var e = (65535 & t) + (65535 & i);
    return (t >> 16) + (i >> 16) + (e >> 16) << 16 | 65535 & e
}
function C(t) {
    return h(_(t))
}

function h(t) {
    var i, e, n = "0123456789abcdef", a = "";
    for (e = 0; e < t.length; e += 1)
        i = t.charCodeAt(e),
            a += n.charAt(i >>> 4 & 15) + n.charAt(15 & i);
    return a
}
function _(t) {
    return f(w(t))
}
function f(t) {
    return u(l(y(t), 8 * t.length))
}


//
function yiche1(t1) {
    var a1 = (new Date).getTime();
    var n1 = {cid: 508, param: ""};
    n1.param = "{\"cityId\":1501,\"serialId\":\"+ +2573\"}";
    r = g("cid=" + 508 + "&param=" + param + Y + a1);
    return a1, r
}

function yiche(t1) {
    return g(t1);
}


