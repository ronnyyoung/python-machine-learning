import ftplib 
import os
import socket
 
HOST = '10.10.40.92'
USER = 'libang'
PASSWD = '18853734036'
 
def FtpConnect(host, username, passwd):
	try:
		ftp = ftplib.FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print('Error, cannot reach ' + HOST, e)
		return
	else:
		print('Connect To Host Success...')
		
	try:
		ftp.login(USER, PASSWD)
	except ftplib.error_perm:
		print('Username or Passwd Error')
		ftp.quit()
		return
	else:
		print('Login Success...')
	
	return ftp
 
def FtpDownload(ftp, remotepath, localpath):
	try:
		ftp.retrbinary('RETR %s' % remotepath, open(localpath, 'wb').write)
	except ftplib.error_perm:
		print('File Error')
		os.unlink(localpath)
	else:
		print('Download Success...')
	ftp.quit()
 
def FtpUpload(ftp, remotepath, localpath):
	try:
		ftp.storbinary('STOR %s' %remotepath, open(localpath, 'rb'))
	except ftplib.error_perm:
		print('File Error')
		os.unlink(localpath)
	else:
		print('Upload Success...')
	ftp.quit()
 
if __name__ == '__main__':
    ftp = FtpConnect('10.5.36.31', 'yangyansheng', '6aH9aAQtrYpf93A')
	#FtpDownload(ftp, './5.rar', '222.rar')  # 上传