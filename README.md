# bank_api

1. Two form are created to send post request and get rest service accordingly 
2. One form will take ifsc code and return all the details  of the bank
3. Other form fetches bank name and bank city, this form will give all bank in the particular city


4. To get access data directly from link 



 4.1) To get branch details using ifsc code use link:
 
 
 
      a) for localhost: http://127.0.0.1:8000/branch_ifsc/<ifsc_code> 
            eg: http://127.0.0.1:8000/branch_ifsc/ABHY0065030
            
            
      b) for live link : http://dpkjha.pythonanywhere.com/branch_ifsc/<ifsc_code>  
            eg: http://dpkjha.pythonanywhere.com/branch_ifsc/ABHY0065030
   
  4.2) To get all bank details in a city using bank name and city:
  
  
      a) for localhost: http::127.0.0.1:8000/bank_name_city/<bank name>/<city>
              eg: http://127.0.0.1:8000/bank_name_city/state bank of india/mumbai 
                                     OR 
                   use underscore between name and include .(dot) if present in list
                      eg : http://127.0.0.1:8000/bank_name_city/state_bank_of_india/mumbai 
      b) for live link follow 4.2.a) but replace http://127.0.0.1:8000 to http://dpkjha.pythonanywhere.com
      
      
      
      
                             
