import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv(r"Instagram.csv")

data = pd.read_csv(r"Instagram.csv")

df.info()

from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
df["Content Type"]=label.fit_transform(df["Content Type"]) # 0 - reel and 1 - post 

df["Post Time"].value_counts()

label1=LabelEncoder()
df["Post Time"]=label1.fit_transform(df["Post Time"]) #1-night,0-evening

df=df.drop(columns="Note ").copy()

df["Date Posted"]=pd.to_datetime(df["Date Posted"],format='%m/%d/%Y')

data['cta rate'] = data['CTA'] / data['Reach']


best_post = data.loc[data['Engagement Rate (%)'].idxmax()]
print("\n🏆 Highest Engagement Post:")
print(best_post[['Date Posted',"Post Time","Duration (sec)", 'Caption', 'Reach', 'Likes', 'Comments', 'Shares', 'Engagement Rate (%)']])


#!pip install matplotlib
#import matplotlib.pyplot as plt
#import seaborn as sns
fg=plt.figure(figsize=(8, 5))
sns.barplot(x="Content Type", y="Engagement Rate (%)", data=data, palette='viridis') 
plt.title('Engagement Rate by Content Type')
plt.ylabel('Average Engagement Rate (%)')
plt.xlabel('Content Type')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

gf = plt.figure(figsize=(10,5))
sns.lineplot(x='Date Posted', y='Engagement Rate (%)', data=df, marker='o')
plt.title("Engagement Rate Over Time")
plt.xticks(rotation=45)
plt.ylabel("Engagement Rate")
plt.show()

pn=plt.figure(figsize=(8,5))
sns.barplot(x='Post Time', y='Engagement Rate (%)', data=data, estimator='mean', ci=None)
plt.title("Engagement by Post Time")
plt.show()

po = plt.figure(figsize=(8,5))
sns.scatterplot(x='Duration (sec)', y='Engagement Rate (%)', hue='Content Type', data=data, s=100)
plt.title("Duration vs Engagement Rate")
plt.show()

