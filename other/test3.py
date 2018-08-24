# _*_encoding:utf-8_*_

style = 'width: 100%; -moz-user-select: text;"' \
        ' value="2018-10-25" name="dateclosed" size="1" aria-invalid="false" data-errorqtip=""'
print style.find("value")
print style[style.find("value"):]
new_style = style[style.find("value"):]
print new_style[7:17]
print new_style[0:17]