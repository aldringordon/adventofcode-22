from Program.CalorieCounter import CalorieCounter

def max_calories():
    cc = CalorieCounter()
    cc.read_and_convert("Day1-CalorieCounting/Data.txt")
    print(cc.get_max_val())
    cc.remove_max()
    print(cc.get_max_val())
    cc.remove_max()
    print(cc.get_max_val())

def main():
    max_calories()

if __name__=="__main__":
    main()