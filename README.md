## Publications
- Emmanouil-Georgios Ieronymakis, "Description of asynchronous service functionality in the OpenAPI standard", Diploma Work, Diploma Work, School of Electrical and Computer Engineering, Technical University of Crete, Chania, Greece, 2024 
https://doi.org/10.26233/heallink.tuc.100531
 - 	Nikolaos Lagogiannis, "OpenAPI SPARQL: Querying OpenAPIOntologies in OWL", Diploma Work, School of Electrical and Computer Engineering, Technical University of Crete, Chania, Greece, 2022
    https://doi.org/10.26233/heallink.tuc.93679

- Fotios Bouraimis, "Instantiating OpenAPI descriptions to the REST services ontology", Diploma Work, School of Electrical and Computer Engineering, Technical University of Crete, Chania, Greece, 2021 https://doi.org/10.26233/heallink.tuc.88861

- F. Bouraimis, N. Mainas and E. G. M. Petrakis, "Composition and polymorphism support in the OpenAPI ontology," in Advanced Information Networking and Applications, vol. 449, Lecture Notes in Networks and Systems, L. Barolli, F. Hussain, T. Enokido, Eds., Cham, Switzerland: Springer Nature, 2022, vol. 1, pp. 309–320. doi: 10.1007/978-3-030-99584-3_2
https://doi.org/10.1007/978-3-030-99584-3_27

 -  Ioannis Apostolakis, Nikolaos Mainas, Euripides G.M. Petrakis, "Simple Querying Service for OpenAPI Descriptions with Semantic Extensions", Information Systems, Vol. 11, pp. 102241, July 2023.
https://doi.org/10.1016/j.is.2023.102241

- Nikolaos Mainas, Fotios Bouraimis, Aikaterini Karavasileiou, Euripides G.M. Petrakis, "Annotated OpenAPI Descriptions and Ontology for REST Services", International Journal on Artificial Intelligence Tools, Vol. 32, No. 6, Sept. 2023.
https://doi.org/10.1142/S0218213023500173

- Chrisa Tsinaraki, Nikolaos Lagogiannis, Nikolaos Mainas, Emmanouil-Georgios Ieronymakis, Euripides G.M. Petrakis, "Querying Semantic OpenAPI Descriptions with OASL", International Journal of Web and Grid Services, 2024, Vol. 20, No. 2, pp. 188-205, 2024.https://doi.org/10.1504/ijwgs.2024.138598

## Jar Run instructions
- Locate the path of the OpenAPI Specification file (.yaml or .json format) you wish to convert
- Locate the path of the desired Output Folder
- execute ``` java -jar "{PATH_TO_JAR}\openapi_ontology_converter.jar" {INPUT_FILE} {OUTPUT_FOLDER}```
- The output turtle file should now be located in the output folder


## Application
- Contains API and GraphDB database containers
- Client can convert OpenAPI Service descriptions to ontology
- Ontology files can be downloaded or imported to GraphDB database
- To deploy the application simply navigate to application folder and run ```sudo docker compose up```
- API is running on localhost port 8080
- GraphDB Interface is running on port 7200
## Where I can find OpenAPI Specification Files
- You can create a free account and download OpenAPI Specification files from https://swagger.io/tools/swaggerhub/ 
- You can also use the descriptions inside the descriptions-1000.zip file included in this repository
