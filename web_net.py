import urllib
import urllib.request
import os
import re


def download_web_image(url, name):
    full_name = name + '.jpg'
    file_path = 'C:\\Users\\Pratim\\Documents\\Pictures\\' + full_name
    urllib.request.urlretrieve(url, full_name)
    os.rename(full_name, file_path)
    return file_path, full_name


def parse_website(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respdata = resp.read()
    paragraph = re.findall(r'<p>(.*?)</p>', str(respdata))
    str_paragraph = ''
    parse_paragraph = ''
    for char in paragraph:
        str_paragraph = str_paragraph + char + ' '
    data_tags = re.findall(r'<(.*?)>', str_paragraph)
    for a_tag in data_tags:
        tags = '<' + a_tag + '>'
        parse_paragraph = str_paragraph.replace(tags, '')
        str_paragraph = parse_paragraph
    return parse_paragraph


def parse_website_ultra(url): #Currently in BETA
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respdata = resp.read()
    paragraph = re.findall(r'<p>(.*?)</p>', str(respdata))
    str_paragraph = ''
    parse_paragraph = ''
    for char in paragraph:
        str_paragraph = str_paragraph + char + ' '
    data_tags = re.findall(r'<(.*?)>', str_paragraph)
    for a_tag in data_tags:
        tags = '<' + a_tag + '>'
        parse_paragraph = str_paragraph.replace(tags, '')
        str_paragraph = parse_paragraph
    tagList = []
    dat_num_tags = re.findall(r'\[(.*?)\]', parse_paragraph)
    for num_tag in dat_num_tags:
        num_tags = '[' + num_tag + ']'
        tagList.append(num_tags)
    for numtag in tagList:
        parse_paragraph = str_paragraph.replace(numtag, '')
        str_paragraph = parse_paragraph
    xentagList = []
    data_num_xen = re.findall(r'\((.*?)\)', parse_paragraph)
    for xentag in data_num_xen:
        xen_tag = '(' + xentag + ')'
        xentagList.append(xentag)
    for xen_tags in xentagList:
        parse_paragraph = str_paragraph.replace(xen_tags, '')
        str_paragraph = parse_paragraph
    return parse_paragraph


def parse_text(paragraph):
    str_paragraph = ''
    parse_paragraph = ''
    for i in paragraph:
        str_paragraph = str_paragraph + i + ' '
    for x in paragraph:
        data_tags = re.findall(r'<(.*?)>', str_paragraph)
        for a_tag in data_tags:
            tags = '<' + a_tag + '>'
            parse_paragraph = str_paragraph.replace(tags, '')
            str_paragraph = parse_paragraph
    return parse_paragraph


def find_images_wiki(topic):
    url = 'https://en.wikipedia.org/wiki/' + topic
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respdata = resp.read()
    img_alt = topic
    try:
        try:
            r_stat = re.findall(r'img alt="' + re.escape(img_alt) + r'(.*?)width', str(respdata))
            data_img = re.findall(r'src="(.*?)"', str(r_stat))
            url = str(data_img[0])
            full_url = 'https:' + url
            download_web_image(full_url, topic)
        except:
            img_alt2 = topic.replace(' ', '')
            r_stat = re.findall(r'img alt="' + re.escape(img_alt2) + r'(.*?)width', str(respdata))
            data_img = re.findall(r'src="(.*?)"', str(r_stat))
            url = str(data_img[0])
            full_url = 'https:' + url
            download_web_image(full_url, topic)
    except:
        try:
            img_alt3 = topic.split()
            img_alt3 = img_alt3[0]
            r_stat = re.findall(r'img alt="' + re.escape(img_alt3) + r'(.*?)width', str(respdata))
            data_img = re.findall(r'src="(.*?)"', str(r_stat))
            url = str(data_img[0])
            full_url = 'https:' + url
            download_web_image(full_url, topic)
        except:
            img_alt4 = topic.split()
            img_alt4 = img_alt4[1]
            r_stat = re.findall(r'img alt="' + re.escape(img_alt4) + r'(.*?)width', str(respdata))
            data_img = re.findall(r'src="(.*?)"', str(r_stat))
            url = str(data_img[0])
            full_url = 'https:' + url
            download_web_image(full_url, topic)
    return full_url


def find_images_yahoo(topic):
    url = 'https://images.search.yahoo.com/search/images;_ylt=AwrB8p6NShdZEWYALnKLuLkF;_ylc=X1MDOTYwNTc0ODMEX3IDMgRiY2sDY2VxYjJhcGM5aHZhaiUyNmIlM0QzJTI2cyUzRGh1BGZyAwRncHJpZAM4LjB3TXEwd1I3V0ZNbkczSVNFTzdBBG10ZXN0aWQDbnVsbARuX3N1Z2cDMTAEb3JpZ2luA2ltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzYEcXVlcnkDRG9uYWxkBHRfc3RtcAMxNDk0Njk4ODgyBHZ0ZXN0aWQDbnVsbA--?gprid=8.0wMq0wR7WFMnG3ISEO7A&pvid=l6EeiDY5LjHHaWJWWJj9UwgmOTguMQAAAAClVr6h&fr2=sb-top-images.search.yahoo.com&p=' + topic + '#id=fpub0&iurl=https%3A%2F%2Fc1.staticflickr.com%2F9%2F8458%2F8061492584_0f320a0ef9_b.jpg&action=click'
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respdata = resp.read()
    r_stat = re.findall(r'<img(.*?)alt', str(respdata))
    data_img = re.findall(r'c1.staticflickr.com(.*?).jpg', str(r_stat))
    img_url = data_img[0]
    full_url = 'https://c1.staticflickr.com' + img_url + '.jpg'
    download_web_image(full_url, topic)

