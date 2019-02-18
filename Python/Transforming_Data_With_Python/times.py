def get_hour():
    import read
    from dateutil.parser import parse
    
    df = read.load_data()
    df["hours"] = df["submission_time"].apply(lambda x: parse(x).hour)
    print(df["hours"].value_counts())
    
    #print(df["hours"])
    
if __name__ == "__main__":
    get_hour()
    
    