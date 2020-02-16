"# wizdoor-task" 
Run " python manage.py runserver " to start the development server  
The end points are 
(i)   http://127.0.0.1:8000/api/products -> to get all products list 
(ii)  http://127.0.0.1:8000/api/category/count ->count the number of product with different product category 
(iii) http://127.0.0.1:8000/api/customers  -> to get all customers with associate oder details 
      for location wise details you can pass a parameter location = '' , say we want to find customers for badda then 
      http://127.0.0.1:8000/api/customers?location=badda
