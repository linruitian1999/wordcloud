from wordcloud import WordCloud#daiy#导入词云
import matplotlib.pyplot as plt
 
f = open(u'D:\office\六.txt','r').read()#导入需要处理的文本的文件
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f)
 
# width,height,margin可以设置图片，包括高宽背景颜色字体间隔等

plt.imshow(wordcloud)
plt.axis("off")
plt.show()#预览图片

wordcloud.to_file('test.png') #把图片保存在蟒蛇文件所在的地址
