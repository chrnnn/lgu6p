import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
sns.set(font='Malgun Gothic',
        rc={'axes.unicode_minus' : False},
        style='darkgrid')

# 페이지 설정
st.set_page_config(page_title = "Matplotlib & Seaborn 튜토리얼",
                   layout="wide")
st.title("Matplotlib & Seaborn 튜토리얼")  # 제목 만들기

# 데이터셋 불러오기
tips = sns.load_dataset('tips')

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(tips.head())


############ 시각화 시작 #############
# 1. 기본 막대 그래프 (matplotlib + seaborn)
st.subheader("1. 기본 막대 그래프")
fig, ax = plt.subplots(figsize=(10, 6))  # matplotlib

sns.barplot(data=tips, x='day', y='total_bill', ax=ax,
            palette='pastel', edgecolor='black', linewidth=1.5)  # seaborn

ax.set_title('요일별 평균 지불 금액', fontweight='bold', pad=15) # matplotlib
ax.set_xlabel('요일') # matplotlib
ax.set_ylabel('평균 지불 금액 ($)') # matplotlib

# plt.show() ==> 이 문법은 jupyter notebook, google colab에서 활용할 때 사용
st.pyplot(fig)  # streamlit 문법


# 2. 산점도
# x축, y축이 연속형 변수여야 함
st.subheader("2. 산점도")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', ax=ax)
# 옵션을 추가해서 시각화를 상세하게
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', 
                size='size', ax=ax1)
st.pyplot(fig1) 


# 3. 히트맵
st.subheader("3. 히트맵")
# 요일과 시간별 평균 팁 계산
pivot_df = tips.pivot_table(values='tip', index='day', columns='time',
                            aggfunc='mean')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt='.2f', ax=ax2)
st.pyplot(fig2) 


# 4. 회귀선이 있는 산점도
st.subheader("4. 회귀선이 있는 산점도")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.regplot(data=tips, x='total_bill', y='tip', 
            scatter_kws={'alpha':0.5}, ax=ax3) # alpha는 투명도?
st.pyplot(fig3)


# 5. 파이 차트
st.subheader("5. 파이 차트")
fig4, ax4 = plt.subplots(nrows=1, ncols=2, figsize=(10,6))
# 요일별 주문 비율
day_counts = tips["day"].value_counts()
ax4[0].pie(day_counts, labels=day_counts.index, 
        autopct="%1.1f%%", colors=sns.color_palette("pastel"))
ax4[0].set_title("요일별 주문 비율")
# 시간대별 주문 비율
time_counts = tips["time"].value_counts()
ax4[1].pie(time_counts, labels=time_counts.index, 
           autopct="%1.1f%%", colors=sns.color_palette("coolwarm"))
ax4[1].set_title("시간대별 주문 비율")
st.pyplot(fig4)


# 6. 박스 플롯
st.subheader("6. 박스 플롯")
fig5, ax5 = plt.subplots(figsize=(10,6))
sns.boxplot(data=tips, x='day', y='total_bill', ax=ax5)
ax5.set_title("박스 플롯 예시")
st.pyplot(fig5)


# 7. 밀도 플롯
st.subheader("7. 밀도 플롯")
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.kdeplot(tips["total_bill"], fill=True, ax=ax6)
ax6.set_title("총 지불 금액 밀도 플롯")
st.pyplot(fig6)

# 8. 트레일 플롯 : 누적 분포 표현
# 특정 값 이하의 데이터 비율 쉽게 확인
st.subheader("8. 트레일 플롯")
fig7, ax7 = plt.subplots(figsize=(10,6))
sns.ecdfplot(data=tips, x='total_bill', ax=ax7, color='coral')
ax6.set_title("총 지불 금액의 누적 분포", fontsize=14, fontweight='bold')
ax6.set_xlabel("총 지불 금액 ($)")
ax6.set_ylabel("누적 확률")
st.pyplot(fig7)