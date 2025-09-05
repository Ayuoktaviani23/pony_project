import streamlit as st
import pandas as pd
import joblib
import time

# Load model & scaler
model = joblib.load("model_pony.joblib")
scaler = joblib.load("scaler_pony.joblib")

# CSS custom
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f6d5f7 0%, #fbe9d7 100%);
    }
    .main {
        background-color: #ffffffcc;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
    }
    .stButton button {
        background: linear-gradient(90deg, #ff9aeb, #a97fff);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #a97fff, #ff9aeb);
        transform: scale(1.05);
    }
    footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul
st.markdown("<h1 style='text-align: center; color: purple;'>🦄 Personality Quiz - My Little Pony</h1>", unsafe_allow_html=True)
st.write("✨ Jawab pertanyaan di bawah ini untuk tahu kamu mirip dengan pony siapa! ✨")

# Pertanyaan (slider)
st.subheader("📋 Pertanyaan Kepribadian")

membaca = st.slider("📚 Seberapa sering kamu suka membaca buku?", 0, 10, 5)
bercanda = st.slider("😂 Apakah kamu suka bercanda / humor?", 0, 10, 5)
olahraga = st.slider("🏃 Seberapa aktif kamu dalam olahraga?", 0, 10, 5)
berpenampilan = st.slider("👗 Seberapa peduli kamu dengan penampilan / fashion?", 0, 10, 5)
jujur = st.slider("🤝 Seberapa jujur kamu dalam kehidupan sehari-hari?", 0, 10, 5)
baik_hati = st.slider("💖 Apakah kamu orang yang baik hati?", 0, 10, 5)
kreatif = st.slider("🎨 Seberapa kreatif kamu dalam ide / karya?", 0, 10, 5)
petualang = st.slider("🌍 Apakah kamu suka tantangan dan petualangan?", 0, 10, 5)
pendiam = st.slider("😶 Seberapa pendiam / introvert kamu?", 0, 10, 5)
loyal = st.slider("🛡️ Seberapa loyal / setia kamu terhadap teman?", 0, 10, 5)
memimpin = st.slider("👑 Apakah kamu lebih suka menjadi pemimpin?", 0, 10, 5)
kerjasama = st.slider("🤗 Seberapa baik kamu bekerja dalam tim / kerjasama?", 0, 10, 5)

# Prediksi
if st.button("🔮 Lihat Hasil"):
    data_baru = pd.DataFrame([[membaca, bercanda, olahraga, berpenampilan, jujur,
                               baik_hati, kreatif, petualang, pendiam, loyal,
                               memimpin, kerjasama]],
                             columns=["membaca","bercanda","olahraga","berpenampilan","jujur",
                                      "baik_hati","kreatif","petualang","pendiam","loyal",
                                      "memimpin","kerjasama"])
    data_baru_scaled = scaler.transform(data_baru)

    # Prediksi
    prediksi = model.predict(data_baru_scaled)[0]
    presentase = max(model.predict_proba(data_baru_scaled)[0])

    # Loading animasi
    with st.spinner("🔮 Meramal kepribadianmu..."):
        time.sleep(2)

    # Hasil
    st.markdown(f"<h2 style='color:#a020f0;'>✨ Kamu mirip dengan <b>{prediksi}</b>! ✨</h2>", unsafe_allow_html=True)
    st.progress(presentase)
    st.success(f"Tingkat keyakinan: {presentase*100:.2f}%")

    # Efek animasi sesuai karakter
    if "Rainbow" in prediksi:
        st.markdown("🌈 WOW! Kamu penuh energi seperti Rainbow Dash! 🚀")
    elif "Twilight" in prediksi:
        st.markdown("📖 Pintar & bijak seperti Twilight Sparkle ✨")
    elif "Pinkie" in prediksi:
        st.markdown("🎉 Fun & ceria kayak Pinkie Pie! 🎂")
    elif "Rarity" in prediksi:
        st.markdown("💎 Elegan & stylish seperti Rarity 👗")
    elif "Fluttershy" in prediksi:
        st.markdown("🌸 Lembut & penuh kasih sayang seperti Fluttershy 🦋")
    elif "Applejack" in prediksi:
        st.markdown("🍎 Jujur & pekerja keras seperti Applejack 🤠")
    else:
        st.markdown("✨ Kamu unik, seperti pony spesial lainnya! ✨")

    # Efek tambahan selain balon
    st.snow()
    st.balloons()

# Sidebar
st.sidebar.title("Tentang Quiz")
st.sidebar.info("Quiz ini dibuat untuk seru-seruan ✨. Jawabanmu akan dibandingkan dengan kepribadian karakter di My Little Pony 🦄.")

# Footer
st.markdown("<footer>🌸 Dibuat dengan ❤️ oleh Aydes 🌸</footer>", unsafe_allow_html=True)
