import os
import json
import numpy

def mkdir(folder): 
    if not os.path.exists(folder):
            os.makedirs(folder)


def process(fo):
    dataset = []
    for i in range(24): 
        dataset.append([])
    line = fo.readline()
    while line:
        if 'direct configuration' in line.lower():
            for i in range(288):
                line = fo.readline()
            for j in range(24):
                line = fo.readline()
                dataset[j].append(line.split())
        line = fo.readline()
    return dataset

def cdis(d1, d2):
    sum = 0
    for i in range(3):
        sum += pow(float(d1[i]) - float(d2[i]), 2)
    return pow(sum, 0.5)

def calc_dis(dataset):
    result = []
    for j, data in enumerate(dataset):
        result.append([])
        for i in range(len(data) - 1):
            result[j].append(cdis(data[i], data[i+1]))
    return result

def transform(dis_sets, d):
    result = []
    for dis_set in dis_sets:
        tmp = []
        for dis in dis_set:
            if dis > d:
                tmp.append(1)
            else:
                tmp.append(0)
        result.append(tmp)
    return result

# dsize = int(raw_input('Amount of cells: ') or 3816)
fname = raw_input('File name (default is XDATCAR): ') or 'XDATCAR'
distance = int(raw_input('Distance (default is 3): ') or 3)
debug = bool(raw_input('Debug Mode (default is false): '))

readfo = open('./data/' + fname, 'r')
dataset = process(readfo)
if debug:
    mkdir('./log')
    mkdir('./log/step1_cells')
    for ix, d in enumerate(dataset, start=1):
        log1 = open('./log/step1_cells/log_process_file_to_data'+str(ix), 'w')
        log1.write(json.dumps(d))
        log1.close
dis_set = calc_dis(dataset)
if debug:
    mkdir('./log/step2_distance')
    log2 = open('./log/step2_distance/log_calc_distance_of_cells', 'w')
    log2.write(json.dumps(dis_set))
    log2.close
dis_metrix = transform(dis_set, distance)
if debug:
    mkdir('./log/step3_metrix')
    log3 = open('./log/step3_metrix/log_transform_metrix_from_distance', 'w')
    log3.write(json.dumps(dis_metrix))
    log3.close
cov_metrix = numpy.cov(dis_metrix)
mkdir('./dist')
afname = './dist/cov_of_' + fname
resultfo = open(afname, 'w')

resultfo.close
numpy.set_printoptions(suppress=True)
numpy.savetxt(afname, cov_metrix, fmt='%.09f', delimiter=',')
numpy.save(afname, cov_metrix)
readfo.close
