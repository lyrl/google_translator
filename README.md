# google_translator

google translation api

google翻译api，不需要key无任调用次数何限制

### install

```
pip install google_translator
```

### Useage
#### shell
```
python Translator.py 'hello'
	
> 你好 
```
#### programmatically

```
t = Translator(Lang.Lang.chinese_simplified)
print t.translate(content)
```

源语言默认为'auto'google会自动检测

#### 手动设置源语言

```
t = Translator(Lang.Lang.chinese_simplified)
t.set_source_lang(Lang.Lang.english)
print t.translate(content)
```