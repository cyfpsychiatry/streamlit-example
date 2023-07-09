import streamlit as st
st.title('抗抑郁药效预测辅助决策系统')
# 页面选择
page = st.sidebar.radio('页面选择', ['首页', '患者基本资料', '心理量表评分', '基因测序基因型', '结果'])
