# README

Scrapy 官网简单的 Demo。



## 亮点

在页面解析函数内使用 `eval（）`函数动态赋值生成 `item`。No bb，show code。

```python
for field in item.fields:
  try:
	  item[field] = eval(field)
	  print(eval(field))
  except NameError:
    self.logger.debug('Field is not Defined' + field)
```

前提是 **`Item`内定义的字段与解析函数内解析出来的字段名相同**。

如果出现没有定义的字段，Debug 打印出提示信息。

出错的话，出现的是 `NameError`。