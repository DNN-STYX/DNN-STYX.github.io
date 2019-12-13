# [](#header-1) **Get Start with STYX**

## [](#header-1)***1. Setup***

Environment Requirement:

*   <font color="#0000FF" size="4">Ubuntu 16.04, CUDA=10.1, cuDNN=7.6, gcc＝4.8</font>

Python Package:

*   <font color="#0000FF" size="4">tensorflow-gpu=1.13.0, keras, xlrd, pillow, pandas, xlutils, matplotlib</font>

## [](#header-1)***2. Example***

Examples of using STYX can be found in [**Github Repo**](https://github.com/DNN-STYX/demo). It provides an example for training the MLP models w.r.t. MNIST benchmark under three different methods (traditional training, adversarial training, and STYX) and then making the robustness evaluation. The example can be run with the following command, which takes about 20 minutes:

```
cd Examples
bash run_example.sh
```

In more detail, we consider that in three steps:

## [](#header-1) (1) model's description

```
cd Tool/traditional_training
```
First we need to provide the model's structure like [**Train\_mnist\_MLP.py**](https://www.baidu.com/)  in the current folder. Currently, we supprot five model types: MLP for MNIST (mnist\_MLP), MLP for Fashion-MNIST (fmnist\_MLP), CNN for MNIST (mnist\_CNN), CNN for Fashion-MNIST (fmnist\_CNN), and CNN for CIFAR-10 (cifar10\_CNN).


## [](#header-1) (2) model's generation
Given the paramters like data\_type="mnist", model\_type="MLP" and train\_epoch=20. Next we use the following command to generate the models by different training method.

### [](#header-1) (2.1) traditional_training

```
cd Tool/traditional_training
python traditional_training.py <data_type> <model_name> <train_epoch>
```

### [](#header-1) (2.2) adversarial_training

```
cd Tool/adversarial_training
python adversarial_training.py <data_type> <model_name> <train_epoch>
```

### [](#header-1) (2.3) STYX

```
cd Tool/STYX
python styx.py <data_type> <model_name> <train_epoch> 
```


## [](#header-1) (3) model's evaluation
After that, we use the following command to evaluate the models by different attacking method. Take the attacking method "FGM" and the model trained by STYX as example (i.e. attacking_method="FGM", training\_method="STYX"):

```
cd Tool/evaluation  
python main_evaluation.py <data_type> <model_name> <training_method> <attacking_method>
```

And the evaluation result will be consist of three parts: Accuracy, Robustness, and Time-cost.