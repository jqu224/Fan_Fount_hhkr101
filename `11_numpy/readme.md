## Now we are done with basic [python's] data strutures

⛵️, PLEASE TAKE A LOOK AT THE TUTORIAL MENTIONED BELOW.    


## today we are going to dive into numpy world


          ⏬            
              
#️⃣ A [TUTORIAL](https://github.com/jqu224/Fan_Fount_hhkr101/blob/master/%6011_numpy/review_n_intro_to_new_world.ipynb) on basic Python/Numpy that is necesseary to get started with .....      
            
          ⏫                



You may follow the iPython notebook on github, or clone and execute it locally.                 
The notebook is based on an [earlier version](http://cs231n.github.io/python-numpy-tutorial/) prepared by Justin Johnson.


==========================================================================           
⛵️：             
print t and f是什么意思             
〽️：             
t and f，表示，check if t 和 f both true then return true              
t or f，表示，check if t or f 任一 true then return true       



⛵️：          
not t 和t ！=f呢          
〽️：            
not t 意思是 t取反           
t ！= ：check if t不等于f，不等于就return true 不然则return false，给print去print          
       
       
hackerrank的input：       
di yi hang\n       
di er hang\n       
di san hang\n       
di si hang\n       
di wu hang\n       
di liu hang\n       

如果你写       
a = []       
for _ in range(3):       
     a  += ["first line: "+input()]        
b = []       
for _ in range(3):       
     b  += ["first line: "+input()]        
这里python会把回车符号\n自动视为end of line的标志，每次只会read in 回车符号之前的一整行。       
python怎么逐行读入呢？       
你就理解为读了一行，擦掉一行。       
然后，把a这部分已读3行，还有最后三行等待读取pending，所以等你运行b这部分的时候，就是从第四行读了。         

=========================================
hackerrank的input：         
di yi hang\n         
di er hang\n           
         
如果你写         
a = []         
a = ["first line: " + input()]          
b = ["second line: " + input()]           
python怎么逐行读入呢？         
你就理解为读了一行，擦掉一行。         
然后，把a这部分已读1行，还有最后1行等待读取pending，所以等你运行b这部分的时候，就是从第2行读了。         



