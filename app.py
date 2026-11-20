import streamlit as st

def analyze_sentiment(text):
    text_lower = text.lower()
    
    # 定義正面與負面的關鍵字詞
    very_positive_words = ['非常好', '太棒了', '完美', '超級好用', '100分', '極力推薦', 'excellent', 'perfect', 'awesome']
    positive_words = ['好用', '不錯', '推薦', '喜歡', '滿意', 'good', 'nice', 'like']
    negative_words = ['不好', '不推薦', '普通', '普通而已', '差', '爛', '失望', 'bad', 'disappointed', 'normal']
    very_negative_words = ['非常差', '極度失望', '垃圾', '再也不買', '爛透了', 'terrible', 'worst', 'awful']
    
    score = 3 # 預設為普通
    
    if any(word in text_lower for word in very_positive_words):
        score = 5
    elif any(word in text_lower for word in positive_words):
        score = 4
    elif any(word in text_lower for word in very_negative_words):
        score = 1
    elif any(word in text_lower for word in negative_words):
        score = 2
        
    return score

# Streamlit 網頁介面設計
st.title("📝 產品評論情緒分析器")
st.write("請在下方輸入文字，系統將會為您評估該評論的情緒等級（1至5星）。")

# 接收輸入文字
user_input = st.text_area("請輸入產品評論文字：", placeholder="例如：這產品非常好用，強烈推薦！")

if st.button("開始分析"):
    if user_input.strip() == "":
        st.warning("請先輸入一些文字！")
    else:
        # 進行情緒分析
        rating = analyze_sentiment(user_input)
        
        # 依分數顯示不同的結果與顏色視覺效果
        st.subheader("分析結果：")
        
        star_mapping = {
            1: "⭐ (非常差)",
            2: "⭐⭐ (差)",
            3: "⭐⭐⭐ (普通)",
            4: "⭐⭐⭐⭐ (好)",
            5: "⭐⭐⭐⭐⭐ (非常好)"
        }
        
        st.metric(label="情緒評分等級", value=f"{rating} / 5")
        st.info(f"詳細評價：{star_mapping[rating]}")

# 預設測試範例
with st.expander("💡 查看測試範例"):
    st.markdown("* **5星級評價**: '這產品非常好用，用過之後就回不去了，超級推薦！'\n* **4星級評價**: '產品還不錯，品質還可以，推薦購買。'\n* **3星級評價**: '用起來感覺普通，沒有想像中的驚艷。'\n* **2星級評價**: '有點失望，品質不太好，不怎麼推薦。'\n* **1星級評價**: '這真的是爛透了，極度失望，千萬不要買！'")