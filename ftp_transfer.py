import ftplib
session = ftplib.FTP('ftp.cea.fr','ftp','ondrej.mandula@cea.fr')
file = open('STOR testftp.txt','rb')                  # file to send
session.storbinary('/incoming/y2k01/test_ondrej/testftp_python.txt', file)     # send the file
file.close()                                    # close file and FTP
session.quit()


import ftplib
session = ftplib.FTP('ftp.cea.fr','ftp','ondrej.mandula@cea.fr')
file = open('testftp.txt','rb')                  # file to send
session.storbinary('STOR '+'/incoming/y2k01/test_ondrej/temp_ext_plot.py', file)
file.close()                                    # close file and FTP
session.quit()

