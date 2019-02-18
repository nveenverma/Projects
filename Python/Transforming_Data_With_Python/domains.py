def find_domain():
    import read
    import pandas as pd
    df = read.load_data() 
    domainsl = df['url'].value_counts()
    domainsl = domainsl[:99:]
    for k, v in domainsl.items():
        print("{0}: {1}".format(k, v))
    
if __name__ == "__main__":
    find_domain()