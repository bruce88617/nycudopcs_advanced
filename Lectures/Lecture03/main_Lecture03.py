"""Tests of Lecture 03"""

from scripts.testFuncs import test1, test2, test3, test4, test5, test6, test7
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lecture 03")
    parser.add_argument("--num", default=1, type=int, help="Return which test? (default: 1)")

    opt = parser.parse_args()

    if opt.num == 1:
        # print("Run Test #{}".format(opt.num))
        test1()
    
    elif opt.num == 2:
        # print("Run Test #{}".format(opt.num))
        test2()

    elif opt.num == 3:
        # print("Run Test #{}".format(opt.num))
        test3()

    elif opt.num == 4:
        # print("Run Test #{}".format(opt.num))
        test4()

    elif opt.num == 5:
        # print("Run Test #{}".format(opt.num))
        test5()

    elif opt.num == 6:
        # print("Run Test #{}".format(opt.num))
        test6()

    elif opt.num == 7:
        # print("Run Test #{}".format(opt.num))
        test7()

    else:
        raise ValueError("num should be 1, 2, 3, 4, or 5.")

