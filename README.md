口袋妖怪白金Online
==================

路由
----
### `GET /?`
当前截图

- `Content-Type: image/png`
- 可使用查询字符串防止缓存

### `GET /talk`
聊天内容

- 内容类型：`application/javascript`
- 内容为一个对象数组：
```json
[
  {
    "date": 1,
    "name": "foo",
    "content": "bar"
  }
]
```

### `POST /talk`
发送聊天内容

- 返回205
- POST数据：`name=content`

### `GET /input`
获得输入内容

- 内容类型：`application/json`
- 内容

### `POST /input`
发送输入内容

- 返回205

License
-------
MIT