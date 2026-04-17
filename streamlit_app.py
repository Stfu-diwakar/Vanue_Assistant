import streamlit as st
import plotly.express as px
import pandas as pd
import time
import folium
from streamlit_folium import st_folium
from streamlit_lottie import st_lottie

from utils.routing import get_best_route
from utils.queue import predict_wait_time
from ai.chatbot import ask_ai
from assets.animations import load_lottie

st.set_page_config(
    page_title="Smart Venue Assistant",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 100%;
}

.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 15px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.2);
}

.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    background: linear-gradient(90deg,#ff4b4b,#ff9f43);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Smart Venue Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered crowd intelligence system</div>', unsafe_allow_html=True)

lottie = load_lottie("https://assets2.lottiefiles.com/packages/lf20_touohxv0.json")
if lottie:
    st_lottie(lottie, height=180)

st.divider()

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Navigation", "Queue", "Map", "Assistant"]
)

if menu == "Dashboard":

    st.subheader("Live Stadium Insights")

    col1, col2, col3 = st.columns([1,1,1], gap="large")

    with col1:
        st.markdown('<div class="card">Crowd Density <h2>72%</h2></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">Avg Wait <h2>6 mins</h2></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">Active Gates <h2>4</h2></div>', unsafe_allow_html=True)

    st.divider()

    df = pd.DataFrame({
        "Time": ["10:00", "10:30", "11:00", "11:30", "12:00"],
        "Crowd": [30, 50, 75, 60, 80]
    })

    fig = px.line(df, x="Time", y="Crowd", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    zone_df = pd.DataFrame({
        "Zone": ["Gate A", "Gate B", "Food Court", "Seats"],
        "Density": [80, 40, 65, 70]
    })

    fig2 = px.bar(zone_df, x="Zone", y="Density")
    st.plotly_chart(fig2, use_container_width=True)

elif menu == "Navigation":

    st.subheader("Smart Route Finder")

    start = st.selectbox("Start Location", ["Gate 1", "Gate 2", "Food Court"])
    end = st.selectbox("Destination", ["Seat A", "Washroom", "Exit"])

    if st.button("Find Route"):
        with st.spinner("Calculating"):
            time.sleep(1)

        route = get_best_route(start, end)
        st.markdown(f'<div class="card">{route}</div>', unsafe_allow_html=True)

elif menu == "Queue":

    st.subheader("Queue Prediction")

    location = st.selectbox("Select Location", ["Food Stall 1", "Washroom A"])

    if st.button("Check Wait Time"):
        with st.spinner("Analyzing"):
            time.sleep(1)

        wait_time = predict_wait_time(location)

        st.markdown(f"""
        <div class="card">
            Estimated Wait Time
            <h1>{wait_time} mins</h1>
        </div>
        """, unsafe_allow_html=True)

elif menu == "Map":

    st.subheader("Live Crowd Map")

    m = folium.Map(location=[28.6, 77.2], zoom_start=16)

    folium.CircleMarker(
        location=[28.6005, 77.2005],
        radius=15,
        color="red",
        fill=True,
        popup="High Crowd"
    ).add_to(m)

    folium.CircleMarker(
        location=[28.601, 77.201],
        radius=10,
        color="green",
        fill=True,
        popup="Low Crowd"
    ).add_to(m)

    st_folium(m, width=400)

elif menu == "Assistant":

    st.subheader("AI Assistant")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_input = st.text_input("Ask about venue")

    if st.button("Send"):
        if user_input:
            response = ask_ai(
                user_input,
                context="Gate 1 crowded, Food Court moderate"
            )

            st.session_state.chat.append(("You", user_input))
            st.session_state.chat.append(("AI", response))

    for role, msg in st.session_state.chat:
        if role == "You":
            st.markdown(f"User: {msg}")
        else:
            st.markdown(f"Assistant: {msg}")
