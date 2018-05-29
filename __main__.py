from analysis.analizer import json_to_str, count_wordfreq
from collect.crawler import fb_get_post_list
from visualize.visualizer import show_gragh_bar, word_cloud

pagename = "BlizzHeroesKR"
# pagename = "WarcraftKR"
# pagename = "BlizzardKR"
# pagename = "jtbcnews"
# pagename = "chosun"
from_date = "2016-10-10"
to_date = "2018-05-23"
file_path = "D:/Bigdata/facebook/%s.json" % pagename

if __name__ == '__main__':
    #수집
    fb_get_post_list(pagename, from_date, to_date)

    #분석
    data_string = json_to_str(file_path, "message_str")
    count_data = count_wordfreq(data_string)
    dict_word = dict(count_data.most_common(35))

    #그래프
    show_gragh_bar(dict_word, pagename)
    word_cloud(dict_word, pagename)