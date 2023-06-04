# Restaurant-Status-Backend

First we need to upload the data into postgre sql, but for that we need to convert the data into a date time format. 





PostgreSql Database
Then we need to save this data frame into a database in the postgresql database. 
I chose postgre sql because it is appropriate for large data and also has a time datatype. 




# Adjusting Time Zones





# Preparing Report

Now to prepare the report of the uptimes and corresponding downtimes of all stores, we need to calculate the amount of times a store was active. 


# Calculating Active Time


To calculate that we need a function that takes 3 parameters store id, day and current time and returns the amount of time (in hours) 
the store was active (meaning the time between start_local_time and end_local_time) in the last hour, last day and last week. 






# Calculating Time Active
For calculating the times active for a given store id we would first find out all reports from the status table which we uploaded on the postgres 
database that can be updated at any time. For that we need to connect to postgresql database and run the following function




# Interpolation Logic
I have divided the time into blocks of 20 minutes. If a store is active at suppose 20:10:00 then I will interpolate that it was active from 20:00:00 to 20:20:20.
Hence I would derive that the store was active for a total of 20 minutes in the last hour. 



Similarly active times would be calculated in the last day and last week using the given data and interpolation logic. 


To calculate uptime and downtime I would subtract the active time by the status time to calculate the active time. 

Active Time - Status Time = Uptime in hours
Status Time - Active Time = Downtime in hours





Similarly I will calculate these times for all the given stores when triggered and a csv file would be returned. 
