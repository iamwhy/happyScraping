import jieba
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
import pandas as pd

data =pd.read_csv('bili_rsycS02E01.csv',header=0,encoding="utf-8-sig")

stop_words = [x.strip() for x in open ('stopwords.txt',encoding="utf-8") ]
text = ''.join(data['comments'])
words = list(jieba.cut(text))
ex_sw_words = []
for word in words:
    if len(word)>1 and (word not in stop_words):
        ex_sw_words.append(word)
c = Counter()
c = Counter(ex_sw_words)
wc_data = zip(c.keys(),c.values())

#used pyecharts 1.5.1, not compatible with 0.5.* version.
def wordcloudfigure() -> WordCloud:
    wc = (
        WordCloud()
        .add("",list(wc_data), word_size_range=[10, 50],shape=SymbolType.TRIANGLE)
        .set_global_opts(title_opts=opts.TitleOpts(title="人生一串S02E01弹幕分析"))
    )
    return wc

# wordcloudfigure()
make_snapshot(snapshot, wordcloudfigure().render(), "wc_triangle.png")

