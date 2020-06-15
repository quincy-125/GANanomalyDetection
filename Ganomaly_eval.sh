#!/bin/env bash
#$ -N ganomaly
#$ -q gpu
#$ -l gpu=1
#$ -o outlog
#$ -e errlog
#$ -M hart.steven@mayo.edu 
#$ -m ae
#$ -notify
#$ -V
#$ -cwd
#$ -l h_vmem=125G

python /research/bsi/projects/PI/tertiary/Hart_Steven_m087494/s211408.DigitalPathology/Code/GANanomalyDetection/eval.py
