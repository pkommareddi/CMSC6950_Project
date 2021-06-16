from pymagicc.io import MAGICCData


def write_delimited(data: MAGICCData, filename, delimiter=',', header=True, index=False, append=False):
    '''
    Write a MAGICCData object as a delimited text file to disk
    '''
    mode = 'a' if append else 'w'
    data = data.timeseries().reset_index()
    data.to_csv(filename, sep=delimiter, header=header, index=index, mode=mode)
