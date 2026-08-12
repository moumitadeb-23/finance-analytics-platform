import pandas as pd

DATASET_PATH = "dataset/credit_card_transactions.csv"

def get_dataset_summary():

    df = pd.read_csv(DATASET_PATH)

    total_transactions = len(df)

    fraud_transactions = int(df["is_fraud"].sum())

    genuine_transactions = total_transactions - fraud_transactions

    fraud_percentage = round(
        (fraud_transactions / total_transactions) * 100,
        4
    )

    average_amount = round(df["amt"].mean(), 2)

    highest_amount = round(df["amt"].max(), 2)

    lowest_amount = round(df["amt"].min(), 2)

    top_categories = (
        df[df["is_fraud"] == 1]["category"]
        .value_counts()
        .head(5)
    )

    top_states = (
        df[df["is_fraud"] == 1]["state"]
        .value_counts()
        .head(5)
    )

    return {

    "total_transactions": total_transactions,

    "fraud_transactions": fraud_transactions,

    "genuine_transactions": genuine_transactions,

    "fraud_percentage": fraud_percentage,

    "average_amount": average_amount,

    "highest_amount": highest_amount,

    "lowest_amount": lowest_amount,

    "categories": top_categories.index.tolist(),

    "category_counts": top_categories.values.tolist(),

    "states": top_states.index.tolist(),

    "state_counts": top_states.values.tolist(),

    "highest_category": top_categories.index[0],

    "highest_category_count": int(top_categories.iloc[0]),

    "highest_state": top_states.index[0],

    "highest_state_count": int(top_states.iloc[0])

}