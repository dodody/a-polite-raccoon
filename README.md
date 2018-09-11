# a-polite-raccoon
대신 예의차려주는 너구리
- - - 
## Deep-Learning
pytorch 0.4.1 && CUDA 9.0 && cudnn 7.1.2 && python 3.6
TrainingData : user-nuguri.txt

### Environment Setup Guide (use anaconda)
1. make conda environment
2. conda install pytorch  <= anaconda can install CUDA, cudnn
3. git clone
4. pip install -requirements.txt

### Making Data-base (use Google's Spread-Sheet)
1. Download Google spread sheet
2. <pre><code> python makeNuguriDB.py [filename] </code><pre>
3. example <pre><code> python makeNuguriDB.py data/nuguridataset.csv </code><pre>
4. check your data folder

### Training Encoder, Decoder
1. <pre><code> python train_model.py </code></pre>
2. check your model folder

### Test Encoder, Decoder
1. <pre><code> python test.py </code></pre>
- - -
