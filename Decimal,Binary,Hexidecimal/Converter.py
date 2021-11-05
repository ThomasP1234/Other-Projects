class converter():
    def conversiontype(self):    
        while True:
            try:
                print("[1] Decimal to Binary\n[2] Decimal to Hexidecimal\n[3] Binary to Decimal\n[4] Binary to Hexidecimal\n[5] Hexidecimal to Binary\n[6] Hexidecimal to Decimal\n")
                self.conversion = int(input('Please choose an option from the list above: '))
                if self.conversion < 1 or self.conversion > 6:
                    raise ValueError
                break
            except ValueError as E:
                print("Must enter Numeric Value Between 1 and 6")

    def run(self):
        print("Welcome to a Binary, Decimal, Hexidecimal Conversion Program.")

        self.conversiontype()

runConverter = converter()
runConverter.run()