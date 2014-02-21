function jsonp(url, callback) {
    var callbackName = 'jsonp' + Date.now()
    var script = document.createElement('script')
    script.src = url + '?callback=' + callbackName
    window[callbackName] = function (data) {
        document.body.removeChild(script);
        callback(data);
    }
    document.body.appendChild(script)
}