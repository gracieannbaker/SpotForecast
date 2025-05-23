# SpotForecast
BIA Columbia Spot price forecasting

This repository contains data and files used to predict the price of energy in the Colombian Spot Market. This project is in progress with BIA, a Colombian Energy Distributer. 

I will detail the files and what they contain. 

# DATA
Input Data.csv contains data from 1 January 2000 to 12 May 2025. 
The Row Labels are the following:
    Row Labels - Date in YYYY-MM-DD
    electric_demand - Colombia's electric demand in GWh
    reservoir_inflows_gwh - Amount of water (energy) that inflows the reservoirs in GWh
    reservoir_inflows_per - Amount of water (energy) that inflows the reservoirs in percentage over the daily average of that specific month (60 years of history).
    reservoir_gwh - Colombia's stored energy on it's reservoirs in GWh
    energy_dumping_gwh - Colombia's dumped energy in GWh
    cere_copkwh - Reliability cost, it's like a tax paid over each consumed kWh, it's internalized on the spot price in COP/kWh.
    spot_price_copkwh - Spot Price in COP/kWh
    scarcity_price_copkwh - Scarcity price, this price acts as a top price for the spot energy transaction. Is form by fuel costs. The spot price can go over the scarcity price but the spot sales and purchases are "techadas" by the scarcity price. In COP/kWh.
    thermo_transport_cost_copkwh - Average cost of transportation of all fuels used to generate thermoelectric energy in COP/kWh
    thermo_supply_cost_copkwh - Average cost of supply of all fuels used to generate thermoelectric energy in COP/kWh

pb_inputs_frcst_dia.csv
Row Labels:
    Fecha - Date in MM/DD/YYYY
    Demanda Comercial - Commercial demand
    ONI - no clue

pb_inputs_real_dia.csv

pb_output_dia.csv

predicciones_DL_inicial.csv

predicciones_PB.csv

sp_forecasting_test.csv

# IPYNBS
hydro_spot_NN.ipynb

hydro_spotML.ipynb

reset.ipynb

tuned_xgboost.ipynb

# Helpers