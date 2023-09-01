 
#these are the examples in Chapters 3 and 4 along with working through Module 2

import statistics
from util_logger import setup_logger

logger, logname = setup_logger(__file__)

dataA = [10, 11, 14, 20, 20, 20, 22, 24, 28, 31]
dataB = [2, 9, 13, 14, 20, 20, 24, 26, 32, 40]

meanA = statistics.mean(dataA)
medianA = statistics.median(dataA)
modeA = statistics.mode(dataA)

meanB = statistics.mean(dataB)
medianB = statistics.median(dataB)
modeB = statistics.mode(dataB)

stdevA = statistics.stdev(dataA)
pstdevA = statistics.pstdev(dataA)
stdevB = statistics.stdev(dataB)
pstdevB = statistics.pstdev(dataB)

varianceA = statistics.variance(dataA)
pvarianceA = statistics.pvariance(dataA)
varianceB = statistics.variance(dataB)
pvarianceB = statistics.pvariance(dataB)

logger.info(f"The mean of dataA is: {meanA}")
logger.info(f"The median of dataA is: {medianA}")
logger.info(f"The mode of dataA is: {modeA}")

logger.info(f"The mean of dataB is: {meanB}")
logger.info(f"The median of dataB is: {medianB}")
logger.info(f"The mode of dataB is: {modeB}")

logger.info(f"The standard deviation for dataA is: {stdevA}")
logger.info(f"The population standard deviatioin for dataA is:{pstdevA}")
logger.info(f"The variance for dataA is: {varianceA}")
logger.info(f"The population variance for dataA is: {pvarianceA}")


logger.info(f"The standard deviation for dataB is: {stdevB}")
logger.info(f"The population standard deviatioin for dataB is:{pstdevB}")
logger.info(f"The variance for dataB is: {varianceB}")
logger.info(f"The population variance for dataB is: {pvarianceB}")