gn= plt.figure(figsize=(10,6))
corr = data.select_dtypes('number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Between Metrics")
plt.show()

import streamlit as st
from streamlit_jupyter import StreamlitPatcher
# Patch Streamlit to work in Jupyter
StreamlitPatcher().jupyter()
# Now you can use supported Streamlit commands
st.set_page_config(page_title = "Digital Marketing Analysis")
st.header("My Data Analysis for our instagram account")
st.subheader("Hello Everyone, I'm Vedhesh.\n")
st.subheader(" This is my analysis of our instagram account reach in 7 days ")
st.text("you want to see analysis one by one use below Buttons :")
a = st.button("🏆 Highest Engagement Post Details:")
b = st.button("Engagement Rate for Content Type(Reel/Post)")
c = st.button("Engagement Rate Over Time ")
d = st.button("Engagement by Post Time")
e= st.button("Duration vs Engagement Rate")
f= st.button("Correlation Between Metrics")
g= st.button("Final")
st.text(" OR you want to see mulTiple analysis in one use below checkpoints :")
a = st.checkbox("🏆 Highest Engagement Post Details:")
b = st.checkbox("Engagement Rate for Content Type(Reel/Post)")
c = st.checkbox("Engagement Rate Over Time ")
d = st.checkbox("Engagement by Post Time")
e= st.checkbox("Duration vs Engagement Rate")
f= st.checkbox("Correlation Between Metrics")
g= st.checkbox("Final")
if a:
    best_post = data.loc[data['Engagement Rate (%)'].idxmax()]
    st.subheader("\n🏆 Highest Engagement Post:")
    d=best_post[['Date Posted',"Post Time","Duration (sec)", 'Caption', 'Reach', 'Likes', 'Comments', 'Shares', 'Engagement Rate (%)']]
    st.write(d)
if b:
    st.pyplot(fg)
    st.write("📊 Key Interpretation \n",
    "The plot shows a significant difference in the average engagement rate between Reels and Posts.\n",
    "Posts have a substantially higher average engagement rate (approximately 18.5%) compared to Reels.\n"
    "Reels have a much lower average engagement rate (approximately 4.5%).")
if c:
    st.pyplot(gf)
    st.write("📉 Key Trend Analysis \n",
"The plot displays the average daily engagement rate from October 2nd to October 8th, 2025, revealing a highly volatile and fluctuating trend with a clear peak.\n",
"Initial Fluctuation (Oct 2 - Oct 4): Engagement starts low (around 3.5% on Oct 2), rises sharply to a local peak (around 11.5% on Oct 3), and then drops back down to a low point (around 3% on Oct 4).\n",
"Major Peak (Oct 5): The engagement rate hits its highest point, peaking dramatically at approximately 22%. This date represents the most successful day in terms of overall engagement.\n",
"Steep Decline (Oct 6 - Oct 8): Following the major peak, the engagement rate drops sharply (to about 9% on Oct 6) and continues a steady decline, ending the plotted period at its lowest point (around 3% on Oct 8).")
st.write("")
if d:
    st.pyplot(pn)
    st.write("🚀 Strategic Conclusion: \n",
"The data clearly suggests that the best time to post for maximizing average engagement is during the evening hours.\n",
"Focus on Evening: The creator should prioritize posting content during the evening window to take advantage of the higher engagement. This likely corresponds to a time when the target audience is most active and consuming content.Re-evaluate .\n", 
"Night Strategy: Posting content at night generates a respectable, but lower, engagement rate. The creator could consider shifting content intended for the night to the evening, or if night posting must continue, investigate if a specific window within the night period performs better than others.\n",
"The difference in average engagement rate between evening and night is roughly $1.9\%$ ($9.5\% - 7.6\%$), which is a significant lift when considering overall audience interaction.")
if e:
    st.pyplot(po)
    st.write("🔵 Interpretation for Reels (Blue Dots):\n"
    ,"Negative Correlation: For Reels, there appears to be a general negative correlation between duration and engagement rate. As the duration increases, the engagement rate tends to decrease, although the relationship is not perfectly linear.\n",
    "The highest engagement for a Reel (around 8%) occurs at a duration of approximately 20 seconds.\n",
    "Engagement rates drop to their lowest (around 1.5% to 3.5%) for durations between 15 and 26 seconds.\n",
    "There's an outlier at 10 seconds with an engagement rate of about 4.8%.\n",
    "Optimal Length: Based on this data, shorter Reels (around 10-20 seconds) perform better than longer ones (22-26 seconds).")
    st.write("🟠 Interpretation for Posts (Orange Dots):\n",
    "Duration is Zero: All Posts are clustered near Duration = 0 seconds. This is expected, as a standard static image post or carousel post does not have a duration in the same way a video (Reel) does.\n",
    "High Engagement: Critically, all three Post data points show significantly higher engagement rates than any of the Reels.\n",
    "The engagement rates for posts range from about 15.5% to 22.5%. \n",
    "The highest performing piece of content in the entire dataset is a Post (around 22.5% engagement).")
if f:
    st.pyplot(gn)
    st.write("⚡ Quick Interpretation \n","The data reveals that shorter content and strong Calls to Action (CTAs) are the most critical factors for success.\n",
             "Engagement Rate is highest when Duration is low ($r = -0.84$) and when the CTA Rate is high ($r = 0.96$).\n",
             "Reach drives raw interaction volume (Likes, Comments, etc.), but high overall Reach significantly lowers the Engagement Rate ($r = -0.84$), suggesting that content seen by non-followers engages less.\n",
             "CTAs are highly effective at driving users to the profile, as CTA Rate is nearly perfectly correlated with Profile Visits and strongly correlated with Follows Gained ($r = 0.88$).")
if g:
    st.write("🔑 Unified Action Plan\n",
"Allocate Resources to Posts: Create more traditional Post content, as it offers the highest return on engagement.\n",
"Enforce Strong CTAs: Ensure every piece of content (especially Posts) includes a compelling Call to Action.\n",
"Post in the Evening: Schedule the highest-priority content for the evening window.\n",
"Keep Reels Short: If creating Reels, aim for 20 seconds or less.")
    st.subheader("  Thank You for Watching  ")




