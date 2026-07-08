import streamlit as st
from deep_translator import GoogleTranslator

# تنظیمات اولیه صفحه
st.set_page_config(page_title="مترجم انگلیسی به فارسی", layout="centered")

# تزریق CSS سفارشی برای بارگذاری و اعمال فونت B Nazanin و راست‌چین کردن متن
st.markdown("""
    <style>
    @font-face {
        font-family: 'B Nazanin';
        src: url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/font-face.css'); /* لود فونت جایگزین استاندارد در صورت عدم وجود B Nazanin روی سیستم کاربر */
    }
    
    /* اعمال فونت و راست‌چین کردن باکس نتیجه */
    .farsi-text {
        font-family: 'B Nazanin', 'Arial', sans-serif;
        font-size: 22px;
        direction: rtl;
        text-align: right;
        line-height: 1.6;
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #4CAF50;
        color: #333333;
    }
    
    /* راست‌چین کردن عنوان نتیجه */
    .farsi-title {
        font-family: 'B Nazanin', 'Arial', sans-serif;
        direction: rtl;
        text-align: right;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان برنامه
st.title("🔄 مترجم هوشمند انگلیسی به فارسی")
st.write("متن انگلیسی خود را در باکس زیر وارد کنید تا ترجمه فارسی آن را با فونت بی نازنین دریافت کنید.")

# دریافت متن ورودی از کاربر
user_input = st.text_area("متن انگلیسی (English Text):", placeholder="Type your English text here...")

# دکمه ترجمه
if st.button("ترجمه کن 🚀"):
    if user_input.strip() != "":
        with st.spinner("در حال ترجمه..."):
            try:
                # فرایند ترجمه
                translated_text = GoogleTranslator(source='en', target='fa').translate(user_input)
                
                st.write("---")
                # نمایش عنوان با فونت فارسی
                st.markdown('<h3 class="farsi-title">متن ترجمه شده:</h3>', unsafe_allow_html=True)
                # نمایش نتیجه ترجمه با فونت B Nazanin و استایل سفارشی
                st.markdown(f'<div class="farsi-text">{translated_text}</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"خطایی در فرآیند ترجمه رخ داد: {e}")
    else:
        st.warning("لطفاً ابتدا متنی را برای ترجمه وارد کنید.")