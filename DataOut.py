"""
Basic I/O class that outputs our retrieved results into a text file
"""

def StockValuesOut(filename, valuedict, valuelist):
    with open(filename, "w") as fout:
        fout.write("Test Output\n")
        for v in valuelist:
            fout.write(v+ ": ")
            fout.write(valuedict[v] + "\n")
            # mess around with formatting so output file looks nicer
            # try looking into Python's string.ljust/rjust/center methods


""" Ignore Main Function """
def main():
    print("Main")

if __name__ == "__main__":
    main()
