from pprint import pprint
import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = 'c23e93ef50109204a1d75e7f28da8858'


def get_article(article_url):

    # set request params for API request
    params = {'token': DIFFBOT_DEV_TOKEN,
              'url': article_url,
              'discussion': 'false'}
    # print("***PARAMS***", params)
    res = requests.get(DIFFBOT_API_URL, params)  # hit the Diffbot API
    res_json = res.json()
    # print("**RESPONSE***", res_json)
    if 'objects' in res_json:
        res_obj = res_json['objects'][0]
        # print("***RESPONSE***", type(res_obj))
        # pprint(res_obj)
        return res_obj['text']

        # pull out the text
    else:
        print('Error: JSON response has not objects key:')
        pprint(res_json)  # pretty-print JSON with each key on a separate line


if __name__ == '__main__':
    import sys
    urls_file = open(sys.argv[1])
    # read whole file and make list of urls
    urls_list = urls_file.read().split("\n")
    urls_file.close()

    corpus = ''
    file_open = True
    counter = 0
    print("COUNTER", counter)

    output_file = open(f'corpus/corpus-{counter}.txt', 'w')

    # for line in urls_file:  # read one line of file per iteration, each line is a url
    for line in urls_list:  # iterate over list of urls
        # remove leading/trailing whitespace
        counter += 1
        url = f"https://techcrunch.com{line}"
        article = get_article(url)
        corpus += article
        output_file.write(corpus)
        print('Corpus saved to {}'.format(output_file.name))

    output_file.close()
