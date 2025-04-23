{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a21cfbd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e1f28c28",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'logisticmodel.pkl'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m model \u001b[38;5;241m=\u001b[39m joblib\u001b[38;5;241m.\u001b[39mload(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlogisticmodel.pkl\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m      2\u001b[0m st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTitanic Survival Prediction\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32mB:\\Data Science Course\\Anaconda\\Lib\\site-packages\\joblib\\numpy_pickle.py:650\u001b[0m, in \u001b[0;36mload\u001b[1;34m(filename, mmap_mode)\u001b[0m\n\u001b[0;32m    648\u001b[0m         obj \u001b[38;5;241m=\u001b[39m _unpickle(fobj)\n\u001b[0;32m    649\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m--> 650\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(filename, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[0;32m    651\u001b[0m         \u001b[38;5;28;01mwith\u001b[39;00m _read_fileobject(f, filename, mmap_mode) \u001b[38;5;28;01mas\u001b[39;00m fobj:\n\u001b[0;32m    652\u001b[0m             \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(fobj, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    653\u001b[0m                 \u001b[38;5;66;03m# if the returned file object is a string, this means we\u001b[39;00m\n\u001b[0;32m    654\u001b[0m                 \u001b[38;5;66;03m# try to load a pickle file generated with an version of\u001b[39;00m\n\u001b[0;32m    655\u001b[0m                 \u001b[38;5;66;03m# Joblib so we load it with joblib compatibility function.\u001b[39;00m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'logisticmodel.pkl'"
     ]
    }
   ],
   "source": [
    "model = joblib.load('logisticmodel.pkl')\n",
    "st.title(\"Titanic Survival Prediction\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a594e000",
   "metadata": {},
   "outputs": [],
   "source": [
    "pclass = st.selectbox(\"Passenger Class\", [1, 2, 3])\n",
    "sex = st.selectbox(\"Sex\", [\"male\", \"female\"])\n",
    "age = st.slider(\"Age\", 1, 80, 25)\n",
    "sibsp = st.number_input(\"Siblings/Spouses Aboard\", 0, 8, 0)\n",
    "parch = st.number_input(\"Parents/Children Aboard\", 0, 6, 0)\n",
    "fare = st.number_input(\"Fare\", 0.0, 600.0, 32.0)\n",
    "embarked = st.selectbox(\"Port of Embarkation\", [\"C\", \"Q\", \"S\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a9810f09",
   "metadata": {},
   "outputs": [],
   "source": [
    "sex = 1 if sex == \"male\" else 0\n",
    "embarked_map = {\"C\": 0, \"Q\": 1, \"S\": 2}\n",
    "embarked_val = embarked_map[embarked]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7506c236",
   "metadata": {},
   "outputs": [],
   "source": [
    "input_data = np.array([[pclass, age, sibsp, parch, fare, sex, embarked_val]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "fd4a2e9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(input_data)\n",
    "    result = \"Survived\" if prediction[0] == 1 else \"Did not survive\"\n",
    "    st.subheader(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
