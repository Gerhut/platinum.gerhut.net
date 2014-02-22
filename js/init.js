(function () {
    var name = 'user';//测试用户名
    var host = window.location.host, gamehost = 'pokemod.gerhut.net';
    var version;
    switch (host) {
        case 'platium.gerhut.net': version = 'platinum'; break;
        case 'heartgold.gerhut.net': version = 'heartgold'; break;
        default: version = 'platium'; version = 'platinum';
    }

    var urlImg = 'http://' + gamehost + '/' + version
      , urlChat = 'http://' + gamehost + '/' + version + '/chat'
      , urlKeys = 'http://' + gamehost + '/' + version + '/input/gerhut/key'
      , urlMouse = 'http://' + gamehost + '/' + version + '/input/gerhut/mouse';
    var timeout = -1
    var gamescreen = document.getElementById('imgGamescreen'), chatlist = document.getElementById('chatlist'), message = document.getElementById('txtMessage');

    window.sendkey = function (code) {
        jsonp(urlKeys + '/' + code, function (data) {
            return;
        })
    }

    window.imageLoaded = function () {
        setTimeout(function () { gamescreen.src = urlImg + '/?' + Date.now(); }, 100);
    }

    window.refreshChat = function() {
        jsonp(urlChat, function (data) {
            chatlist.innerHTML = data;
            setTimeout(window.refreshChat, 500);
        })
    }
    window.talk = function () {
        if (message.value != '' && message.value.length <= 40) {
            jsonp(urlChat + '/' + encodeURIComponent(name) + '/' + encodeURIComponent(txtMessage.value), function send(data) {
                return;
            })
            message.value = ''
        }
    }
    window.sendmouse = function(event) {
        jsonp(urlMouse + '/' + Math.round(event.offsetX) + ',' + Math.round(event.offsetY), function (data) {
            return;
        })
    }
})()