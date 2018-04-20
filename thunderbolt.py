from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import os


class WebParser:

    def __init__(self, url='', data_=''):

        if len(data_) > 1:

            self.data_ = data_
            pass
        elif len(url) > 0:

            self.data_ = ''

            self.url = url
            raw_data = urllib.request.urlopen(self.url)

            data = BeautifulSoup((raw_data).read(), 'lxml')

            self.data = data

    def parse_website(self, type):

        if len(self.data_) > 0:

            if type.lower() == 'p':

                p_list = []

                for p in self.data_.find_all('p'):
                    p_list.append(p.text)

                return p_list

            elif type.lower() == 'img':

                src_list = []

                for images in self.data_.find_all('img'):
                    src_list.append(re.findall(r'src="(.*?)"', str(images)))

                return src_list

            elif type.lower() == 'a':

                # In Development

                a_list = []

                for anchors in self.data_.find_all('a'):
                    a_list.append(anchors.href)

            else:

                return None
        else:

            if type.lower() == 'p':

                p_list = []

                for p in self.data.find_all('p'):
                    p_list.append(p.text)

                return p_list

            elif type.lower() == 'img':

                src_list = []

                for images in self.data.find_all('img'):
                    src_list.append(re.findall(r'src="(.*?)"', str(images)))

                return src_list

            elif type.lower() == 'a':

                # In Development

                a_list = []

                for anchors in self.data.find_all('a'):
                    a_list.append(anchors.href)

            else:

                return 'null'


class Search:

    # This class allows you to put a in a search topic and get search results

    def __init__(self, query):

        self.url = 'https://search.yahoo.com/search'

        self.values = {'p': query}

        self.pre_req = (urllib.parse.urlencode(self.values)).encode('utf-8')  # puts values into format for search

        self.t_data = BeautifulSoup(
            urllib.request.urlopen(urllib.request.Request('https://search.yahoo.com/search', self.pre_req)).read(),
            'lxml')

        self.img_data = BeautifulSoup(urllib.request.urlopen(urllib.request.Request('https://images.search.yahoo.com/search/images', self.pre_req)).read(), 'lxml')

    def get_values(self, type):

        if type.lower() == 'li':

            link_list = []

            for span in self.t_data.find_all('span', class_=' fz-ms fw-m fc-12th wr-bw lh-17'):
                link_list.append(span.text)

            return link_list

        elif type.lower() == 'img':

            img_list = []

            for img in self.img_data.find_all('img'):

                img_list.append(''.join(re.findall(r'src="(.*?)"', str(img))))

            return img_list


class FileBrowser:

    def __init__(self, file_name, path=''):

        if len(path) > 0:
            os.chidir(path)


        self.file_name = file_name

    @property
    def is_open(self):

        if not self.file.closed:

            return True

        else:

            return False

    def raise_error(self, error):

        return 'That is not a support type of split, the supported types are "word", and "line"'

    def read_file(self, type, li_type='word'):

        with open(self.file_name, 'r') as self.file:


            if type.lower() == 'str':

                return str(self.file.read())

            elif type.lower() == 'li':

                if li_type.lower() == 'word':

                    newline_strip = ' '.join(((self.file).read()).split('\n'))

                    return newline_strip.split(' ')

                elif li_type.lower() == 'line':

                    return str((self.file).read()).split('\n')

                else:

                    return self.raise_error(str(li_type))

        self.file.close()
