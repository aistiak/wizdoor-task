<h1># wizdoor-task"</h1><br> 
Run " python manage.py runserver " to start the development server <br>  
The end points are <br>
<ul>
      <li>
            (i)   http://127.0.0.1:8000/api/products -> to get all products list 
      </li>
      <li>
            (ii)  http://127.0.0.1:8000/api/category/count ->count the number of product with different product category        
      </li>
      <li>  
            (iii) http://127.0.0.1:8000/api/customers  -> to get all customers with associate oder details <br>
            for location wise details you can pass a parameter location = '' , say we want to find customers for badda then <br>
            http://127.0.0.1:8000/api/customers?location=badda         
      </li>
      
</ul>

      
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
            docker run -p 8001:8001 <pulled_image_id>    
      </li>
      <li>
            (iii) the endpoints are <br>
             http://localhost:8001/api/products <br>
             http://localhost:8001/api/category/count <br> 
             http://localhost:8001/api/customers  <br>    
      </li>
</ul>




