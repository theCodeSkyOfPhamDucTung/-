import streamlit as st
import sqlite3
import pandas
import time
#Nền
connection = sqlite3.connect("data.db", check_same_thread = False)
control = connection.cursor()
control.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT, vocabulary TEXT, typeVb TEXT, mean TEXT)")
connection.commit()
def add_vocabulary(vocabulary, typeVb, mean):
    control.execute("INSERT INTO data(vocabulary, typeVb, mean) VALUES (?, ?, ?)", (vocabulary, typeVb, mean))
    connection.commit()
def show_vocabulary():
    control.execute("SELECT * FROM data")
    return control.fetchall()
def change_vocabulary(n_vocabulary, n_typeVb, n_mean, select_id):
    control.execute("UPDATE data SET vocabulary = ?, typeVb = ?, mean = ? WHERE id = ?", (n_vocabulary, n_typeVb, n_mean, select_id))
    connection.commit()
#Giao diện và tính năng
st.set_page_config(page_icon = "profile-icon-design-free-vector.jpg", page_title = "Demo đường cong lãng quên")
st.title("Hello World")
with st.sidebar:
    st.header("Menu")
    menu = st.radio("Chọn, nhanh", ["Chép từ vựng", "Xem từ vựng", "Sửa từ vựng"])
if menu == "Chép từ vựng":
    with st.form(key = "one", clear_on_submit = True):
        st.header("Nhập từ mới")
        col1, col2, col3 = st.columns([3, 1, 2], gap = "small")
        with col1:
            st.write("Từ mới")
            vocabulary1 = []
            for i in range(10):
                new_vocabulary = st.text_input(f"Từ vựng {i+1}")
                vocabulary1.append(new_vocabulary)
        with col2:
            st.write("Kiểu từ")
            typeVb1 = []
            for i in range(10):
                new_typeVb = st.text_input(f"Kiểu từ {i+1}")
                typeVb1.append(new_typeVb)
        with col3: 
            st.write("Nghĩa")
            mean1 = []
            for i in range(10):
                new_mean = st.text_input(f"Nghĩa {i+1}")
                mean1.append(new_mean)
        submit_button1 = st.form_submit_button("Xác nhận")
        if submit_button1:
            less = False
            for i in range(10):
                if vocabulary1[i].strip() == "" or typeVb1[i].strip() == "" or mean1[i].strip() == "":
                    less = True
                    break
            if less == True:
                st.warning("Nhập thiếu")
            else:
                st.success("Thêm thành công")
                for vocabulary, typeVb, mean in zip(vocabulary1, typeVb1, mean1):
                    add_vocabulary(vocabulary, typeVb, mean)
if menu == "Xem từ vựng":
    ram_data = show_vocabulary()
    st.table(ram_data)
if menu == "Sửa từ vựng":
    with st.form(key = "two", clear_on_submit = True):
        select_id = st.text_input("Nhập số thứ tự từ vựng")
        n_vocabulary = st.text_input("Nhập từ vựng thay thế")
        n_typeVb = st.text_input("Nhập loại từ thay thế")
        n_mean = st.text_input("Nhập nghĩa thay thế")
        submit_button2 = st.form_submit_button("Xác nhận")
        if submit_button2:
            change_vocabulary(n_vocabulary, n_typeVb, n_mean, select_id)
    # st.header("Ko có gì :>")
    # st.write("Để xem cả :3")
    
connection.close()
