# _*_encoding:utf-8_*_
import re

style = 'width: 100%; -moz-user-select: text;"' \
        ' value="2018-10-25" name="dateclosed" size="1" aria-invalid="false" data-errorqtip=""'
print style.find("value")
print style[style.find("value"):]
new_style = style[style.find("value"):]
print new_style[7:17]
print new_style[0:17]
print re.match("\d{4}\-\d{2}\-\d{2}", style, 0)   # 从开头匹配，所以匹配不到
print re.search("\d{4}\-\d{2}\-\d{2}", style).string
print len(re.findall("\d{4}\-\d{2}\-\d{23}", style))

