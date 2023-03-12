string = 'Swoją drogą to gdzie rośnie               pieprz?'+" \t       "

import re
string = re.sub('\W+',' ', string)
print(f'|{string.split(" ")}|')