# a-polite-raccoon
대신 예의차려주는 너구리
- - - 
## Deep-Learning
pytorch 0.4.1 && CUDA 9.0 && cudnn 7.1.2 && python 3.6

### 1. Environment Setup Guide (use anaconda)
(1) make conda environment
(2) conda install pytorch  <= anaconda can install CUDA, cudnn
(3) git clone
(4) pip install -requirements.txt

### 2. Making Data-base (use Google's Spread-Sheet)
(1) Download Google spread sheet and excute makeNuguriDB.py
<pre><code> python makeNuguriDB.py [filename] </code></pre>
(2) example 
<pre><code> python makeNuguriDB.py data/nuguridataset.csv </code></pre>
(3) check your data folder, then you can find user-nuguri.txt.(needed for training)

### 3. Training
(1) 
<pre><code> python train.py </code></pre>
(2) check your model folder, then you can find seq2seq model.pkl (needed for test)

### 4. Test
(1) 
<pre><code> python test.py [input sentence]</code></pre>
(2) example
<pre><code> python test.py 지랄하지마 </code></pre>

- - -
