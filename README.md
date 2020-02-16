"# wizdoor-task" 
Run " python manage.py runserver " to start the development server  
The end points are 
(i)   http://127.0.0.1:8000/api/products -> to get all products list 
(ii)  http://127.0.0.1:8000/api/category/count ->count the number of product with different product category 
(iii) http://127.0.0.1:8000/api/customers  -> to get all customers with associate oder details 
      for location wise details you can pass a parameter location = '' , say we want to find customers for badda then 
      http://127.0.0.1:8000/api/customers?location=badda
      
<br>      
      
<h2>#docker </h2><br>
you can also get the docker image and run the project 
<ul>
      <li>
            (i)   pull ther docker image <br>
            docker pull aistiak/wizdoor_task:firsttry
      </li>
      <li>
            (ii)  then run       <br>
            docker run -p 8001:8001 wizdoor_task      
      </li>
      <li>
            (iii) the endpoints are <br>
             http://localhost:8001/api/products <br>
             http://localhost:8001/api/category/count <br> 
             http://localhost:8001/api/customers  <br>    
      </li>
</ul>




