def read_data():
    from collections import Counter
    import read
    df = read.load_data()
    
    hl_col = df.loc[:,'headline']
    s = ""
    
    for i in hl_col:
        s += (str(i).strip() + " ")
    
    new_s = s.split(" ")
    cnt = Counter(new_s)
    print (cnt.most_common(100))    
    
if __name__ == "__main__":
    read_data()