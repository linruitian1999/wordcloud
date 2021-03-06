
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import  jieba
def GetWordCloud():
   path_txt = 'D://office/六六.txt'#需要处理的文本的位置，如果是其他格式的文本建议导入其他文本处理库
   path_img = "D://office/六六.png"#生成词云的图片，最好是白色背景，主体的颜色最好深一点，不然生成的效果不明显
   f = open(path_txt, 'r', encoding='UTF-8').read()#uf8的文本格式，如果报错的话，打开文本文件，将输出格式修改一下

   background_image = np.array(Image.open(path_img))
   # 结巴分词，专门处理中文文本的分词结构
   #增加忽略分词，如果数量过多可以做一个文本词库把不要拆分的文本放进去
   jieba.suggest_freq(('火钳刘明'), True)
   jieba.suggest_freq(('谢罪警告'), True)
   jieba.suggest_freq(('开花就完事了'), True)
   jieba.suggest_freq(('开花'), True)
   jieba.suggest_freq(('章口就来'), True)
   jieba.suggest_freq(('章口就莱'), True)
   jieba.suggest_freq(('两开花'), True)
   jieba.suggest_freq(('改编不是乱编'), True)
   jieba.suggest_freq(('中美合拍'), True)
   jieba.suggest_freq(('国际巨星'), True)
   jieba.suggest_freq(('我也喜欢'), True)
   cut_text = " ".join(jieba.cut(f))
   wordcloud = WordCloud(
       # 设置字体，simhei是黑体，字体所在的位置是隐藏的，只能把地址放在地址栏里直接打开，然后查看想要用的字体，把自己的文件名复制下来
       font_path="C:/Windows/Fonts/simhei.ttf",
       margin=1,
       background_color="white",#图片背景颜色，可以改成别的颜色
       # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
       mask=background_image).generate(cut_text)
   # 生成颜色值
   image_colors = ImageColorGenerator(background_image)
   # 下面代码表示显示图片
   plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
   plt.axis("off")
   plt.imshow(wordcloud)
   plt.savefig("D:/office/xhxhxh.jpg",dpi=1000)#生成的图片的位置，可以修改
   plt.show()

if __name__ == '__main__':
   GetWordCloud()
#有时候会出现格式不匹配的问题，一般改一下格式就可以用了

#完结，撒花 ✿✿ヽ°▽°ノ✿
