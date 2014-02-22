function jsonp(url, callback) {
    var callbackName = 'jsonp' + Date.now()
    var script = document.createElement('script')
    script.src = url + '?callback=' + callbackName
    window[callbackName] = function () {
        document.body.removeChild(script);
        callback.apply(this, arguments);
    }
    document.body.appendChild(script)
}