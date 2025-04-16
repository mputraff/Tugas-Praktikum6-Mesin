5 data pertama:
   CompanyID CompanyName Industry         Region  Year  Revenue  ProfitMargin  \
0          1   Company_1   Retail  Latin America  2015    459.2           6.0   
1          1   Company_1   Retail  Latin America  2016    473.8           4.6   
2          1   Company_1   Retail  Latin America  2017    564.9           5.2   
3          1   Company_1   Retail  Latin America  2018    558.4           4.3   
4          1   Company_1   Retail  Latin America  2019    554.5           4.9   

   MarketCap  GrowthRate  ESG_Overall  ESG_Environmental  ESG_Social  \
0      337.5         NaN         57.0               60.7        33.5   
1      366.6         3.2         56.7               58.9        32.8   
2      313.4        19.2         56.5               57.6        34.0   
3      283.0        -1.1         58.0               62.3        33.4   
4      538.1        -0.7         56.6               63.7        30.0   

   ESG_Governance  CarbonEmissions  WaterUsage  EnergyConsumption  
0            76.8          35577.4     17788.7            71154.7  
1            78.5          37314.7     18657.4            74629.4  
2            77.8          45006.4     22503.2            90012.9  
3            78.3          42650.1     21325.1            85300.2  
4            76.1          41799.4     20899.7            83598.8  


Daftar kolom dalam dataset:
- 'CompanyID'
- 'CompanyName'
- 'Industry'
- 'Region'
- 'Year'
- 'Revenue'
- 'ProfitMargin'
- 'MarketCap'
- 'GrowthRate'
- 'ESG_Overall'
- 'ESG_Environmental'
- 'ESG_Social'
- 'ESG_Governance'
- 'CarbonEmissions'
- 'WaterUsage'
- 'EnergyConsumption'


Classification Report:
              precision    recall  f1-score   support

        High       1.00      1.00      1.00       541
         Low       1.00      1.00      1.00      1133
      Medium       1.00      1.00      1.00      1326

    accuracy                           1.00      3000
   macro avg       1.00      1.00      1.00      3000
weighted avg       1.00      1.00      1.00      3000


![output](https://github.com/user-attachments/assets/ec61fab8-6f4f-4582-ab88-e520dcb7c61b)
![image](https://github.com/user-attachments/assets/87eeb929-c13a-46d4-9891-4b29d1045ba0)

Prediksi untuk data baru: High

