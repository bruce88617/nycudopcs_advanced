"""Tests of Lecture 01"""

from scripts.testFuncs import test1, test2, test3, testDT1, testDT2, testDT3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lecture 01")
    parser.add_argument("--idx", default=1, type=int, help="Return which test? (default: 1)")
    parser.add_argument("--avail", default=20, type=int, help="Available weight (default: 20)")
    parser.add_argument("--num", default=10, type=int, help="Number of items (default: 10)")
    parser.add_argument("--maxVal", default=200, type=int, help="Maximum item value (default: 200)")
    parser.add_argument("--maxWt", default=200, type=int, help="Maximum item weight (default: 20)")

    opt = parser.parse_args()

    if opt.idx == 1:
        print("Run Test #{}".format(opt.idx))
        test1(availWeight=opt.avail)
    
    elif opt.idx == 2:
        print("Run Test #{}".format(opt.idx))
        test2(availWeight=opt.avail)

    elif opt.idx == 3:
        print("Run Test #{}".format(opt.idx))
        test3(availWeight=opt.avail, numItems=opt.num, mavVal=opt.maxVal, maxWeight=opt.maxWt)

    elif opt.idx == 4:
        print("Run Test #{}".format(opt.idx))
        testDT1(availWeight=opt.avail)

    elif opt.idx == 5:
        print("Run Test #{}".format(opt.idx))
        testDT2(availWeight=opt.avail, numItems=opt.num, mavVal=opt.maxVal, maxWeight=opt.maxWt)

    elif opt.idx == 6:
        print("Run Test #{}".format(opt.idx))
        testDT3(availWeight=opt.avail, numItems=opt.num, mavVal=opt.maxVal, maxWeight=opt.maxWt)

    else:
        raise ValueError("num should be 1, 2, 3, 4, 5, or 6.")
    

