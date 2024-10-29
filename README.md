# wtfpython (in which I rant about writexml)

python's writexml is just wrong. want proof? here it goes...

```python
$ cat print.py
#!/usr/bin/python3
import sys
import xml.dom.minidom
test = xml.dom.minidom.parse(sys.argv[1])
test.writexml(sys.stdout, indent='', addindent='  ', newl='\n', encoding="UTF-8")
```

Let's run this over and over with the same XML? A simply one, like...

```python
$ cat 0.xml
<out><one/><two/></out>
```

Let's run it 10 times:

```
for i in {0..9}; do ./print.py $i".xml" > $((i + 1)).xml; done
```

The result should be all more or less the same, right? I mean, the first one
should be prettier than the input, because we're identing it properly, but
after that nothing else needs changing...

Let's see how did the first run look:

```python
$ cat 1.xml
<?xml version="1.0" encoding="UTF-8"?>
<out>
  <one/>
  <two/>
</out>
```

There you go, looks great! What about the others?

[1.xml](1.xml)
[2.xml](2.xml)
[3.xml](3.xml)
[4.xml](4.xml)
[5.xml](5.xml)
[6.xml](6.xml)
[7.xml](7.xml)
[8.xml](8.xml)
[9.xml](9.xml)
[10.xml](10.xml)

`¯\_(ツ)_/¯`

*For what is worth, these scripts, in case copyright applies to them, are licensed as [GPLv3](LICENSE).*
