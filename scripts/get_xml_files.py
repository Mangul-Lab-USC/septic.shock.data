from ftplib import FTP
import os
import tarfile


def get_xml(accession, ftp):
    acc_dir = accession[:-2] + 'nnn'
    filename = accession + '_family.xml'
    url = '/geo/series/' + acc_dir + '/' + accession + '/miniml/' + filename + '.tgz'
    with open(url, 'wb') as fp:
        ftp.retrbinary('RETR ' + url, fp.write)

    with tarfile.open(filename + '.tgz', mode='r:gz') as tf:
        tf.extract(filename, path='../raw_data/')

    os.remove(filename + '.tgz')


if __name__ == '__main__':
    ftp = FTP('ftp://ftp.ncbi.nlm.nih.gov')
    ftp.login()

    with open('../raw_data/series_accessions.txt', 'r') as acc_file:
        for accession in acc_file.readlines():
            get_xml(accession.rstrip(), ftp)
    ftp.quit()
