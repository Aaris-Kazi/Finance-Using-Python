from finance_value import finance
from plotter import actual, overall
from predictor import *
from os import path

def main():
    test = path.exists('google.csv')
    if(test):
        banner = "1: To load csv (GOOGLE)\n 2: Get Info \n 3: Graph of Stonks \n 4: Graph of Overall \n 5: Predict the Graph"
        print(banner)
        s = int(input('Select Value:'))
        df = pd.read_csv('google.csv')
        if s == 1:
            finance()
        elif s == 2:
            print(df.info())
        elif s == 3:
            actual(df['Date'], df['Close'])
        elif s == 4:
            overall(df)
        elif s == 5:
            # forsvm()
            forlinear()
        else:
            print('Please CHoose the option in the given value')
        
    else:
        print('file not exist')
        finance()

    
if __name__ == "__main__":
    main()

