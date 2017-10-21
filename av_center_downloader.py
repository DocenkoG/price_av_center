# -*- coding: UTF-8 -*-
import os
import logging
import logging.config
import time
import shutil
import pycurl
import io

 

def make_loger():
    global log
    logging.config.fileConfig('logging.cfg')
    log = logging.getLogger('logFile')



# curl -o "C:\AV_PROM\prices\ав_центр\av_center.xls" ftp://diler2:FGfhn@85.249.224.228/PRD.xls
def download( myname ):
    global log
    pathDwnld = './tmp'
    ftp_user_name = 'diler2'
    ftp_user_password = 'FGfhn'
    proxy      = "*****"
    proxy_port = 99999
    proxy_user_name = "*****"
    proxy_user_password = "*****"
    ftp_source = 'ftp://85.249.224.228/PRD.xls'
    new_file   = 'new_av_center.xls'
    old_file   = 'old_av_center.xls'
    make_loger()
    log.debug( 'Begin '   + __name__ + '  downLoader' )

    try:
        buffer = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, ftp_source)
        c.setopt(pycurl.UPLOAD, 0)
#       c.setopt(pycurl.DOWNLOAD, 1)
        c.setopt(pycurl.USERPWD, "%s:%s" % (ftp_user_name, ftp_user_password))
#       c.setopt(pycurl.PROXY, proxy)
#       c.setopt(pycurl.PROXYPORT, proxy_port)
#       c.setopt(pycurl.PROXYUSERPWD, "%s:%s" % (proxy_user_name, proxy_user_password))
#       c.setopt(pycurl.HTTPPROXYTUNNEL, 1)
#       c.setopt(pycurl.READFUNCTION, FileReader(open(source_file, 'rb')).read_callback)
        c.setopt(pycurl.WRITEFUNCTION, buffer.write)
        c.setopt(pycurl.VERBOSE, 1)
        c.perform()
        code = c.getinfo(c.RESPONSE_CODE)
        data = buffer.getvalue()
        datasize = len(data)
        c.close()
        log.debug('datasize='+str(datasize)+'  Code='+str(code) )
        if os.path.exists(old_file):  os.remove(old_file)
        if os.path.exists(new_file):  os.rename(new_file, old_file)
        f2 = open(new_file, 'wb')                                  #Теперь записываем файл
        f2.write(data)
        f2.close()
        log.info('Файл загружен')
        return True

    except pycurl.error as e:
        print('e=<',e,'>')
