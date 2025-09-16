# ?> ./parameters.py
# Number of parameters: 0.
# ?> ./parameters.py "initiation"
# Number of parameters: 1.
# ?> ./parameters.py "this" "is" "crazy" "there's" "everywhere!"
# Number of parameters: 5.
# ?>

import sys

count = len(sys.argv) - 1
print("Number of parameters: %d." %count)

#ยังไม่เสร็จ