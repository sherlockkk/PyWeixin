import xml.dom.minidom
import re


def xml_parse():
    text_xml = '<msg><emoji fromusername="wxid_l4z4n5acbuvf21" tousername="wxid_7yj2nevz2pc812" type="1" idbuffer="media:0_0" md5="a7b5db52e29f565e91122bc6091c9a69" len="42003" productid="" androidmd5="a7b5db52e29f565e91122bc6091c9a69" androidlen="42003" s60v3md5="a7b5db52e29f565e91122bc6091c9a69" s60v3len="42003" s60v5md5="a7b5db52e29f565e91122bc6091c9a69" s60v5len="42003" cdnurl="http://emoji.qpic.cn/wx_emoji/DicQiavKZJlV4ETT8usAa7piaLk3Ps9MuRlpCSxVOqjPpt8geHYqaAymQ/" designerid="" thumburl="" encrypturl="http://emoji.qpic.cn/wx_emoji/DicQiavKZJlV4ETT8usAa7piaLk3Ps9MuRlA8b2yM8WJscMvjsoTDaeOg/" aeskey="c5ea5ddfc1ca229b288cc92236d2c157" width="200" height="200"></emoji></msg>'
    dom = xml.dom.minidom.parseString(text_xml)
    root = dom.documentElement
    tag_names = root.getElementsByTagName('emoji')
    for tag_name in tag_names:
        print(tag_name.nodeValue)


def re_paser():
    text = '<msg><emoji fromusername="wxid_l4z4n5acbuvf21" tousername="wxid_7yj2nevz2pc812" type="1" idbuffer="media:0_0" md5="a7b5db52e29f565e91122bc6091c9a69" len="42003" productid="" androidmd5="a7b5db52e29f565e91122bc6091c9a69" androidlen="42003" s60v3md5="a7b5db52e29f565e91122bc6091c9a69" s60v3len="42003" s60v5md5="a7b5db52e29f565e91122bc6091c9a69" s60v5len="42003" cdnurl="http://emoji.qpic.cn/wx_emoji/DicQiavKZJlV4ETT8usAa7piaLk3Ps9MuRlpCSxVOqjPpt8geHYqaAymQ/" designerid="" thumburl="" encrypturl="http://emoji.qpic.cn/wx_emoji/DicQiavKZJlV4ETT8usAa7piaLk3Ps9MuRlA8b2yM8WJscMvjsoTDaeOg/" aeskey="c5ea5ddfc1ca229b288cc92236d2c157" width="200" height="200"></emoji></msg>'
    re_match = re.findall('[a-zA-z]+://[^\s]*', text)
    print(re_match[0][0:len(re_match[0]) - 1])


if __name__ == '__main__':
    # xml_parse()
    re_paser()
