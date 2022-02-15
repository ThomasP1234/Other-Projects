punctuation = ["!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","{","|","}","~"]

class fileCompression():
    def read(self):
        try:
            file = open('data.txt', 'r')
            data = file.read()
            file.close()

            file2 = open('algorithm.txt', 'r')
            data2 = file2.read()
            file2.close()

            data = data.strip('[').strip(']').split(', ')
            newData = []
            for i in data:
                i = i.strip("'")
                newData.append(i)

            data2 = data2.strip('[').strip(']').split(', ')
            newData2 = []
            for i in data2:
                i = i.strip("'")
                newData2.append(i)

            return [newData, newData2]           
        except Exception as e:
            print(e) 
            print('Error reading file')
            return 2
        
    def write(self, data1, data2):
        try:
            file = open('data.txt', 'w')
            file.write(str(data1))
            file.close()

            file2 = open('algorithm.txt', 'w')
            file2.write(str(data2))
            file2.close()
            
            print('Wrote to file')
        except:
            print('Error writing file')
    
    def compress(self):
        userInput = input('Enter the phrase or sentence ').split(' ')
        words = []
        compressed = []
        counter = 0
        for word in userInput:
            hasPunc = False
            for punc in punctuation:
                if punc == "\'":
                    if punc in word:
                        stringVar = ''
                        stringVar += word.replace("\'", 'µApostropheµ')
                        word = stringVar
                elif punc in word:
                    word = word.replace(punc, f"µ_Punc_µ{punc}µ_Punc_µ")
                    word = word.split("µ_Punc_µ")
                    print(word)
                    for j in word:
                        if not(j in words):
                            words.append(j)
                        counter2 = 0
                        for i in words:
                            if j == i:
                                compressed.append(counter2)
                            counter2 += 1
                    hasPunc = True
            if hasPunc == False:    
                if not(word in words):
                    words.append(word)
                counter2 = 0
                for i in words:
                    if word == i:
                        compressed.append(counter2)
                    counter2 += 1
        self.write(words, compressed)
        

    def decompress(self):
        file = self.read()
        if not(file == 2):
            reconstruct = ""
            for i in file[1]:
                if file[0][int(i)] in punctuation:
                    reconstruct = reconstruct[:-1]
                    reconstruct += file[0][int(i)]
                    reconstruct += " "
                else:
                    reconstruct += file[0][int(i)]
                    reconstruct += " "
            print(reconstruct.replace("µApostropheµ", "'"))


    def run(self):
        valid = False
        while not(valid):
            userInput = input('[1] Compress File\n[2] Decompress File\n[3] Quit\n')
            if userInput == '1':
                self.compress()
            elif userInput == '2':
                self.decompress()
            elif userInput == '3':
                valid = True
            else:
                print('Please enter a correct option')

compression = fileCompression()
compression.run()