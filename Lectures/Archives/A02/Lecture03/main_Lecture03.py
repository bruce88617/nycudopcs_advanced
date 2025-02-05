"""
Tests of Lecture 03

Part I: Random Walk
"""


import scripts.part1 as p1
import scripts.part2 as p2
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lecture 03")
    parser.add_argument("--p", "--part", default=1, type=int, help="Return which part? (default: 1)")
    parser.add_argument("--num", default=1, type=int, help="Return which test? (default: 1)")
    parser.add_argument("--numTrials", default=100, type=int, help="Number of trials (default: 100)")
    parser.add_argument("--numSteps", default=100, type=int, help="Number of steps (default: 100)")
    parser.add_argument("--name", default="", type=str, help="Name of drunk (default: "")")
    parser.add_argument(
        "--dClass", 
        default=0, 
        type=int, 
        help="Drunk class: 0 for UsualDrunk, 1 for EastWardDrunk, and 2 for HeatAvoidDrunk. (default: 0)"
    )

    opt = parser.parse_args()

    if opt.p == 1:
        # Run Tests in Part I
        if opt.num == 1:
            p1.test1(
                numTrials = opt.numTrials,
                dClass = opt.dClass,
                name = opt.name,
            )
        
        elif opt.num == 2:
            p1.test2(
                numTrials = opt.numTrials,
                dClass = opt.dClass,
                name = opt.name,
            )

        elif opt.num == 3:
            p1.test3(
                numTrials = opt.numTrials,
                name = opt.name,
            )

        elif opt.num == 4:
            p1.test4(
                numTrials = opt.numTrials,
                name = opt.name,
            )

        elif opt.num == 5:
            p1.test5(
                numSteps = opt.numSteps,
                numTrials = opt.numTrials,
                name = opt.name,
            )

        elif opt.num == 6:
            p1.test6(
                numSteps = opt.numSteps,
                name = opt.name,
            )

        elif opt.num == 7:
            p1.test7(
                numSteps = opt.numSteps,
                name = opt.name,
            )

        else:
            raise ValueError("num should be 1, 2, 3, 4, 5, 6, or 7.")

    else:
        # Run Tests in Part II
        if opt.num == 1:
            p2.test1()
        
        elif opt.num == 2:
            p2.test2()

        elif opt.num == 3:
            p2.test3()

        elif opt.num == 4:
            p2.test4()

        elif opt.num == 5:
            p2.test5()

        elif opt.num == 6:
            p2.test6()

        elif opt.num == 7:
            p2.test7()

        elif opt.num == 8:
            p2.test8()

        elif opt.num == 9:
            p2.test9()

        elif opt.num == 10:
            p2.test10()

        else:
            raise ValueError("Test # does not exist.")


