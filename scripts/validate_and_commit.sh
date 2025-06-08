#!/bin/bash
python dump_anchor_meta.py && jq '.[].id' anchor_meta_dump.json | sort | uniq -d