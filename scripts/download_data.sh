#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data

mkdir -p $data

tools=$base/tools

# link default training data for easier access

mkdir -p $data/wikitext-2

for corpus in train valid test; do
    absolute_path=$(realpath $tools/pytorch-examples/word_language_model/data/wikitext-2/$corpus.txt)
    ln -snf $absolute_path $data/wikitext-2/$corpus.txt
done

# download a different interesting data set!

mkdir -p $data/art_of_perfumery

mkdir -p $data/art_of_perfumery/raw

wget https://www.gutenberg.org/cache/epub/16378/pg16378.txt
mv pg16378.txt $data/art_of_perfumery/raw/perfume.txt

# preprocess slightly

cat $data/art_of_perfumery/raw/perfume.txt | python $base/scripts/preprocess_raw.py > $data/art_of_perfumery/raw/perfume.cleaned.txt

# tokenize, fix vocabulary upper bound

cat $data/art_of_perfumery/raw/perfume.cleaned.txt | python $base/scripts/preprocess.py --vocab-size 5000 --tokenize --lang "en" --sent-tokenize > \
    $data/art_of_perfumery/raw/perfume.preprocessed.txt

# split into train, valid and test

head -n 440 $data/art_of_perfumery/raw/perfume.preprocessed.txt | tail -n 400 > $data/art_of_perfumery/valid.txt
head -n 840 $data/art_of_perfumery/raw/perfume.preprocessed.txt | tail -n 400 > $data/art_of_perfumery/test.txt
tail -n 3075 $data/art_of_perfumery/raw/perfume.preprocessed.txt | head -n 2955 > $data/art_of_perfumery/train.txt
