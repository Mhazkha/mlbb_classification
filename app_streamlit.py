import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_mlbb.joblib")

st.title("MLBB Classification")
kill = st.slider("jumlah kill", 0,20)
assist = st.slider("jumlah assist",0,20)
death = st.slider("jumlah death", 0,20)
turret = st.slider("jumlah turret", 0,20)

if st.button("predict"):
	data_baru = pd.DataFrame([[kill,assist,death,turret]],
			columns=["kill","assist","death","turret"])
	st.success(f"hasi prediksi : {model.predict(data_baru)[0]}")
	st.balloons()