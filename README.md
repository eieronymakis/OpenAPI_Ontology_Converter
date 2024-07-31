# OpenAPI_Ontology_Converter

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
