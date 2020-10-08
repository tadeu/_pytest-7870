#!/usr/bin/env bash
pytest . --import-mode=importlib -s --no-header --no-summary >pytest-output.txt
pytest a b --import-mode=importlib -s --no-header --no-summary >pytest-output-multiple-roots.txt
python manual.py >manual-output.txt
diff -u manual-output.txt pytest-output.txt >diff1.txt
diff -u manual-output.txt pytest-output-multiple-roots.txt >diff2.txt
