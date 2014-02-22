(function () {
    var name
    var host = window.location.host, gamehost = 'pokemod.gerhut.net';
    var version;
    switch (host) {
        case 'platium.gerhut.net': version = 'platinum'; break;
        case 'heartgold.gerhut.net': version = 'heartgold'; break;
        default: version = 'platium'; version = 'platinum';
    }

    var urlImg = 'http://' + gamehost + '/' + version
      , urlChat = 'http://' + gamehost + '/' + version + '/chat'
      , urlInfo = 'http://' + gamehost + '/' + version + '/info'
      , urlKeys = 'http://' + gamehost + '/' + version + '/input/gerhut/key'
      , urlMouse = 'http://' + gamehost + '/' + version + '/input/gerhut/mouse';
    var timeout = -1
    var gamescreen = document.getElementById('imgGamescreen')
        , chatlist = document.getElementById('chatlist')
        , inputlist = document.getElementById('inputlist')
        , message = document.getElementById('txtMessage');

    window.sendkey = function (code) {
        jsonp(urlKeys + '/' + code, function (data) {
            return;
        })
    }

    window.imageLoaded = function () {
        setTimeout(function () { gamescreen.src = urlImg + '/?' + Date.now(); }, 100);
    }

    window.refreshChat = function () {
        jsonp(urlInfo, function (chatData, inputData) {
            chatlist.innerHTML = chatData;
            inputlist.innerHTML = inputData;
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
    window.sendmouse = function (event) {
        jsonp(urlMouse + '/' + Math.round(event.offsetX) + ',' + Math.round(event.offsetY), function (data) {
            return;
        })
    }

    window.run = function (udata) {
        name = udata.uname
        window.refreshChat()
    }
})()