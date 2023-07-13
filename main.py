import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Titulo do app
st.title('Stock History App')

# Create a sidebar section for user input [BBAS3.SA / MSFT /]
st.sidebar.title("Selecione o stock:")
ticker_symbol = st.sidebar.text_input("Enter the stock symbol", value='AAPL', max_chars=10)

# Retrieve stock data using yfinance
data = yf.download(ticker_symbol, start="2020-01-01", end="2023-06-26")

# Display the stock data in a dataframe
st.subheader("Stock History")
st.dataframe(data)

# Plot the closing price using Plotly(preço das açoes)
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Closing Price'))
fig.update_layout(title=f"{ticker_symbol} Stock Price", xaxis_title="Date", yaxis_title="Price")
st.plotly_chart(fig)

# Plot the volume using Plotly(volume de negociaçoes)
fig_volume = go.Figure()
fig_volume.add_trace(go.Scatter(x=data.index, y=data['Volume'], name='Volume'))
fig_volume.update_layout(title=f"{ticker_symbol} Stock Volume", xaxis_title="Date", yaxis_title="Volume")
st.plotly_chart(fig_volume)