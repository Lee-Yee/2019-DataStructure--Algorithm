我是劉萱

# Week 2

## CLASS

class類別，就像一個模組，可以產出具有相似特性的實體(物件)

例如class動物

第一隻動物是名叫"Nico"(名字)的"狗"

第二隻動物是名叫"Nana"(名字)的"貓"(物種)

他們都會有相同的"屬性"、不同的"參數"

譬如，他們都會有"名字"、"物種"的屬性

每隻動物對應到這個屬性都會有一個特殊的值("參數")

Ex.

class Animal():

　　def __init__(self, name):
 
  　　　self.name = name
  
a = Animal("dog")  #建立一個名叫dog的Animal實體(物件)

print(a.name)

資料來源https://ppt.cc/f1XG3x

## 時間複雜度
|時間複雜度      |             | 
| ------------- |-------------|
|O(1) |陣列讀取|
|O(n) |簡易搜尋|
|O(log n) |二分搜尋|
|O(nlogn) |合併排序|
|O(n²) |選擇排序|
|O(2^n) |費波那契數列|

### O(1)：陣列讀取

時間複雜度為 O(1) 的演算法，代表著不管你輸入多少個東西，程式都會在同一時間跑完。最簡單的例子就是讀取一個陣列中特定索引值的元素。

例如：

countries= ["America"," Australia"," Canada"," France","Taiwan","Japan"]

n = 0

print(countries[n])

\>> " America "

陣列讀取時，不管n等於多少，程式都可以在 “一個步驟” 就到達索引值n所對應的元素，像這樣的案例，我們就會說陣列讀取演算法的時間複雜度為 O(1) 。

### O(n)：簡易搜尋

時間複雜度為 O(n) 的演算法，代表著執行步驟會跟著輸入 n 等比例的增加。例如當 n = 8，程式就會在 8 個步驟完成。最簡單的例子，就是所謂的簡易搜尋。

Ex.

countries= ["America","Australia","Canada","France","Taiwan","Japan"]

for country in countries:

　　if country == "Taiwan":
  
　　　print("I love Taiwan")
    
　　　break
    
　　else:
  
　　　print("This is not Taiwan")
資料來源https://ppt.cc/fQkk8x


# Week 3


# Week 4


自行練習存檔
https://drive.google.com/drive/folders/1RCGUt_diu3g1JgMfRTSrCEFgF1JnXia0?usp=sharing
Markdown Cheatsheet
https://gist.github.com/billy3321/1001749662c370887c63bb30f26c9e6e#h1
