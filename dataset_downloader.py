import pandas as pd
from google_play_scraper import reviews

all_reviews = []
token = None

while True:
    batch, token = reviews(
        "de.hafas.android.db",
        lang="de",
        country="de",
        count=200,
        continuation_token=token
    )

    if not batch:
        break

    all_reviews.extend(batch)

    print(len(all_reviews))

    if token is None:
        break

pd.DataFrame(all_reviews).to_csv("db_navigator_reviews.csv", index=False)