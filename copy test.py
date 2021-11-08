import shutil
import os
    
source_dir = 'C:\code-tests\move-test'
target_dir = 'C:\code-tests\move-test-2'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
