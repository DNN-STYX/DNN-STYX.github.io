# [](#header-1) **Get Start with STYX**

## [](#header-1)***1. Setup***

Environment Requirement:

*   <font color="#0000FF" size="4">Ubuntu 16.04, CUDA=10.1, cuDNN=7.6, gcc＝4.8</font>

Python Package:

*   <font color="#0000FF" size="4">tensorflow-gpu=1.13.0, keras, xlrd, pillow, pandas, xlutils, matplotlib</font>

## [](#header-1)***2. Example***

Examples of using STYX can be found in [**Github Repo**](https://github.com/DNN-STYX/DNN-STYX.github.io/tree/master/demo). It provides an example for training the MLP models w.r.t. MNIST benchmark under three different methods (traditional training, mutation training, and adversarial training) and then making the robustness evaluation. The example can be run with the following command, which takes about 15 mins:

```
cd Examples
bash run_example.sh
```
In more detail, we consider that in three steps:

## [](#header-1) (1) model's description

```
cd STYX/traditional_training
```
First we need to provide the model's structure like [**Train\_mnist\_MLP.py**](https://www.baidu.com/)  in the current folder. 


## [](#header-1) (2) model's generation
Given the paramters like model\_name="mnist\_MLP" and train\_epoch=20. Next we use the following command to generate the models by different training method.

### [](#header-1) (2.1) traditional_training

```
cd STYX/traditional_training
python traditional_training.py $model_name $train_epoch
```
### [](#header-1) (2.2) mutation_training

```
cd STYX/mutation_training
python mutation_training.py $model_name $train_epoch 
```
### [](#header-1) (2.3) adversarial_training

```
cd STYX/adversarial_training
python adversarial_training.py $model_name $train_epoch
```

## [](#header-1) (3) model's evaluation
After that, we use the following command to evaluate the models by different attacking method. Take the attacking method "FGM" as example:

```
cd STYX/evaluation  
python evaluation.py ["FGM"]
```

And the evaluation result is stored in evaluation.xls under evaluation folder.