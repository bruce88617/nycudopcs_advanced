"""Tests of Lecture 04"""


from scripts.testFuncs import test1, test2, test3, test4, test5
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lecture 07")
    parser.add_argument("--num", default=1, type=int, help="Return which test? (default: 1)")

    opt = parser.parse_args()

    if opt.num == 1:
        # print("Run Test #{}".format(opt.num))
        test1()
    
    elif opt.num == 2:
        # print("Run Test #{}".format(opt.num))
        test2(numData=1000, numTrials=100, precision=1e-4)

    # elif opt.num == 3:
    #     # print("Run Test #{}".format(opt.num))
    #     test3()

    # elif opt.num == 4:
    #     # print("Run Test #{}".format(opt.num))
    #     test4()

    # elif opt.num == 5:
    #     # print("Run Test #{}".format(opt.num))
    #     test5()

    # elif opt.num == 6:
    #     # print("Run Test #{}".format(opt.num))
    #     test6()

    # elif opt.num == 7:
    #     # print("Run Test #{}".format(opt.num))
    #     test7()

    # elif opt.num == 8:
    #     # print("Run Test #{}".format(opt.num))
    #     test8()

    # elif opt.num == 9:
    #     # print("Run Test #{}".format(opt.num))
    #     test9()

    # elif opt.num == 10:
    #     # print("Run Test #{}".format(opt.num))
    #     test10()

    else:
        raise ValueError("Test # does not exist.")

