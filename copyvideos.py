import shutil, os, sys, datetime

def main(source_dir, target_dir):
    walk_dir(source_dir, target_dir)

def walk_dir(dir_path, target_dir):
    for dir_name, subdirs, filenames in os.walk(dir_path):
        for file_name in filenames:
            if is_video(file_name):
                copy_video(os.path.join(dir_name, file_name), target_dir)
        for subdir in subdirs:
            walk_dir(subdir, target_dir)

def is_video(file_name):
    return file_name.lower()[-4:] in ('.mov', '.mp4')

def copy_video(file_path, target_dir):
    c_time = create_time(file_path)
    file_target_dir = os.path.join(target_dir, c_time.strftime('%Y-%m-%d'))
    if not os.path.exists(file_target_dir):
        os.makedirs(file_target_dir)
    if not os.path.exists(os.path.join(file_target_dir, os.path.basename(file_path))):
        print('copying %s to %s' % (file_path, file_target_dir))
        shutil.copy(file_path, file_target_dir)

def create_time(file_path):
    t = os.path.getctime(file_path)
    return datetime.datetime.fromtimestamp(t)

if __name__=='__main__':
    source_dir = sys.argv[1]
    target_dir =  sys.argv[2]
    main(source_dir, target_dir)
