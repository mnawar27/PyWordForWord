import string
class wordforword:

    def __init__(self):
        self.worddict = {}
        self.letterdict = {}
        self.lines = []
        self.linecount = 0
        self.wordcount = 0
        self.lettercount = 0

    #---PRINT----
    def doprint(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                self.lines.append(line.strip()) 
    
        print(self.lines)
        return self.lines
    
    #---WORD COUNT----
    def wc(self):
        num_lines = len(self.lines)
    
        for line in self.lines:
            line = line.translate(str.maketrans('', '', string.punctuation))
            spline = line.split()
            print(spline)
            self.wordcount += len(spline)
            self.lettercount += len("".join(spline))

        print(num_lines, self.wordcount, self.lettercount)
        return (num_lines, self.wordcount, self.lettercount)

if __name__ == "__main__":

    c = wordforword()
    file = "/Users/mnawar/Desktop/Projects2/PyWordForWord/testdata/testdata0.txt"

    c.doprint(file)
    c.wc()

