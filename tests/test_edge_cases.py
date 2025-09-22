# Small sanity tests—keep these lightweight and readable.

import pandas as pd

def test_first_year_growth_is_nan():
    df = pd.DataFrame({"country":["X","X"], "year":[2019,2020], "population":[100,110]})
    df = df.sort_values(["country","year"])
    df["yoy_growth_pct"] = df.groupby("country")["population"].pct_change() * 100
    assert df["yoy_growth_pct"].isna().iloc[0]

