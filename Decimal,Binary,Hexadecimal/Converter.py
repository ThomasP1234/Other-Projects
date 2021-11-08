class converter():
    def conversion_type(self):
        while True:
            try:
                print("[1] Decimal to binary\n[2] Decimal to hexadecimal\n[3] Binary to decimal\n[4] Binary to hexadecimal\n[5] Hexadecimal to binary\n[6] Hexadecimal to decimal\n[7] Quit\n")
                self.conversion = int(input('Please choose an option from the list above: '))
                if self.conversion < 1 or self.conversion > 7:
                    raise ValueError
                return
            except ValueError as E:
                print("Must enter a numeric value between 1 and 7")
    
    def convert(self):
        if self.conversion == 1:
            self.conversion_one()
        elif self.conversion == 2:
            self.conversion_two()
        elif self.conversion == 3:
            self.conversion_three()
        elif self.conversion == 4:
            self.conversion_four()
        elif self.conversion == 5:
            self.conversion_five()
        elif self.conversion == 6:
            self.conversion_six()
        else:
            print("Goodbye")
            exit()

    def repetition_request(self):
        for i in range(10):
            try:
                print("[1] Convert Again\n[2] Quit Program\n")
                self.again = int(input('Please choose an option from the list above: '))
                if self.again < 1 or self.again > 2:
                    raise ValueError
                return
            except ValueError as E:
                print("Must enter either 1 or 2")
        print("Too many invalid attempts - Conversion aborted")

    def conversion_one(self):
        decimal = int(input("Please enter the decimal number: "))
        binary = bin(decimal)
        print(f"The decimal number {decimal} in binary is: {binary[2:]}")

    def conversion_two(self):
        decimal = int(input("Please enter the decimal number: "))
        hexNum = hex(decimal)
        print(f"The decimal number {decimal} in hexadecimal is: #{hexNum[2:]}")

    def conversion_three(self):
        binary = int(input("Please enter the binary number: "))
        decimal = int(str(binary), 2)
        print(f"The binary number {binary} in decimal is: {decimal}")

    def conversion_four(self):
        binary = int(input("Please enter the binary number: "))
        decimal = int(str(binary), 2)
        hexNum = hex(decimal)
        print(f"The binary number {binary} in hexadecimal is: #{hexNum[2:]}")

    def conversion_five(self):
        for i in range(10):
            try:
                hexNum = input("Please enter the hexadecimal number: #")
                decimal = int(hexNum, 16)
                binary = bin(decimal)
                print(f"The hexadecimal number #{hexNum} in binary is: {binary[2:]}")
                return
            except ValueError:
                "Invalid hexadecimal value - Please try again"
        print("Too many invalid attempts - Conversion aborted")

    def conversion_six(self):
        for i in range(10):
            try:
                hexNum = input("Please enter the hexadecimal number: #")
                decimal = int(hexNum, 16)
                print(f"The hexadecimal number #{hexNum} in decimal is: {decimal}")
                return
            except ValueError:
                "Invalid hexadecimal value - Please try again"
        print("Too many invalid attempts - Conversion aborted")

    def run(self):
        self.again = True
        while self.again == True:
            print("Welcome to a binary, decimal, hexadecimal conversion program.")

            self.conversion_type()
            self.convert()
            self.repetition_request()
        print("Goodbye")

runConverter = converter()
runConverter.run()