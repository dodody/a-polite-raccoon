# a-polite-raccoon
대신 예의차려주는 너구리
- - - 
## Deep-Learning
pytorch 0.4.1 && python 3.6

### 1. Environment Setup Guide ( AWS T2 instance )
1. Download "Nuguri.pem" https://drive.google.com/open?id=1yMMtW_pSSSIkgzYmfHPn8q-OumGGlxCH 
2. Move folder which has "Nuguri.pem" , if your "Nuguri.pem" file located in Downloads folder,
<pre><code> cd Downloads </code></pre>
3. Try ssh connection  
<pre><code> ssh -i "Nuguri.pem" ubuntu@ec2-34-215-156-12.us-west-2.compute.amazonaws.com </code></pre>
4. If 1~3 finished, you can access AWS T2 instance.
5. Check a-polite-raccoon folder.

### 2. Making Data-base ( Use Google's Spread-Sheet )
1. Download Google spread sheet and excute makeNuguriDB.py
<pre><code> python makeNuguriDB.py [filename] </code></pre>
2. Example 
<pre><code> python makeNuguriDB.py data/nuguridataset.csv </code></pre>
3. Check your data folder, then you can find user-nuguri.txt.(need to train)

### 3. Training
1. Excute train.py 
<pre><code> python train.py </code></pre>
2. Check your model folder, then you can find seq2seq model.pkl (need to test)

### 4. Test
1. Excute test.py
<pre><code> python test.py [input sentence]</code></pre>
2. Example
<pre><code> python test.py 이런 XX야 XXXX </code></pre>

- - -
