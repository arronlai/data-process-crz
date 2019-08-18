# a demo to process data for Chen

# Folder structure
    1. data/: input datasets here
    2. dist/: result will be here (.npy is binary file, need to read with python, another file is txt, but it doesn't have structure of array)
    3. log/: track log here, you can verify if all the steps give right result

# Parameters
    1. file_name, default is XDATCAR: You will be asked to give the file name of your dataset, if you don't input anything, it will be XDATCAR, and the output file will be named as cov_file_name (default is cov_XDATCAR)
    2. distance, default is 3: It will be used to calculate the metrix
    3. debug_mode, default is False: you can set it to be ture to get log file of all steps in log/, so that you can check if the calculated result is correct after each step