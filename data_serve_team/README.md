# Back Market Data Engineering Serve team

This technical assessment will be evaluated regarding these following points:
- Python Programming
- Clean code
- Interoperability
- Scalability
- Versioning
- Automatization

### Data Pipeline Assessment
You can develop & refactor your code (using your versioning tool) following this pipeline:
1. Import the following file from S3 to GCP:  https://backmarket-data-jobs.s3-eu-west-1.amazonaws.com/data/product_catalog.csv (Should we mention the file format?)
2. Make the data available in BigQuery for the feature team A which wants only rows for product with an image
3. Make the data available in BigQuery for the feature team B which wants all rows, even the ones where there are no images

Now Back Market is growing so fast, there are lot more data to import into GCP. How would you adapt your code to scale it up to handle the increasing amount?  

Eventually, more and more feature teams want to expose data and we want to provide a standard way of doing so. How would you build a tooling library and make it available to them (deployment, versioning, …)?

### Tips:
1. Do not reinvent the wheel
2. Do not hesitate to make assumptions and to share them
3. Think about the quality of the code
4. Handle the common errors, what if we start again your code?
5. Take the time you need
6. Enjoy!
