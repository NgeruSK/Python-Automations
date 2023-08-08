import datetime
import shutil
current_time = datetime.datetime.now()
output_filename = 'backup_'+str(current_time)
dir_name = 'test folder'
shutil.make_archive(output_filename, 'zip', dir_name)