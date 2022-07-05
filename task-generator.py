import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,900,size=(2000000000,1)), columns=list('A'))
df.to_csv('tasks/workload.csv', index=False)
