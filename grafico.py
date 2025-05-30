import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Nível de educação em relação a renda!')

url = 'https://raw.githubusercontent.com/ofeliacarvalhow/joxercicios/refs/heads/main/adult11.csv'
df = pd.read_csv(url)

df['salary'] = df['salary'].replace({
    '<=50K': 'abaixo de 50K',
    '>50K': 'acima de 50K'
})

st.subheader('Nível de escolaridade dos gringo')
educad = df['education'].value_counts().sort_values(ascending=True)
fig1, ax1 = plt.subplots(figsize=(8, 6))
educad.plot(kind='barh', ax=ax1, color='skyblue')
ax1.set_xlabel('Gringos')
ax1.set_ylabel('Escolaridade')
st.pyplot(fig1)

st.subheader('comparação de renda com nível de educação')
salarioeducado = df.groupby(['education', 'salary']).size().unstack().fillna(0)

fig2, ax2 = plt.subplots(figsize=(10, 6))
salarioeducado.plot(kind='bar', ax=ax2)
ax2.set_ylabel('Gringos')
ax2.set_xlabel('Escolaridade')
ax2.set_title('Salário (Abaixo/Acima de 50K) em relação a educação')
plt.xticks(rotation=45)
st.pyplot(fig2)
