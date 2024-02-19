import streamlit as st

st.set_page_config(
    page_title="Chrono Manager GUI",
    page_icon="✍️",
    layout="centered",
)


st.title("ChronoManager GUI")

events_tab, create_event_tab, login_tab = st.tabs(
    ["Мои события", "Созадть событие", "Логин"]
)


with events_tab:
    st.header("Список событий")
    st.write("**Здесь будет список событий**")

with create_event_tab:
    st.header("Новое событие")

    title = st.text_input("Event title")
    description = st.text_input("Event description")
    expire_date = st.date_input("Event date")
    expire_time = st.time_input("Event time")
    notify_before = st.selectbox(
        "За какое время напомнить?", ("30 мин.", "1 час", "1,5 часа", "2 часа")
    )

    show_res = st.button("Show event data", type="primary")
    if show_res:
        st.write(f"title: {title}")
        st.write(f"description: {description}")
        st.write(f"expire_date: {expire_date}")
        st.write(f"expire_time: {expire_time}")
        st.write(f"notify_before: {notify_before}")

with login_tab:
    st.header("Войдите под своей учетной записью")
    with st.form("my_form"):
        login_val = st.text_input("Логин")
        pwd_val = st.text_input("Пароль")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Логин", login_val, "пароль", pwd_val)

        st.write("Не помню пароль")
