# Fixed Income Risk Analytics (Python)

A Python project for bond valuation and fixed income risk analysis using discounted cash flow (DCF) methods. The project computes key risk metrics and performs interest rate stress testing across multiple government bonds.

## Overview

This project models fixed income securities using standard financial mathematics and evaluates how bond prices and risk measures change under different interest rate scenarios.

It demonstrates practical understanding of bond pricing, duration, convexity, and interest rate risk.

## Features

- Bond pricing using discounted cash flow (DCF)
- Cash flow generation for coupon bonds
- Macaulay Duration calculation
- Modified Duration calculation
- DV01 (Dollar Value of 1 basis point)
- Convexity calculation
- Interest rate stress testing
- Yield vs Price visualization

## Bonds Analysed

- 7.17 GS 2028  
- 7.18 GS 2033  
- 6.79 GS 2034  

## Technologies Used

- Python  
- Pandas  
- Matplotlib  

## Concepts Used

- Discounted Cash Flow (DCF)
- Yield to Maturity (YTM)
- Bond Pricing
- Macaulay & Modified Duration
- DV01
- Convexity
- Interest Rate Risk
- Stress Testing

## Outputs

- Stress test results in Excel format  
- Price vs Yield curves for each bond (PNG files)

## Future Improvements

- Portfolio-level risk aggregation  
- Yield curve modelling (bootstrapping)  
- Credit spread analysis  
- Interactive dashboard (Streamlit / Plotly)  
- Multi-asset fixed income modelling  

## Assumptions

- Annual coupon payments  
- Flat yield curve (parallel shifts)  
- No taxes or transaction costs  
- No default risk considered  
