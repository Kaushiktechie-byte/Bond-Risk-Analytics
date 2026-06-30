
import os

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"


import pandas as pd

# -----------------------------
# BOND DATA
# -----------------------------

bonds = pd.DataFrame({
    "Bond": [
        "7.17 GS 2028",
        "7.18 GS 2033",
        "6.79 GS 2034"
    ],
    "Coupon": [
        0.0717,
        0.0718,
        0.0679
    ],
    "YTM": [
        0.0620,
        0.0662,
        0.0663
    ],
    "Years": [
        2,
        7,
        8
    ]
})

FACE = 100

# -----------------------------
# CASHFLOW TABLE
# -----------------------------

def create_bond_table(face, coupon_rate, ytm, maturity):

    coupon = face * coupon_rate

    years = list(range(1, maturity + 1))

    cashflows = [coupon] * maturity

    cashflows[-1] += face

    table = pd.DataFrame({
        "Year": years,
        "Cashflow": cashflows
    })

    table["Discount Factor"] = (
        1 / ((1 + ytm) ** table["Year"])
    )

    table["PV"] = (
        table["Cashflow"]
        * table["Discount Factor"]
    )

    table["tPV"] = (
        table["Year"]
        * table["PV"]
    )

    return table


# -----------------------------
# BOND ANALYTICS
# -----------------------------

def analyze_bond(face, coupon_rate, ytm, maturity):

    table = create_bond_table(
        face,
        coupon_rate,
        ytm,
        maturity
    )

    price = table["PV"].sum()

    macaulay_duration = (
        table["tPV"].sum()
        / price
    )

    modified_duration = (
        macaulay_duration
        / (1 + ytm)
    )

    dv01 = (
        modified_duration
        * price
        * 0.0001
    )

    table["Convexity Term"] = (
        table["Cashflow"]
        * table["Year"]
        * (table["Year"] + 1)
        /
        ((1 + ytm) ** (table["Year"] + 2))
    )

    convexity = (
        table["Convexity Term"].sum()
        / price
    )

    return {
        "Price": round(price, 4),
        "Duration": round(macaulay_duration, 4),
        "Modified Duration": round(modified_duration, 4),
        "DV01": round(dv01, 6),
        "Convexity": round(convexity, 4)
    }

def stress_test_bond(face, coupon_rate, ytm, maturity, shocks):

    stress_results = []

    for shock in shocks:
        metrics = analyze_bond(face, coupon_rate, ytm + shock, maturity)

        stress_results.append([
            shock,
            metrics["Price"],
            metrics["Duration"],
            metrics["Modified Duration"],
            metrics["DV01"],
            metrics["Convexity"]
        ])

    return pd.DataFrame(
        stress_results,
        columns=[
            "Shock",
            "Price",
            "Duration",
            "Modified Duration",
            "DV01",
            "Convexity"
        ]
    )

shocks = [-0.02, -0.01, 0, 0.01, 0.02]

result = stress_test_bond(
    FACE,
    0.0717,
    0.0620,
    2,
    shocks
)

print(result)


