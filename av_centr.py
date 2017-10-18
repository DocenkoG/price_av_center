# -*- coding: UTF-8 -*-
import os
import os.path
import logging
import logging.config
import io
import sys
import configparser
import time
import av_centr_downloader
import av_centr_converter
import shutil

global log
global myname



def make_loger():
    global log
    logging.config.fileConfig('logging.cfg')
    log = logging.getLogger('logFile')



def main( ):
    global  myname
    global  mydir
   
    make_loger()
    log.info('------------  '+ myname +'  - начало обработки ------------')

    if  av_centr_downloader.download( myname ) :
#        log.info('Конвертация xlsx для исправления формата xlsx')
#        os.system( myname + '_converter_xlsx.xlsm')
        av_centr_converter.convert2csv( myname )
        shutil.copy2( myname + '.csv', 'c://AV_PROM/prices/' + myname +'/'+ myname + '.csv')
    log.info('------------  '+ myname +'  - обработка завершена ------------')
    if os.path.exists('python.log'):
        shutil.copy2( 'python.log',    'c://AV_PROM/prices/' + myname +'/python.log')



if __name__ == '__main__':
    global  myname
    global  mydir
    myname   = os.path.basename(os.path.splitext(sys.argv[0])[0])
    mydir    = os.path.dirname (sys.argv[0])
    if ('' != mydir) : os.chdir(mydir)
    main( )
 
#os.system(r'c:\prices\_scripts\remove_tmp_profiles.cmd')