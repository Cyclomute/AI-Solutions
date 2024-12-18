{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bc1b699c-d620-4aec-8915-c06412393288",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-12-16 23:15:25.930 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Load the saved model\n",
    "model = joblib.load('flowerspecieprediction.pkl')\n",
    "\n",
    "# Title and Description\n",
    "st.title(\"Iris Flower Species Predictor\")\n",
    "st.write(\"Enter the features of an iris flower to predict its species.\")\n",
    "\n",
    "# Input Fields\n",
    "sepal_length = st.number_input(\"Sepal Length (cm)\", min_value=0.0, step=0.1)\n",
    "sepal_width = st.number_input(\"Sepal Width (cm)\", min_value=0.0, step=0.1)\n",
    "petal_length = st.number_input(\"Petal Length (cm)\", min_value=0.0, step=0.1)\n",
    "petal_width = st.number_input(\"Petal Width (cm)\", min_value=0.0, step=0.1)\n",
    "\n",
    "# Prediction Button\n",
    "if st.button(\"Predict\"):\n",
    "    # Prepare the input data as a NumPy array\n",
    "    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])\n",
    "    \n",
    "    # Make a prediction\n",
    "    prediction = model.predict(input_data)\n",
    "    \n",
    "    # Map prediction to species name\n",
    "    iris_species = [\"Setosa\", \"Versicolor\", \"Virginica\"]\n",
    "    species = iris_species[prediction[0]]\n",
    "    \n",
    "    # Display result\n",
    "    st.success(f\"The predicted species is: {species}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1a15233-5357-4d9f-a552-a9b2ba39b352",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
