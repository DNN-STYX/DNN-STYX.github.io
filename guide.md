## Get Start with STYX

Examples of using STYX can be found in <a href="https://github.com/DNN-STYX/DNN-STYX.github.io/tree/master/demo"> Github Repo</a>. It provides an example for training the MLP models w.r.t. MNIST benchmark under three different methods (traditional training, mutation training, and adversarial training) and then making the robustness evaluation. The example can be run with the following command, which takes about 15 mins:

```markdown
cd Examples
bash run_example.sh
```
In more detail, we consider that in three steps:

### 1.model's description

```markdown
cd STYX/traditional_training
```
First we need to provide the model's structure like <a href="https://www.baidu.com/"> Train\_mnist\_MLP.py</a> in the current folder. 


### 2.model's generation
Given the paramters like model\_name="mnist\_MLP" and train\_epoch=20. Next we use the following command to generate the models by different training method.
#### (1) traditional_training

```markdown
cd STYX/traditional_training
python traditional_training.py $model_name $train_epoch
```
#### (2) mutation_training

```markdown
cd STYX/mutation_training
python mutation_training.py $model_name $train_epoch 
```
#### (3) adversarial_training

```markdown
cd STYX/adversarial_training
python adversarial_training.py $model_name $train_epoch
```

### 3.model's evaluation
After that, we use the following command to evaluate the models by different attacking method. Take the attacking method "FGM" as example:

```markdown
cd STYX/evaluation  
python evaluation.py ["FGM"]
```

And the evaluation result is stored in evaluation.xls under evaluation folder.

## Get Start with STYX