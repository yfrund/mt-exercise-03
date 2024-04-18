#! /bin/bash

scripts=$(dirname "$0")
base=$(realpath $scripts/..)

models=$base/models
data=$base/data
tools=$base/tools

mkdir -p $models

num_threads=4
device=""

SECONDS=0

(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python3 main.py --data $data/art_of_perfumery \
        --epochs 40 \
        --log-interval 100 \
        --emsize 250 --nhid 250 --dropout 0.9 --tied \
        --save $models/model09.pt \
	--logfiles $models/logs/model09
)

echo "time taken:"
echo "$SECONDS seconds"
