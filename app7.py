

import streamlit as st
import pandas as pd
import joblib




# Load the model and data
model = joblib.load('traffic_congestion_model.pkl')
data = pd.read_csv('cleaned_data_for_web_2.csv')

# Set up the title of the web app
st.write("# Traffic Congestion Prediction For London")

# Define your mappings
direction_of_travel_mapping = {'E': 0, 'N': 1, 'S': 2, 'W': 3}
local_authority_name_mapping = {'Barking and Dagenham': 0, 'Barnet': 1, 'Bexley': 2, 'Brent': 3, 'Bromley': 4, 'Camden': 5, 'City of London': 6, 'Croydon': 7, 'Ealing': 8, 'Enfield': 9, 'Greenwich': 10, 'Hackney': 11, 'Hammersmith and Fulham': 12, 'Haringey': 13, 'Harrow': 14, 'Havering': 15, 'Hillingdon': 16, 'Hounslow': 17, 'Islington': 18, 'Kensington and Chelsea': 19, 'Kingston upon Thames': 20, 'Lambeth': 21, 'Lewisham': 22, 'Merton': 23, 'Newham': 24, 'Redbridge': 25, 'Richmond upon Thames': 26, 'Southwark': 27, 'Sutton': 28, 'Tower Hamlets': 29, 'Waltham Forest': 30, 'Wandsworth': 31, 'Westminster': 32}  # Complete this with all mappings





