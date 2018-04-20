from flask import Flask, render_template, request
import thunderbolt
from web_net import *

class CurryBrowser():

    def __init__(self):

        self.results_dict = {'web_links' : [], 'query': ''}

        self.html_code = ''

        self.main()

    def main(self):

        curb = Flask(__name__)

        @curb.route('/', methods=['GET'])

        def search_page():

            return render_template('search_page.html')

        @curb.route('/', methods=['POST'])

        def show_result():

            query = get_query('text')

            web_links = get_links(query)

            images = get_images(query)

            self.results_dict['web_links'] = web_links

            self.results_dict['query'] = query

            return render_template('result_page.html', search=query, links=web_links, images=images[5 : 15])

        def get_query(form_name):

            query = request.form[form_name]

            return query

        def get_links(query):

            link_list = []

            ser = thunderbolt.Search(query)

            for link in ser.get_values('li'):

                link = 'http://' + link

                link_list.append(link)

            return link_list

        def get_images(query):

            img_list = []

            ser = thunderbolt.Search(query)

            images = ser.get_values('img')

            image_num = 0

            for image in range(int((len(images) * .5)) - 3):

                img_list.append(images[image_num])

                image_num += 2

            return img_list


        if __name__ == '__main__':

            curb.run()


CurryBrowser()
