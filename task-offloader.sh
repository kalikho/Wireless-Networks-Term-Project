#!/bin/bash
python3 offloader/offloader1.py >> logs/offloaders.logs &
python3 offloader/offloader2.py >> logs/offloaders.logs &
python3 offloader/offloader3.py >> logs/offloaders.logs &
python3 offloader/offloader4.py >> logs/offloaders.logs &
