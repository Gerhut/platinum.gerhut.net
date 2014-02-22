﻿(function () {
    var name = 'user';//测试用户名
    var host = window.location.host, gamehost = 'pokemod.gerhut.net';
    var version;
    switch (host) {
        case 'platium.gerhut.net': version = 'platium'; break;
        case 'heartgold.gerhut.net': version = 'heartgold'; break;
        default: version = 'platium'; version = 'platium';
    }

    var urlImg = 'http://' + gamehost + '/' + version, urlChat = 'http://' + gamehost + '/' + version + '/chat', urlKeys = 'http://' + gamehost + '/' + version + '/keys';
    var timeout = -1
    var gamescreen = document.getElementById('imgGamescreen'), chatlist = document.getElementById('chatlist'), message = document.getElementById('txtMessage');

    window.load = function () {

        if (window.timeout > -1)
            clearTimeout(timeout)
        timeout = setTimeout(refresh, 100)
    }

    function refresh() {
        gamescreen.src = urlImg + '/?' + Date.now();
        jsonp(urlChat, function (data) {
            chatlist.textContent = data;
            setTimeout(refresh, 100);
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

})()