road_name_mapping = {'A1': 0, 'A10': 1, 'A100': 2, 'A1000': 3, 'A1003': 4, 'A1004': 5, 'A1005': 6, 'A1006': 7, 'A1008': 8, 'A1009': 9, 'A101': 10, 'A1010': 11, 'A1011': 12, 'A102': 13, 'A1020': 14, 'A103': 15, 'A1037': 16, 'A104': 17, 'A105': 18, 'A1055': 19, 'A106': 20, 'A1069': 21, 'A107': 22, 'A1080': 23, 'A1081': 24, 'A1083': 25, 'A109': 26, 'A11': 27, 'A110': 28, 'A111': 29, 'A1110': 30, 'A1112': 31, 'A112': 32, 'A113': 33, 'A114': 34, 'A115': 35, 'A1153': 36, 'A116': 37, 'A117': 38, 'A118': 39, 'A1199': 40, 'A12': 41, 'A1200': 42, 'A1201': 43, 'A1202': 44, 'A1203': 45, 'A1205': 46, 'A1206': 47, 'A1207': 48, 'A1208': 49, 'A1209': 50, 'A1210': 51, 'A1211': 52, 'A123': 53, 'A124': 54, 'A1240': 55, 'A125': 56, 'A1251': 57, 'A1261': 58, 'A1263': 59, 'A127': 60, 'A13': 61, 'A1306': 62, 'A1400': 63, 'A2': 64, 'A20': 65, 'A200': 66, 'A2000': 67, 'A2001': 68, 'A201': 69, 'A2015': 70, 'A2016': 71, 'A2018': 72, 'A202': 73, 'A2022': 74, 'A203': 75, 'A2039': 76, 'A204': 77, 'A2041': 78, 'A2043': 79, 'A205': 80, 'A206': 81, 'A207': 82, 'A208': 83, 'A209': 84, 'A21': 85, 'A210': 86, 'A211': 87, 'A212': 88, 'A213': 89, 'A214': 90, 'A215': 91, 'A216': 92, 'A217': 93, 'A218': 94, 'A219': 95, 'A2198': 96, 'A2199': 97, 'A22': 98, 'A220': 99, 'A2203': 100, 'A2205': 101, 'A2206': 102, 'A2208': 103, 'A2209': 104, 'A221': 105, 'A2210': 106, 'A2211': 107, 'A2212': 108, 'A2213': 109, 'A2214': 110, 'A2215': 111, 'A2216': 112, 'A2217': 113, 'A2218': 114, 'A222': 115, 'A223': 116, 'A224': 117, 'A23': 118, 'A232': 119, 'A233': 120, 'A234': 121, 'A235': 122, 'A236': 123, 'A237': 124, 'A238': 125, 'A239': 126, 'A24': 127, 'A240': 128, 'A243': 129, 'A244': 130, 'A297': 131, 'A298': 132, 'A3': 133, 'A30': 134, 'A300': 135, 'A3000': 136, 'A3002': 137, 'A3003': 138, 'A3004': 139, 'A3005': 140, 'A3006': 141, 'A3008': 142, 'A301': 143, 'A302': 144, 'A3031': 145, 'A3036': 146, 'A304': 147, 'A3044': 148, 'A305': 149, 'A306': 150, 'A3063': 151, 'A307': 152, 'A308': 153, 'A309': 154, 'A310': 155, 'A311': 156, 'A3113': 157, 'A312': 158, 'A313': 159, 'A314': 160, 'A315': 161, 'A316': 162, 'A3200': 163, 'A3201': 164, 'A3202': 165, 'A3203': 166, 'A3204': 167, 'A3205': 168, 'A3207': 169, 'A3209': 170, 'A3210': 171, 'A3211': 172, 'A3212': 173, 'A3213': 174, 'A3214': 175, 'A3216': 176, 'A3217': 177, 'A3218': 178, 'A3219': 179, 'A3220': 180, 'A4': 181, 'A40': 182, 'A400': 183, 'A4000': 184, 'A4001': 185, 'A4003': 186, 'A4005': 187, 'A4006': 188, 'A4007': 189, 'A4008': 190, 'A401': 191, 'A402': 192, 'A4020': 193, 'A404': 194, 'A406': 195, 'A407': 196, 'A408': 197, 'A4088': 198, 'A4089': 199, 'A409': 200, 'A4090': 201, 'A41': 202, 'A410': 203, 'A411': 204, 'A4125': 205, 'A4127': 206, 'A4140': 207, 'A4180': 208, 'A4200': 209, 'A4201': 210, 'A4202': 211, 'A4204': 212, 'A4205': 213, 'A4206': 214, 'A4207': 215, 'A4208': 216, 'A4209': 217, 'A437': 218, 'A4380': 219, 'A5': 220, 'A5000': 221, 'A501': 222, 'A502': 223, 'A503': 224, 'A504': 225, 'A5100': 226, 'A5109': 227, 'A5135': 228, 'A5150': 229, 'A5200': 230, 'A5201': 231, 'A5202': 232, 'A5203': 233, 'A5204': 234, 'A5205': 235, 'A598': 236, 'B100': 237, 'B104': 238, 'B106': 239, 'B108': 240, 'B109': 241, 'B111': 242, 'B114': 243, 'B116': 244, 'B118': 245, 'B119': 246, 'B121': 247, 'B126': 248, 'B1335': 249, 'B135': 250, 'B137': 251, 'B138': 252, 'B140': 253, 'B142': 254, 'B1421': 255, 'B144': 256, 'B1452': 257, 'B1453': 258, 'B1461': 259, 'B153': 260, 'B154': 261, 'B160': 262, 'B161': 263, 'B165': 264, 'B168': 265, 'B174': 266, 'B175': 267, 'B177': 268, 'B179': 269, 'B186': 270, 'B187': 271, 'B191': 272, 'B192': 273, 'B193': 274, 'B2030': 275, 'B2032': 276, 'B207': 277, 'B208': 278, 'B210': 279, 'B212': 280, 'B213': 281, 'B214': 282, 'B215': 283, 'B2158': 284, 'B216': 285, 'B2173': 286, 'B218': 287, 'B219': 288, 'B221': 289, 'B2212': 290, 'B222': 291, 'B2230': 292, 'B224': 293, 'B228': 294, 'B229': 295, 'B230': 296, 'B232': 297, 'B234': 298, 'B235': 299, 'B236': 300, 'B237': 301, 'B238': 302, 'B241': 303, 'B242': 304, 'B243': 305, 'B251': 306, 'B252': 307, 'B258': 308, 'B263': 309, 'B265': 310, 'B266': 311, 'B271': 312, 'B272': 313, 'B273': 314, 'B275': 315, 'B276': 316, 'B277': 317, 'B278': 318, 'B279': 319, 'B280': 320, 'B281': 321, 'B282': 322, 'B283': 323, 'B3003': 324, 'B302': 325, 'B304': 326, 'B306': 327, 'B310': 328, 'B317': 329, 'B319': 330, 'B321': 331, 'B323': 332, 'B324': 333, 'B326': 334, 'B3364': 335, 'B349': 336, 'B350': 337, 'B351': 338, 'B352': 339, 'B353': 340, 'B358': 341, 'B361': 342, 'B363': 343, 'B377': 344, 'B400': 345, 'B402': 346, 'B406': 347, 'B408': 348, 'B409': 349, 'B412': 350, 'B413': 351, 'B414': 352, 'B4491': 353, 'B4492': 354, 'B451': 355, 'B452': 356, 'B453': 357, 'B454': 358, 'B455': 359, 'B4557': 360, 'B456': 361, 'B461': 362, 'B465': 363, 'B466': 364, 'B467': 365, 'B469': 366, 'B472': 367, 'B483': 368, 'B501': 369, 'B502': 370, 'B506': 371, 'B507': 372, 'B509': 373, 'B510': 374, 'B511': 375, 'B515': 376, 'B517': 377, 'B519': 378, 'B521': 379, 'B550': 380, 'B552': 381, 'C': 382, 'M1': 383, 'M11': 384, 'M25': 385, 'M4': 386, 'M41': 387, 'U': 388}  # Complete this with all mappings



