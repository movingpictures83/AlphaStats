# AlphaStats
# Language: Python
# Input: CSV
# Output: TXT
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy_1.16.0, scipy_1.4.1

PluMA plugin that takes a file of alpha-diversity values
and produces statistics for all groups, and each individual group.
Output will be produced in a TXT file.

The input CSV file is assumed to have columns for: Description (group)
and value.  Files output by PhyloSeq are compatible.
