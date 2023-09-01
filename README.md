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


#### Support Languages
```
Afrikaans	af 

Albanian	sq 

Arabic	ar 

Azerbaijani	az 

Basque	eu 

Bengali	bn 

Belarusian	be 

Bulgarian	bg 

Catalan	ca 

Chinese Simplified	zh-CN 

Chinese Traditional	zh-TW 

Croatian	hr 

Czech	cs 

Danish	da 

Dutch	nl 

English	en 

Esperanto	eo 

Estonian	et 

Filipino	tl 

Finnish	fi 

French	fr 

Galician	gl 

Georgian	ka 

German	de 

Greek	el 

Gujarati	gu 

Haitian Creole	ht 

Hebrew	iw 

Hindi	hi 

Hungarian	hu 

Icelandic	is 

Indonesian	id 

Irish	ga 

Italian	it 

Japanese	ja 

Kannada	kn 

Korean	ko 

Latin	la 

Latvian	lv 

Lithuanian	lt 

Macedonian	mk 

Malay	ms 

Maltese	mt 

Norwegian	no 

Persian	fa Polish	pl 

Portuguese	pt 

Romanian	ro 

Russian	ru 

Serbian	sr 

Slovak	sk 

Slovenian	sl 

Spanish	es 

Swahili	sw 

Swedish	sv 

Tamil	ta 

Telugu	te 

Thai	th 

Turkish	tr 

Ukrainian	uk 

Urdu	ur 

Vietnamese	vi 

Welsh	cy 

Yiddish	yi
``` test
