# Streamlit Documentation: https://docs.streamlit.io/


import pickle
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# Title/Text
st.title("Car Price Prediction :car: :dollar:")
st.text("findout the price of your car")


# Dataframe
df = pd.read_csv("Ready_to_ML.csv")

# To load machine learning model
filename = "my_model"
model = pickle.load(open(filename, "rb"))

# To take feature inputs
# defining variables for user input
available_make_models = ('Mercedes-Benz A 180', 'Opel Astra', 'Opel Corsa', 'Opel Adam',
                         'Opel Insignia', 'Opel Cascada', 'Opel Grandland X',
                         'Renault Megane', 'Renault Clio', 'Renault Captur',
                         'Renault Talisman', 'Renault Kadjar', 'Peugeot 308', 'Peugeot 208',
                         'Peugeot 207', 'Peugeot 3008', 'Peugeot 508', 'Peugeot RCZ',
                         'Peugeot 206', 'Peugeot 2008', 'Fiat 500', 'Fiat Tipo',
                         'Fiat 500X', 'Fiat Panda', 'Fiat 500C', 'SEAT Leon', 'SEAT Ibiza',
                         'SEAT Arona', 'SEAT Ateca', 'Skoda Octavia', 'Skoda Scala',
                         'Skoda Fabia', 'Skoda Superb', 'Skoda Kodiaq', 'Skoda Karoq',
                         'Dacia Sandero', 'Dacia Logan', 'Dacia Duster', 'Toyota Yaris',
                         'Toyota Corolla', 'Toyota Aygo', 'Toyota Auris', 'Toyota C-HR',
                         'Toyota RAV 4', 'Nissan Micra', 'Nissan Qashqai', 'Nissan Juke',
                         'Nissan Pulsar', 'Nissan 370Z', 'Nissan 350Z', 'Nissan X-Trail',
                         'Ford Fiesta', 'Ford Focus', 'Ford Mondeo', 'Ford Kuga',
                         'Ford Mustang', 'Hyundai i30', 'Hyundai i20', 'Hyundai IONIQ',
                         'Hyundai TUCSON', 'Volvo V40',
                         'Volvo C30', 'Volvo C70',
                         'Volvo XC60', 'Volvo XC90', 'Volvo S90', 'Volvo XC40', 'Volvo V90',
                         'Volvo V60', 'Volvo S60')

make_model = st.selectbox('What is the make_model?', available_make_models)
power_kW = st.slider("What is the power_kW?", 43, 419, step=1)
mileage = st.slider("What is the mileage?", 0, 415000, step=1)
age = st.slider("What is the car age?", 0, 20, step=1)
engine_size = st.slider("What is the engine_size?", 0, 5812, step=1)
car_type = st.radio("What's your favorite movie genre",
                    ('Used', 'Pre-registered', 'Demonstration', "Employee's car")
                    )


# Create a dataframe using feature inputs
my_dict = {
    "make_model": make_model,
    "power_kW": power_kW,
    "mileage": mileage,
    "age": age,
    "engine_size": engine_size,
    "type": car_type
}

df = pd.DataFrame.from_dict([my_dict])
st.dataframe(df, use_container_width=True, hide_index=True, column_config={
    "make_model": "Make Model",
    "power_kW": "Power kW",
    "mileage": st.column_config.NumberColumn(
        "Mileage",
        format="%d Miles"),
    "age": st.column_config.NumberColumn(
        "Age",
        format="%d Years"),
    "engine_size": "Engine Size",
    "type": "Car Type"
})

# Prediction with user inputs
predict = st.button("Predict :dollar:")
result = model.predict(df)
if predict:
    st.toast('Predicting....', icon='⌛️')
    st.success("{:.2f} :dollar:".format(result[0], 2))
    st.button('reset result', type='primary')
