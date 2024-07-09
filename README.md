Shopper Service Exercise
=====================


# Agenda (By Priority)
* Microservice Design, Setup, & Coding
    * Options on approach if Diagraming is desired
        * Architecture / Diagramming (Optional) then Implementation
        * Implementation then Architecture / Diagramming (Optional)
* SQL Server (or any rdbms) and a NoSQL development
* Basic Cloud Configuration Familiarity
* CI/CD

# Requirements
* Microservice calls another microservice with a url of *http://3.94.153.172* then merges the data on shopper-data-address.csv
* We prefer shopper-data-address.csv data be imported to a database that the microservice would connect to and retrieve.
* shopper-data-address.csv's first line are the headers (or column names)
* Output of the microservice should likely match the file desired_output.json
