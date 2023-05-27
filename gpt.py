import openai
import os
from IPython.display import Markdown

openai.api_key = "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"
system_intel = "I am doing an assignment , give the answer in the perspective of a student"
prompt = "Write a blog on how to use GPT-4 with python in a jupyter notebook"
def ask_GPT4(system_intel, prompt): 
    result = openai.ChatCompletion.create(model="gpt-3",
                                 messages=[{"role": "system", "content": system_intel},
                                           {"role": "user", "content": prompt}])
    display(Markdown(result['choices'][0]['message']['content']))

# Call the function above
ask_GPT4(system_intel, prompt)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
kmeans.fit(pca_df)
df['cluster'] = kmeans.labels_
plt.scatter(pca_df['principal component 1'], pca_df['principal component 2'], c=kmeans.labels_)
plt.title('K-means Clustering on Reduced Mall_Customers Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
