"""
Basic I/O class that outputs our retrieved results into a text file
"""

def StockValuesOut(filename, dict, valuelist):
    with open(filename, "w") as fout:
        fout.write("Test Output\n")
        for v in valuelist:
            fout.write(v+"\n")

def main():
    print("Main")

if __name__ == "__main__":
    main()
