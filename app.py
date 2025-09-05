import streamlit as st
import pandas as pd
import joblib
import time

# Load model & scaler
model = joblib.load("model_pony.joblib")
scaler = joblib.load("scaler_pony.joblib")

# Konfigurasi halaman
st.set_page_config(page_title="Pony Character Prediction", layout="centered")

# CSS custom + animasi karakter
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(-45deg, #ffdde1, #ee9ca7, #fad0c4, #ffd1ff);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .main {
        background-color: #ffffffcc;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
    }

    .prediction {
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        padding: 15px;
        border-radius: 15px;
    }

    /* Fluttershy */
    .fluttershy {
        background: rgba(255, 236, 179, 0.8);
        color: #ff69b4;
        animation: flutter 2s infinite alternate;
    }
    @keyframes flutter {
        from { transform: scale(1); }
        to { transform: scale(1.1); }
    }

    /* Rainbow Dash */
    .rainbow {
        background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 32px;
        font-weight: bold;
        animation: rainbow 2s linear infinite;
    }
    @keyframes rainbow {
        from { filter: hue-rotate(0deg); }
        to { filter: hue-rotate(360deg); }
    }

    /* Pinkie Pie */
    .pinkie {
        background: #ffe6f0;
        color: #ff1493;
        animation: bounce 1s infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    /* Twilight Sparkle */
    .twilight {
        background: #d1c4e9;
        color: #4a148c;
        text-shadow: 0 0 10px #ba68c8, 0 0 20px #ab47bc;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 5px #ba68c8, 0 0 10px #ab47bc; }
        to { text-shadow: 0 0 20px #7b1fa2, 0 0 30px #6a1b9a; }
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

    # Efek animasi sesuai karakter
    if "Rainbow" in prediksi:
        st.markdown(f"<div class='prediction rainbow'>🌈 Kamu penuh energi seperti Rainbow Dash! 🚀</div>", unsafe_allow_html=True)
    elif "Twilight" in prediksi:
        st.markdown(f"<div class='prediction twilight'>📖 Pintar & bijak seperti Twilight Sparkle ✨</div>", unsafe_allow_html=True)
    elif "Pinkie" in prediksi:
        st.markdown(f"<div class='prediction pinkie'>🎉 Fun & ceria kayak Pinkie Pie! 🎂</div>", unsafe_allow_html=True)
    elif "Rarity" in prediksi:
        st.markdown("<div class='prediction'>💎 Elegan & stylish seperti Rarity 👗</div>", unsafe_allow_html=True)
    elif "Fluttershy" in prediksi:
        st.markdown(f"<div class='prediction fluttershy'>🌸 Lembut & penuh kasih sayang seperti Fluttershy 🦋</div>", unsafe_allow_html=True)
    elif "Applejack" in prediksi:
        st.markdown("<div class='prediction'>🍎 Jujur & pekerja keras seperti Applejack 🤠</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='prediction'>✨ Kamu unik, seperti pony spesial lainnya! ✨</div>", unsafe_allow_html=True)

    # Progress bar + tingkat keyakinan
    st.progress(presentase)
    st.success(f"Tingkat keyakinan: {presentase*100:.2f}%")

    # Efek tambahan
    st.snow()
    st.balloons()

# Sidebar
st.sidebar.title("Tentang Quiz")
st.sidebar.info("Quiz ini dibuat untuk seru-seruan ✨. Jawabanmu akan dibandingkan dengan kepribadian karakter di My Little Pony 🦄.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:14px;'>🌸 Dibuat dengan ❤️ oleh Aydes 🌸</p>", unsafe_allow_html=True)
