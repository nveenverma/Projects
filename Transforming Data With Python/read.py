def load_data():
    import pandas as pd
    data = pd.read_csv("hn_stories.csv", names = ["submission_time", "upvotes", "url", "headline"])
    return (data)

if __name__ == "__main__":
    load_data()