road_type_mapping = {'Major': 0, 'Minor': 1}
congestion_level_mapping = {'blockage': 0, 'congested': 1, 'highly_congested': 2, 'slightly_congested': 3, 'smooth': 4}


# Reverse the congestion_level_mapping to create a decoder
congestion_level_decoder = {v: k for k, v in congestion_level_mapping.items()}

# Define a function to get filtered roads based on the selected local authority
def get_filtered_roads(local_authority):
    return data[data['local_authority_name'] == local_authority]['road_name'].unique()

# Define a function to get the road type for a given road name
def get_road_type(road_name):
    road_info = data[data['road_name'] == road_name].iloc[0]
    return road_info['road_type']  # Adjust this if your column name is different

# Create columns for the layout
col1, col2, col3 = st.columns(3)

# Get user inputs
direction_of_travel = col1.selectbox("Direction of Travel", list(direction_of_travel_mapping.keys()), key='direction_of_travel_select')
hour = col2.select_slider("Select hour of the day", options=[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], key='hour_select')
region_name = col3.selectbox("Select Region", ['London'], key='region_select')
local_authority_name = col1.selectbox("Local Authority", list(local_authority_name_mapping.keys()), key='local_authority_select')

# Dynamically get the filtered road names based on the selected local authority
filtered_road_names = get_filtered_roads(local_authority_name)
selected_road_name = col2.selectbox("Road Name", filtered_road_names, key='road_name_select')

# Automatically get and display the road type for the selected road
for _ in range(2):  # Adjust the range to add more or less space
    col3.write("")
selected_road_type = get_road_type(selected_road_name)

road_type_container = col3.empty()  # Create a placeholder
road_type_container.info(f"Road Type: {selected_road_type}")  # Update the placeholder with road type info

# Prepare the user inputs for prediction
if st.button('Predict'):
    inputs = [
        direction_of_travel_mapping.get(direction_of_travel, -1),
        hour,
        0,  # For 'London' in 'region_name'
        local_authority_name_mapping.get(local_authority_name, -1),
        road_name_mapping.get(selected_road_name, -1),
        road_type_mapping.get(selected_road_type, -1)
    ]
    df_pred = pd.DataFrame([inputs], columns=['direction_of_travel', 'hour', 'region_name', 'local_authority_name', 'road_name', 'road_type'])
    
    prediction = model.predict(df_pred)
    congestion_pred = congestion_level_decoder.get(int(prediction[0]), 'Unknown')
    st.write(f"Predicted Congestion Level: {congestion_pred}")

