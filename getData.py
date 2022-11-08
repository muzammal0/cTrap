import os
import shutil

user = os.getlogin()
file_names = ['ndns', 'dns', 'nds', 'ds']
for i in range(len(file_names)):
    print(file_names[i])
    file_path = '/home/' + user + '/' + file_names[i] + '.txt'
    dest_dir = '/home/' + user + '/copydata_' + file_names[i] + '/'
    home_dir = '/home/' + user + '/'
    src_dir = '/home/' + user + '/camera_trap/data_root/done/'

    try:
        with open(file_path) as f:
            uuids = f.readlines()
            for m in range(len(uuids)):
                uuids[m] = uuids[m].replace('-', '')
                folder_src = (src_dir + uuids[m]).rstrip('\r\n ')
                try:
                    shutil.copytree(folder_src, (dest_dir + uuids[m]))
                    print("Folder copied")
                except Exception as e:
                    print("Folder not found")
                    # with open(home_dir + file_names[i] + '_' + user + '_notfounds.txt', 'a+') as f:
                    # f.write(str(uuids[m]))

            shutil.make_archive(home_dir + 'data_' + user + '_' + file_names[i], 'zip', root_dir=dest_dir)
            print("Folder Zipped")
            shutil.rmtree(dest_dir)

    except Exception as e:
        print(e)
