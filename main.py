import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')
import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("Google Drive 데이터 시각화 (Plotly + Streamlit)")

# Google Drive에서 데이터 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

df = load_data()

st.subheader("데이터 미리보기")
st.write(df.head())

# Plotly 시각화
st.subheader("Plotly 그래프")

# 예시: scatter plot (데이터에 따라 열 이름 바꾸기)
columns = df.columns.tolist()
if len(columns) >= 2:
    x_col = st.selectbox("X축 선택", columns, index=0)
    y_col = st.selectbox("Y축 선택", columns, index=1)

    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
    st.plotly_chart(fig)
else:
    st.warning("시각화를 위해 최소 두 개의 열이 필요합니다.")
