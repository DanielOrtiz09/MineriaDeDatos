from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def open_file(path: str) -> str:
    coon = ""
    with open(path, "r") as f:
        coon = f.readlines()
    return " ".join(coon)

df = pd.read_csv("VideoGamesDS.csv")
df.to_csv("TextC.txt")
all_words = ""
enun = open_file("TextC.txt") 
pals = enun.rstrip().split(" ")
Counter(" ".join(pals).split()).most_common(20)
for arg in pals:
    tokens = arg.split()
    all_words += " ".join(tokens) + " "

print(all_words)
wordcloud = WordCloud(
    background_color="black", min_font_size=7
).generate(all_words)


plt.close()
plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig("wordcloudp10.png")
plt.close()