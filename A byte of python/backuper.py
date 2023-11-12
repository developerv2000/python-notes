import time
import os

system_seperator = os.sep
sources = ['D:\\Bob\\books', 'D:\\Bob\\avas']
backup_dir = 'D:\\Bob\\backups'

today = time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(backup_dir + system_seperator + today):
    os.mkdir(backup_dir + system_seperator + today)

backup_name = backup_dir + system_seperator + today + system_seperator + now + '.zip'

zip_command = 'zip -qr {0} {1}'.format(backup_name, ' '.join(sources))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в:', backup_dir)
else:
    print('Ошибка. Создание резервной копии не удалось!')

